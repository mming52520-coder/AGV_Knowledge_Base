#!/usr/bin/env python3
"""Deterministic ROS 1 code-graph snapshot generator for the AGV V2 worktree.

The scanner is intentionally read-only.  It hashes source evidence, extracts a
conservative graph, and writes a new snapshot without modifying either the
source tree or the immutable V1 snapshot.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import os
import re
import subprocess
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Iterator, Mapping, Sequence


SCHEMA_VERSION = 2
EXTRACTOR_VERSION = "codex-v2-staging-1"
INCLUDED_SUFFIXES = {
    ".c", ".cc", ".cmake", ".cpp", ".cxx", ".h", ".hpp",
    ".launch", ".md", ".msg", ".py", ".service", ".sh", ".srv",
    ".template", ".txt", ".xml", ".yaml", ".yml",
}
EXCLUDED_ROOTS = {".git", ".claude", "build", "devel"}
EXCLUDED_PARTS = {".idea", "__pycache__", "node_modules"}
EXACT_INCLUDED_NAMES = {
    ".catkin_workspace", ".gitignore", "CATKIN_IGNORE", "CMakeLists.txt", "package.xml",
}
BACKUP_RE = re.compile(r"(?:\.bak(?:_|$)|~$|\.orig$|\.swp$)", re.IGNORECASE)
CONTEXT_SOURCE_PATHS = {
    "src/remote_ctrl/scripts/joy_turtlebot.py",
    "src/remote_ctrl/scripts/joy_turtlesim.py",
}
TERMINAL_MIGRATION_PREDICATES = {
    "removed_without_replacement",
    "removed_diagnostic",
}
OUTPUT_ARTIFACTS = {
    "source-files.jsonl",
    "entities.jsonl",
    "relations.jsonl",
    "migration-relations.jsonl",
    "extraction-warnings.jsonl",
    "v1-to-v2-diff.json",
    "V1-to-V2差异摘要.md",
    "manifest.json",
}
EXTRACTION_LIMITATIONS = [
    {
        "limitation_id": "launch-static-xml-only",
        "detail": "Launch extraction reads explicit node/group namespaces only; it does not expand include, arg/substitution, if/unless conditions, or remap semantics.",
    },
    {
        "limitation_id": "endpoint-static-syntax-only",
        "detail": "Endpoint extraction covers direct ROS C++/Python calls, templated C++ subscribe, and static Python _subscribe(_param_topic(...)) defaults; arbitrary macros, runtime-computed names, and dynamic loops remain unresolved.",
    },
    {
        "limitation_id": "relation-removal-not-definitive",
        "detail": "V1 has no per-file source manifest and uses a curated graph, so V1-only relations are extraction_limited candidates rather than definitive runtime removals.",
    },
    {
        "limitation_id": "private-path-disclosure",
        "detail": "The snapshot records source locators and relative evidence paths; publish only to a private repository or sanitize paths before wider disclosure.",
    },
]
ENTITY_COMPARISON_LIMITATION = {
    "limitation_id": "unchanged-graph-semantics-not-source-code",
    "detail": "Entity unchanged compares only declared graph semantic fields (identity/status/ROS name/executable/interface kind/message type/version/vehicles). It does not prove unchanged implementation or configuration source; V1 has no per-file manifest and its hashes are graph-page provenance.",
}


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_json(value: Any) -> str:
    return sha256_bytes(canonical_json(value).encode("utf-8"))


def tree_sha256(root: Path) -> str:
    rows = [
        {"path": path.relative_to(root).as_posix(), "sha256": sha256_bytes(path.read_bytes())}
        for path in sorted((candidate for candidate in root.rglob("*") if candidate.is_file()), key=lambda p: p.relative_to(root).as_posix())
    ]
    return sha256_json(rows)


def validate_non_overlapping_roots(
    source_root: Path,
    v1_root: Path,
    output_root: Path,
    baseline_source_root: Path | None = None,
) -> None:
    source_root = source_root.resolve()
    v1_root = v1_root.resolve()
    output_root = output_root.resolve()
    read_roots: list[tuple[Path, str]] = [(source_root, "source"), (v1_root, "V1")]
    if baseline_source_root is not None:
        read_roots.append((baseline_source_root.resolve(), "V1 source"))
    for read_root, label in read_roots:
        if output_root == read_root or read_root in output_root.parents:
            raise ValueError(f"output must not equal or nest the {label} root: {output_root}")
        if output_root in read_root.parents:
            raise ValueError(f"{label} root must not nest the output root: {output_root}")


def is_unsafe_linked_artifact(path: Path) -> bool:
    """Reject output aliases that could redirect writes into a read-only tree."""
    if path.is_symlink():
        return True
    is_junction = getattr(path, "is_junction", None)
    if callable(is_junction) and is_junction():
        return True
    try:
        return path.exists() and path.stat().st_nlink > 1
    except OSError:
        return True


def validate_utf8_text_artifacts(output_root: Path) -> None:
    """Reject lossy decoding before graph artifacts are trusted or projected."""
    for name in sorted(OUTPUT_ARTIFACTS):
        path = output_root / name
        try:
            text = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError as error:
            raise ValueError(f"output artifact is not valid UTF-8: {name}") from error
        if "\ufffd" in text:
            raise ValueError(
                f"output artifact contains Unicode replacement character U+FFFD: {name}"
            )


def load_baseline_source_context(
    v1_root: Path,
    baseline_source_root: Path | None,
) -> dict[str, Any]:
    """Describe optional V1-source evidence without overstating its integrity."""
    source_set: dict[str, Any] = {}
    source_sets_path = v1_root / "source-sets.jsonl"
    if source_sets_path.is_file():
        matches = [
            row for row in _load_jsonl(source_sets_path)
            if row.get("source_set") == "vehicle-3"
        ]
        if len(matches) != 1:
            raise ValueError(f"expected exactly one vehicle-3 source set, got {len(matches)}")
        source_set = matches[0]
    limitation = (
        "The immutable V1 snapshot retained only an aggregate vehicle-3 source-set hash, "
        "not a per-file manifest. Per-file hashes below are contextual hashes of the "
        "current-machine V1 source worktree and cannot prove byte identity with the "
        "original V1 extraction input."
    )
    if baseline_source_root is None:
        return {
            "available": False,
            "source_locator": "",
            "source_kind": "not_provided",
            "git_state": {},
            "v1_source_set": source_set,
            "git_head_matches_v1_source_set": None,
            "aggregate_hash_reverified": False,
            "integrity_limitation": limitation,
        }
    baseline_source_root = baseline_source_root.resolve()
    if not baseline_source_root.is_dir():
        raise ValueError(f"V1 source root is not a directory: {baseline_source_root}")
    git_state = inspect_git_state(baseline_source_root)
    expected_head = str(source_set.get("git_head", ""))
    actual_head = str(git_state.get("head", ""))
    return {
        "available": True,
        "source_locator": baseline_source_root.as_posix(),
        "source_kind": "contextual_current_machine_v1_source_worktree",
        "git_state": git_state,
        "v1_source_set": source_set,
        "git_head_matches_v1_source_set": bool(expected_head and actual_head == expected_head),
        "aggregate_hash_reverified": False,
        "integrity_limitation": limitation,
    }


def slugify(value: str) -> str:
    value = value.strip().replace("::", "-")
    value = re.sub(r"^[/~]+", "", value)
    value = re.sub(r"[^0-9A-Za-z_]+", "-", value)
    value = value.replace("_", "-")
    value = re.sub(r"-+", "-", value).strip("-").lower()
    return value or "unnamed"


def normalize_ros_name(value: str) -> str:
    value = value.strip()
    if not value:
        return value
    if value.startswith("~"):
        return "~" + re.sub(r"/+", "/", value[1:]).lstrip("/")
    return "/" + re.sub(r"/+", "/", value).strip("/")


def _executable_key(executable: str) -> str:
    """Normalize launch-only filename suffixes to their source/CMake identity."""
    return executable[:-3] if executable.endswith(".py") else executable


def classify_path(relative_path: str) -> tuple[bool, str]:
    """Return inclusion and an auditable reason for every filesystem file."""
    path = PurePosixPath(relative_path.replace("\\", "/"))
    parts = path.parts
    if not parts:
        return False, "empty_path"
    if parts[0] in EXCLUDED_ROOTS:
        return False, f"excluded_root:{parts[0]}"
    if any(part in EXCLUDED_PARTS for part in parts):
        return False, "excluded_tool_cache"
    if parts[0] == "deploy":
        if path.name in EXACT_INCLUDED_NAMES or path.suffix.lower() in INCLUDED_SUFFIXES:
            return True, "deployment_source"
        return False, "unsupported_deployment_artifact"
    if BACKUP_RE.search(path.name):
        return False, "backup_or_editor_artifact"
    if path.name.startswith("tmp_"):
        return False, "temporary_artifact"
    if path.name in EXACT_INCLUDED_NAMES:
        return True, "exact_source_name"
    if path.suffix.lower() in INCLUDED_SUFFIXES:
        return True, "source_or_document_extension"
    return False, "unsupported_or_generated_extension"


def source_disposition(relative_path: str) -> tuple[str, str]:
    included, reason = classify_path(relative_path)
    normalized = relative_path.replace("\\", "/")
    if not included:
        return "excluded", reason
    if normalized.startswith("src/_archived_battery_management/"):
        return "context", "archived_source_context"
    if normalized in CONTEXT_SOURCE_PATHS:
        return "context", "tutorial_source_context"
    return "included", reason


def is_primary_node_source(package_name: str, relative_path: str) -> bool:
    disposition, _ = source_disposition(relative_path)
    return disposition == "included" and package_name != "battery_management"


def scan_source_files(source_root: Path) -> tuple[list[dict[str, Any]], dict[str, str], str]:
    """Inventory every file while hashing only the declared source scope."""
    records: list[dict[str, Any]] = []
    hashes: dict[str, str] = {}
    all_files = sorted(
        (path for path in source_root.rglob("*") if path.is_file()),
        key=lambda path: _relative(path, source_root),
    )
    for path in all_files:
        relative = _relative(path, source_root)
        disposition, reason = source_disposition(relative)
        digest: str | None = None
        if disposition in {"included", "context"}:
            digest = sha256_bytes(path.read_bytes())
            hashes[relative] = digest
        records.append({
            "path": relative,
            "size": path.stat().st_size,
            "disposition": disposition,
            "reason": reason,
            "sha256": digest,
        })
    fingerprint_rows = [
        {"path": path, "sha256": digest} for path, digest in sorted(hashes.items())
    ]
    return records, hashes, sha256_json(fingerprint_rows)


def _run_git(source_root: Path, *args: str) -> tuple[int, bytes]:
    process = subprocess.run(
        ["git", "-C", str(source_root), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return process.returncode, process.stdout


def inspect_git_state(source_root: Path) -> dict[str, Any]:
    head_code, head_raw = _run_git(source_root, "rev-parse", "HEAD")
    branch_code, branch_raw = _run_git(source_root, "branch", "--show-current")
    status_code, status_raw = _run_git(
        source_root, "status", "--porcelain=v1", "-z", "--untracked-files=all"
    )
    head = head_raw.decode("ascii", errors="replace").strip() if head_code == 0 else ""
    branch = branch_raw.decode("utf-8", errors="replace").strip() if branch_code == 0 else ""
    if status_code != 0:
        return {
            "repository": False,
            "head": head,
            "branch": branch,
            "dirty": None,
            "status_counts": {},
            "status_sha256": "",
        }
    decoded = status_raw.decode("utf-8", errors="surrogateescape")
    fields = decoded.rstrip("\0").split("\0") if decoded else []
    changes: list[dict[str, str]] = []
    index = 0
    while index < len(fields):
        field = fields[index]
        if len(field) < 3:
            index += 1
            continue
        code, path = field[:2], field[3:].replace("\\", "/")
        row = {"status": code, "path": path}
        if ("R" in code or "C" in code) and index + 1 < len(fields):
            index += 1
            row["original_path"] = fields[index].replace("\\", "/")
        changes.append(row)
        index += 1
    changes.sort(key=canonical_json)
    return {
        "repository": True,
        "head": head,
        "branch": branch,
        "dirty": bool(changes),
        "status_counts": dict(sorted(Counter(row["status"] for row in changes).items())),
        "status_sha256": sha256_bytes(status_raw),
        "changes": changes,
    }


class V1IdentityIndex:
    """Strong-key lookup that never performs fuzzy or silent entity merges."""

    def __init__(self, entities: Sequence[Mapping[str, Any]]):
        self.entity_by_uid: dict[str, Mapping[str, Any]] = {
            str(entity.get("entity_uid", "")): entity for entity in entities
        }
        self.reserved_uids = set(self.entity_by_uid)
        self.package_by_title: dict[str, str] = {}
        self.node_by_title: dict[str, str | None] = {}
        self.node_by_executable: dict[str, str | None] = {}
        self.node_by_ros_name: dict[str, str | None] = {}
        self.node_by_package_executable: dict[tuple[str, str], str | None] = {}
        self.node_by_package_ros_name: dict[tuple[str, str], str | None] = {}
        self.node_metadata: dict[str, tuple[str, str, str]] = {}
        self.interface_by_key: dict[tuple[str, str], str | None] = {}

        def add_unique(index: dict[Any, str | None], key: Any, uid: str) -> None:
            if not key:
                return
            if key in index and index[key] != uid:
                index[key] = None
            else:
                index[key] = uid

        for entity in entities:
            uid = str(entity.get("entity_uid", ""))
            semantic = entity.get("semantic") or {}
            entity_type = entity.get("type")
            if entity_type == "ros_package":
                self.package_by_title[str(entity.get("title", ""))] = uid
            elif entity_type == "ros_node":
                executable = _executable_key(str(semantic.get("executable", "")))
                ros_name = normalize_ros_name(str(semantic.get("ros_name", "")))
                package_uid = str(entity.get("package_uid", ""))
                package_name = (
                    package_uid.removeprefix("agv:ros:package:")
                    if package_uid.startswith("agv:ros:package:")
                    else str(semantic.get("package", ""))
                )
                title = str(entity.get("title", ""))
                add_unique(self.node_by_title, title, uid)
                add_unique(self.node_by_executable, executable, uid)
                add_unique(self.node_by_ros_name, ros_name, uid)
                if package_name:
                    add_unique(self.node_by_package_executable, (package_name, executable), uid)
                    add_unique(self.node_by_package_ros_name, (package_name, ros_name), uid)
                self.node_metadata[uid] = (package_name, executable, ros_name)
            elif entity_type == "ros_interface":
                ros_name = str(semantic.get("ros_name", ""))
                kind = str(semantic.get("interface_kind", ""))
                if ros_name and not kind.endswith("_group") and "+" not in ros_name and "*" not in ros_name:
                    add_unique(self.interface_by_key, (normalize_ros_name(ros_name), kind), uid)

    def package_uid(self, package_name: str) -> str:
        return self.package_by_title.get(package_name, f"agv:ros:package:{package_name}")

    def node_uid(
        self,
        executable: str,
        ros_name: str = "",
        fallback_name: str = "",
        package_name: str = "",
        executable_unique: bool = True,
    ) -> str:
        executable_key = _executable_key(executable)
        fallback_key = _executable_key(fallback_name) if fallback_name else executable_key
        fallback_source = fallback_name or executable or ros_name
        fallback = re.sub(r"[^0-9A-Za-z_]+", "-", fallback_source.strip("/~")).strip("-").lower()
        canonical_override = bool(fallback_name and fallback_key != executable_key)
        if canonical_override:
            titled_uid = self.node_by_title.get(fallback_name)
            if titled_uid:
                return titled_uid
            return f"agv:ros:node:{fallback or 'unnamed'}"

        package_uid = self.node_by_package_executable.get((package_name, executable_key))
        if package_uid:
            return package_uid
        executable_uid = self.node_by_executable.get(executable_key) if executable_unique else None
        if executable_uid:
            known_package = self.node_metadata[executable_uid][0]
            if not known_package or not package_name or known_package == package_name:
                return executable_uid

        normalized_ros_name = normalize_ros_name(ros_name)
        package_ros_uid = self.node_by_package_ros_name.get((package_name, normalized_ros_name))
        ros_uid = package_ros_uid or (
            self.node_by_ros_name.get(normalized_ros_name) if executable_unique else None
        )
        if ros_uid:
            known_package, known_executable, _ = self.node_metadata[ros_uid]
            package_matches = not known_package or not package_name or known_package == package_name
            if package_matches and known_executable == executable_key:
                return ros_uid

        candidate = f"agv:ros:node:{fallback or 'unnamed'}"
        if not executable_unique and package_name:
            candidate += f"-{slugify(package_name)}"
        if candidate in self.reserved_uids:
            candidate += f"-{slugify(package_name or executable_key or 'new')}"
        return candidate

    def interface_uid(self, ros_name: str, interface_kind: str) -> str:
        normalized = normalize_ros_name(ros_name)
        existing_uid = self.interface_by_key.get((normalized, interface_kind))
        if existing_uid:
            return existing_uid
        prefix = "service" if interface_kind == "service" else "interface"
        candidate = f"agv:ros:{prefix}:{slugify(normalized)}"
        if candidate in self.reserved_uids:
            candidate += "-atomic"
        return candidate

    @staticmethod
    def type_uid(package_name: str, type_name: str, interface_kind: str) -> str:
        prefix = "message" if interface_kind == "message_type" else "service-type"
        return f"agv:ros:{prefix}:{slugify(package_name)}-{slugify(type_name)}"


def diff_entities(
    baseline_entities: Sequence[Mapping[str, Any]],
    target_entities: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    baseline = {str(row["entity_uid"]): row for row in baseline_entities}
    target = {str(row["entity_uid"]): row for row in target_entities}
    shared = sorted(baseline.keys() & target.keys())
    unchanged = [
        uid for uid in shared
        if canonical_json(baseline[uid].get("semantic") or {})
        == canonical_json(target[uid].get("semantic") or {})
    ]
    modified = [uid for uid in shared if uid not in set(unchanged)]
    added = sorted(target.keys() - baseline.keys())
    removed = sorted(baseline.keys() - target.keys())
    counts = {
        "baseline": len(baseline),
        "target": len(target),
        "matched": len(shared),
        "unchanged": len(unchanged),
        "modified": len(modified),
        "added": len(added),
        "removed": len(removed),
    }
    assert counts["baseline"] == counts["matched"] + counts["removed"]
    assert counts["target"] == counts["matched"] + counts["added"]
    assert counts["matched"] == counts["unchanged"] + counts["modified"]
    return {
        "counts": counts,
        "unchanged": unchanged,
        "modified": modified,
        "added": added,
        "removed": removed,
    }


def classify_scope_changes(
    baseline_entities: Sequence[Mapping[str, Any]],
    target_entities: Sequence[Mapping[str, Any]],
    *,
    baseline_has_file_manifest: bool,
) -> list[dict[str, Any]]:
    changes: list[dict[str, Any]] = []
    if not baseline_has_file_manifest:
        changes.append({
            "change_kind": "baseline_manifest_limitation",
            "classification": "scope_change",
            "detail": "V1 has aggregate source-set hashes but no per-file manifest; file-level deletion claims are unavailable.",
        })
    baseline_packages = {
        str(row["entity_uid"]) for row in baseline_entities if row.get("type") == "ros_package"
    }
    target_packages = {
        str(row["entity_uid"]) for row in target_entities if row.get("type") == "ros_package"
    }
    added_packages = sorted(target_packages - baseline_packages)
    if added_packages:
        changes.append({
            "change_kind": "expanded_package_scope",
            "classification": "scope_change",
            "entity_uids": added_packages,
        })
    removed_packages = sorted(baseline_packages - target_packages)
    if removed_packages:
        changes.append({
            "change_kind": "contracted_package_scope",
            "classification": "scope_change_needs_review",
            "entity_uids": removed_packages,
        })
    return changes


def _group_members(group_name: str, target_names: Sequence[str]) -> list[str]:
    explicit = [normalize_ros_name(part.strip()) for part in group_name.split("+") if part.strip()]
    if "*" not in group_name:
        return [name for name in target_names if name in explicit]
    regex_parts: list[str] = []
    for part in group_name.split("+"):
        normalized = normalize_ros_name(part.strip())
        regex_parts.append("^" + re.escape(normalized).replace(r"\*", ".*") + "$")
    patterns = [re.compile(pattern) for pattern in regex_parts]
    return [name for name in target_names if any(pattern.match(name) for pattern in patterns)]


def build_group_decompositions(
    baseline_entities: Sequence[Mapping[str, Any]],
    target_entities: Sequence[Mapping[str, Any]],
    baseline_snapshot: str,
    target_snapshot: str,
) -> list[dict[str, Any]]:
    targets_by_kind: dict[str, dict[str, str]] = {"topic": {}, "service": {}}
    for row in target_entities:
        semantic = row.get("semantic") or {}
        target_kind = str(semantic.get("interface_kind", ""))
        if row.get("type") == "ros_interface" and target_kind in targets_by_kind:
            targets_by_kind[target_kind][normalize_ros_name(str(semantic.get("ros_name", "")))] = str(row["entity_uid"])
    rows: list[dict[str, Any]] = []
    for entity in baseline_entities:
        semantic = entity.get("semantic") or {}
        kind = str(semantic.get("interface_kind", ""))
        name = str(semantic.get("ros_name", ""))
        if entity.get("type") != "ros_interface" or not (kind.endswith("_group") or "+" in name or "*" in name):
            continue
        member_kind = kind.removesuffix("_group") if kind.endswith("_group") else "topic"
        targets = targets_by_kind.get(member_kind, {})
        for member in sorted(_group_members(name, sorted(targets))):
            rows.append({
                "from_snapshot": baseline_snapshot,
                "from_entity_uid": str(entity["entity_uid"]),
                "predicate": "decomposed_into",
                "to_snapshot": target_snapshot,
                "to_entity_uid": targets[member],
                "confidence": 1.0,
                "match_method": "explicit_group_member",
                "evidence": {"baseline_ros_name": name, "target_ros_name": member},
            })
    return sorted(rows, key=lambda row: canonical_json(row))


@dataclasses.dataclass
class GraphResult:
    entities: list[dict[str, Any]]
    relations: list[dict[str, Any]]
    warnings: list[dict[str, Any]]


@dataclasses.dataclass
class PackageInfo:
    name: str
    version: str
    relative_dir: str
    absolute_dir: Path
    dependencies: list[str]
    status: str


@dataclasses.dataclass
class NodeInfo:
    package: PackageInfo
    executable: str
    ros_name: str
    source_paths: list[str]
    launch_names: list[str]
    status: str
    identity_name: str


@dataclasses.dataclass(frozen=True)
class EndpointUse:
    node_uid: str
    package_uid: str
    predicate: str
    ros_name: str
    interface_kind: str
    message_type: str
    path: str
    line: int
    expression: str


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _strip_cmake_comments(text: str) -> str:
    return "\n".join(line.split("#", 1)[0] for line in text.splitlines())


def _package_status(name: str, relative_dir: str) -> str:
    if any(part.startswith("_archived") for part in PurePosixPath(relative_dir).parts):
        return "archived"
    if name == "agv_legacy":
        return "compatibility"
    if name.startswith("agv_") or name == "dyp_ultrasonic_driver":
        return "active"
    if name in {
        "analog_controlled_motor", "battery_management", "bringup", "encoder",
        "magnetic_controlled_motor", "odometer", "relay", "remote_ctrl",
        "trajectory_recorder", "ultrasonic_controlled_motor", "wheeltec_base",
    }:
        return "compatibility"
    return "available"


def _load_packages(source_root: Path, warnings: list[dict[str, Any]]) -> list[PackageInfo]:
    packages: list[PackageInfo] = []
    for package_xml in sorted((source_root / "src").rglob("package.xml"), key=lambda p: _relative(p, source_root)):
        relative = _relative(package_xml, source_root)
        included, _ = classify_path(relative)
        if not included:
            continue
        try:
            root = ET.fromstring(_read_text(package_xml))
            name = (root.findtext("name") or "").strip()
            version = (root.findtext("version") or "").strip()
            if not name:
                raise ValueError("package name is empty")
            dependencies = sorted({
                (element.text or "").strip()
                for tag in ("depend", "build_depend", "build_export_depend", "exec_depend")
                for element in root.findall(tag)
                if (element.text or "").strip()
            })
            relative_dir = _relative(package_xml.parent, source_root)
            packages.append(PackageInfo(
                name=name,
                version=version,
                relative_dir=relative_dir,
                absolute_dir=package_xml.parent,
                dependencies=dependencies,
                status=_package_status(name, relative_dir),
            ))
        except (ET.ParseError, ValueError) as exc:
            warnings.append({"kind": "invalid_package_xml", "path": relative, "detail": str(exc)})
    seen: set[str] = set()
    unique: list[PackageInfo] = []
    for package in sorted(packages, key=lambda p: (p.name, p.relative_dir)):
        if package.name in seen:
            warnings.append({
                "kind": "duplicate_package_name",
                "package": package.name,
                "path": f"{package.relative_dir}/package.xml",
            })
            continue
        seen.add(package.name)
        unique.append(package)
    return unique


def _cmake_targets(package: PackageInfo, source_root: Path) -> dict[str, list[str]]:
    cmake = package.absolute_dir / "CMakeLists.txt"
    if not cmake.exists():
        return {}
    text = _strip_cmake_comments(_read_text(cmake))
    targets: dict[str, list[str]] = {}
    for match in re.finditer(r"add_executable\s*\(\s*([^\s\)]+)(.*?)\)", text, re.DOTALL):
        target, body = match.group(1), match.group(2)
        if "$" in target:
            continue
        sources = [
            _relative(package.absolute_dir / token, source_root)
            for token in re.findall(r"[^\s\)]+\.(?:cxx|cpp|cc|c)(?![A-Za-z0-9_])", body)
            if (package.absolute_dir / token).exists()
        ]
        targets[target] = sources
    for match in re.finditer(r"foreach\s*\(\s*node\s+([^\)]+)\)(.*?)endforeach\s*\(\s*\)", text, re.DOTALL):
        if "add_executable(${node}src/${node}.cpp)" not in re.sub(r"\s+", "", match.group(2)):
            # Fall through to the source-file discovery below; this branch is
            # deliberately conservative around arbitrary CMake metaprogramming.
            continue
        for target in match.group(1).split():
            candidate = package.absolute_dir / "src" / f"{target}.cpp"
            if candidate.exists():
                targets[target] = [_relative(candidate, source_root)]
    return targets


CPP_INIT_RE = re.compile(r"ros::init\s*\([^;]*?['\"]([^'\"]+)['\"]", re.DOTALL)
PY_INIT_RE = re.compile(r"rospy\.init_node\s*\(\s*['\"]([^'\"]+)['\"]")


def _join_ros_namespace(namespace: str, name: str) -> str:
    if "$" in namespace or "$" in name:
        return ""
    return normalize_ros_name("/".join(part.strip("/") for part in (namespace, name) if part.strip("/")))


def scan_launch_nodes(launch_path: Path) -> list[dict[str, str]]:
    root = ET.fromstring(_read_text(launch_path))
    rows: list[dict[str, str]] = []

    def walk(element: ET.Element, namespace: str) -> None:
        local_namespace = namespace
        if element.tag == "group" and element.attrib.get("ns"):
            local_namespace = _join_ros_namespace(namespace, element.attrib["ns"])
        if element.tag == "node":
            node_namespace = local_namespace
            if element.attrib.get("ns"):
                node_namespace = _join_ros_namespace(local_namespace, element.attrib["ns"])
            name = element.attrib.get("name") or element.attrib.get("type", "")
            ros_name = _join_ros_namespace(node_namespace, name)
            if ros_name:
                rows.append({
                    "package": element.attrib.get("pkg", ""),
                    "executable": element.attrib.get("type", ""),
                    "ros_name": ros_name,
                })
        for child in element:
            walk(child, local_namespace)

    walk(root, "")
    return rows


def _launch_aliases(source_root: Path, warnings: list[dict[str, Any]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for launch in sorted((source_root / "src").rglob("*.launch"), key=lambda p: _relative(p, source_root)):
        relative = _relative(launch, source_root)
        try:
            launch_rows = scan_launch_nodes(launch)
        except ET.ParseError as exc:
            warnings.append({"kind": "invalid_launch_xml", "path": relative, "detail": str(exc)})
            continue
        for row in launch_rows:
            if row["package"] and row["executable"] and "$" not in row["executable"]:
                rows.append({**row, "path": relative})
    return sorted(rows, key=canonical_json)


def _production_executables(source_root: Path) -> set[str]:
    launch = source_root / "src" / "agv_bringup" / "launch" / "vehicle.launch"
    if not launch.exists():
        return set()
    try:
        rows = scan_launch_nodes(launch)
    except ET.ParseError:
        return set()
    return {_executable_key(row["executable"]) for row in rows}


def _node_identity_name(package_name: str, executable: str) -> str:
    explicit = {
        ("magnetic_controlled_motor", "motor_control"): "magnetic_motor_control",
        ("ultrasonic_controlled_motor", "motor_control_node"): "ultrasonic_motor_control",
    }
    return explicit.get((package_name, executable), executable)


def _node_status(package: PackageInfo, executable: str, production: set[str]) -> str:
    lowered = executable.lower()
    if "probe" in lowered:
        return "diagnostic"
    if executable in production:
        return "active"
    if package.status in {"archived", "compatibility"}:
        return package.status
    return "available"


def _discover_nodes(
    source_root: Path,
    packages: Sequence[PackageInfo],
    warnings: list[dict[str, Any]],
) -> list[NodeInfo]:
    production = _production_executables(source_root)
    by_key: dict[tuple[str, str], NodeInfo] = {}
    for package in packages:
        targets = _cmake_targets(package, source_root)
        source_to_target = {
            path: target for target, paths in targets.items() for path in paths
        }
        for target, source_paths in targets.items():
            primary_sources = [
                path for path in source_paths if is_primary_node_source(package.name, path)
            ]
            if not primary_sources:
                if package.status != "archived":
                    warnings.append({
                        "kind": "cmake_target_without_resolved_source",
                        "package": package.name,
                        "executable": target,
                    })
                continue
            key = (package.name, target)
            by_key[key] = NodeInfo(
                package=package,
                executable=target,
                ros_name=normalize_ros_name(target),
                source_paths=sorted(primary_sources),
                launch_names=[],
                status=_node_status(package, target, production),
                identity_name=_node_identity_name(package.name, target),
            )
        candidates = sorted(
            list(package.absolute_dir.rglob("*.cpp")) + list(package.absolute_dir.rglob("*.py")),
            key=lambda path: _relative(path, source_root),
        )
        for path in candidates:
            relative = _relative(path, source_root)
            if not is_primary_node_source(package.name, relative):
                continue
            text = _read_text(path)
            match = CPP_INIT_RE.search(text) if path.suffix == ".cpp" else PY_INIT_RE.search(text)
            target = source_to_target.get(relative)
            if not match:
                continue
            executable = target or path.stem
            ros_name = normalize_ros_name(match.group(1))
            key = (package.name, executable)
            if key not in by_key:
                by_key[key] = NodeInfo(
                    package=package,
                    executable=executable,
                    ros_name=ros_name,
                    source_paths=[relative],
                    launch_names=[],
                    status=_node_status(package, executable, production),
                    identity_name=_node_identity_name(package.name, executable),
                )
            else:
                by_key[key].ros_name = ros_name
                if relative in by_key[key].source_paths:
                    by_key[key].source_paths.remove(relative)
                by_key[key].source_paths.insert(0, relative)

    package_by_name = {package.name: package for package in packages}
    production_launch = "src/agv_bringup/launch/vehicle.launch"
    aliases_by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in _launch_aliases(source_root, warnings):
        aliases_by_key[(row["package"], _executable_key(row["executable"]))].append(row)
    for key, aliases in aliases_by_key.items():
        package_name, executable = key
        node = by_key.get(key)
        if node is None:
            package = package_by_name.get(package_name)
            if package is None or package.status == "archived":
                continue
            warnings.append({
                "kind": "launch_node_without_source_evidence",
                "package": package_name,
                "executable": executable,
                "launch_paths": sorted({row["path"] for row in aliases}),
            })
            continue
        node.launch_names = sorted({row["ros_name"] for row in aliases})
        production_aliases = [row["ros_name"] for row in aliases if row["path"] == production_launch]
        package_local_aliases = [
            row["ros_name"] for row in aliases
            if row["path"].startswith(f"{node.package.relative_dir}/launch/")
        ]
        if production_aliases:
            node.ros_name = sorted(production_aliases)[0]
        elif package_local_aliases:
            node.ros_name = sorted(package_local_aliases)[0]
    return sorted(by_key.values(), key=lambda node: (node.package.name, node.executable))


def _variable_defaults(text: str) -> dict[str, str]:
    values: dict[str, str] = {}
    patterns = [
        r"std::string\s+(\w+_?)\s*=\s*(?:std::string\s*\()?\s*['\"]([^'\"]+)['\"]",
        r"std::string\s+(\w+_?)\s*\{\s*['\"]([^'\"]+)['\"]\s*\}",
        r"\.param\s*<\s*std::string\s*>\s*\(\s*['\"][^'\"]+['\"]\s*,\s*(\w+_?)\s*,\s*(?:std::string\s*\()?\s*['\"]([^'\"]+)['\"]",
        r"\b(\w+_)\s*\(\s*['\"]([^'\"]+)['\"]\s*\)",
    ]
    for pattern in patterns:
        for match in re.finditer(pattern, text, re.DOTALL):
            values[match.group(1)] = match.group(2)
    return values


def _resolve_name(expression: str, variables: Mapping[str, str]) -> str:
    expression = expression.strip()
    literal = re.match(r"(?:std::string\s*\()?\s*['\"]([^'\"]+)['\"]", expression)
    if literal:
        return normalize_ros_name(literal.group(1))
    if re.fullmatch(r"(?:/|~)[A-Za-z0-9_][A-Za-z0-9_./-]*", expression):
        return normalize_ros_name(expression)
    variable = re.match(r"([A-Za-z_]\w*)", expression)
    if variable and variable.group(1) in variables:
        return normalize_ros_name(variables[variable.group(1)])
    return ""


def _normalize_message_type(value: str) -> str:
    return re.sub(r"\s+", "", value.strip().lstrip(":" )).replace("::", "/")


def _python_imported_ros_types(text: str) -> dict[str, str]:
    """Resolve simple ``from package.msg/srv import Type`` class references."""
    imported: dict[str, str] = {}
    pattern = r"^\s*from\s+([A-Za-z_]\w*)\.(msg|srv)\s+import\s+([^\n#]+)"
    for match in re.finditer(pattern, text, re.MULTILINE):
        package, _, symbols = match.groups()
        for raw_symbol in symbols.split(","):
            symbol = raw_symbol.strip().strip("()")
            alias_match = re.fullmatch(r"([A-Za-z_]\w*)(?:\s+as\s+([A-Za-z_]\w*))?", symbol)
            if not alias_match:
                continue
            original, alias = alias_match.groups()
            imported[alias or original] = f"{package}/{original}"
    return imported


def _python_enclosing_function_name(text: str, position: int) -> str:
    matches = list(re.finditer(r"^\s*def\s+([A-Za-z_]\w*)\s*\(", text[:position], re.MULTILINE))
    return matches[-1].group(1) if matches else ""


def _endpoint_matches(
    text: str,
    suffix: str,
) -> Iterator[tuple[re.Match[str], str, str, str]]:
    if suffix == ".py":
        patterns = [
            (r"rospy\.Publisher\s*\(\s*([^,\n]+)\s*,\s*([^,\n\)]+)", "publishes", "topic", "expression_first"),
            (r"rospy\.Subscriber\s*\(\s*([^,\n]+)\s*,\s*([^,\n\)]+)", "subscribes", "topic", "expression_first"),
            (r"rospy\.Service\s*\(\s*([^,\n]+)\s*,\s*([^,\n\)]+)", "provides_services", "service", "expression_first"),
            (r"rospy\.ServiceProxy\s*\(\s*([^,\n]+)\s*,\s*([^,\n\)]+)", "uses_services", "service", "expression_first"),
            (
                r"(?:self\.)?_subscribe\s*\(\s*(?:self\.)?_param_topic\s*\(\s*['\"][^'\"]+['\"]\s*,\s*['\"]([^'\"]+)['\"]\s*\)\s*,\s*([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)",
                "subscribes", "topic", "expression_first",
            ),
            (
                r"(?:self\.)?_subscribe\s*\(\s*['\"]([^'\"]+)['\"]\s*,\s*([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)",
                "subscribes", "topic", "expression_first",
            ),
        ]
    else:
        patterns = [
            (r"\badvertise\s*<\s*([^>]+)>\s*\(\s*([^,\n]+)", "publishes", "topic", "message_first"),
            (r"\bsubscribe\s*<\s*([^>]+)>\s*\(\s*([^,\n]+)", "subscribes", "topic", "message_first"),
            (r"\bsubscribe\s*\(\s*([^,\n]+)", "subscribes", "topic", "expression_only"),
            (r"\badvertiseService\s*\(\s*([^,\n]+)", "provides_services", "service", "expression_only"),
            (r"\bserviceClient\s*<\s*([^>]+)>\s*\(\s*([^,\n]+)", "uses_services", "service", "message_first"),
        ]
    for pattern, predicate, kind, layout in patterns:
        for match in re.finditer(pattern, text, re.MULTILINE):
            groups = match.groups()
            if layout == "message_first":
                message_type, expression = groups[0], groups[1]
            elif layout == "expression_first":
                expression, message_type = groups[0], groups[1]
            else:
                expression, message_type = groups[0], ""
            yield match, predicate, kind, f"{expression}\0{message_type}"


def _extract_endpoint_uses(
    source_root: Path,
    nodes: Sequence[NodeInfo],
    identity_index: V1IdentityIndex,
    warnings: list[dict[str, Any]],
) -> list[EndpointUse]:
    uses: list[EndpointUse] = []
    executable_counts = Counter(_executable_key(node.executable) for node in nodes)
    for node in nodes:
        node_uid = identity_index.node_uid(
            node.executable,
            node.ros_name,
            node.identity_name,
            node.package.name,
            executable_counts[_executable_key(node.executable)] == 1,
        )
        package_uid = identity_index.package_uid(node.package.name)
        for relative in node.source_paths:
            path = source_root / PurePosixPath(relative)
            if not path.exists() or path.suffix.lower() not in {".cpp", ".cc", ".cxx", ".py"}:
                continue
            text = _read_text(path)
            variables = _variable_defaults(text)
            imported_types = _python_imported_ros_types(text) if path.suffix.lower() == ".py" else {}
            for match, predicate, kind, packed in _endpoint_matches(text, path.suffix.lower()):
                expression, message_type = packed.split("\0", 1)
                ros_name = _resolve_name(expression, variables)
                if not ros_name:
                    if (
                        path.suffix.lower() == ".py"
                        and expression.strip() == "topic"
                        and _python_enclosing_function_name(text, match.start()) == "_subscribe"
                    ):
                        continue
                    warnings.append({
                        "kind": "unresolved_interface_expression",
                        "path": relative,
                        "line": _line_number(text, match.start()),
                        "operation": predicate,
                        "expression": expression.strip()[:160],
                    })
                    continue
                normalized_message_type = _normalize_message_type(message_type)
                normalized_message_type = imported_types.get(
                    normalized_message_type,
                    normalized_message_type,
                )
                uses.append(EndpointUse(
                    node_uid=node_uid,
                    package_uid=package_uid,
                    predicate=predicate,
                    ros_name=ros_name,
                    interface_kind=kind,
                    message_type=normalized_message_type,
                    path=relative,
                    line=_line_number(text, match.start()),
                    expression=expression.strip(),
                ))
    return sorted(set(uses), key=lambda use: dataclasses.astuple(use))


def _evidence(path: str, line: int, operation: str, file_hashes: Mapping[str, str]) -> dict[str, Any]:
    return {
        "path": path,
        "line": line,
        "operation": operation,
        "file_sha256": file_hashes.get(path, ""),
    }


def _semantic_fingerprint(semantic: Mapping[str, Any]) -> str:
    return sha256_json(semantic)


def extract_graph(
    source_root: Path,
    identity_index: V1IdentityIndex,
    file_hashes: Mapping[str, str],
) -> GraphResult:
    warnings: list[dict[str, Any]] = []
    packages = _load_packages(source_root, warnings)
    nodes = _discover_nodes(source_root, packages, warnings)
    uses = _extract_endpoint_uses(source_root, nodes, identity_index, warnings)

    entities: dict[str, dict[str, Any]] = {}
    relations: dict[str, dict[str, Any]] = {}

    def add_relation(source: str, predicate: str, target: str, qualifiers: Mapping[str, Any] | None = None) -> None:
        row = {
            "from_entity_uid": source,
            "predicate": predicate,
            "to_entity_uid": target,
            "qualifiers": dict(qualifiers or {}),
        }
        relations[canonical_json(row)] = row

    def add_entity(
        uid: str,
        entity_type: str,
        title: str,
        path: str,
        status: str,
        semantic: dict[str, Any],
        evidence: Sequence[Mapping[str, Any]],
        **extra: Any,
    ) -> None:
        baseline = identity_index.entity_by_uid.get(uid)
        baseline_semantic = (baseline or {}).get("semantic") or {}
        if baseline is not None and "vehicles" in baseline_semantic:
            semantic["vehicles"] = list(baseline_semantic.get("vehicles") or [])
        normalized_evidence = sorted((dict(row) for row in evidence), key=canonical_json)
        entities[uid] = {
            "entity_uid": uid,
            "type": entity_type,
            "comparison_scope": "code",
            "path": path,
            "title": title,
            "status": status,
            "review": "generated",
            "semantic": semantic,
            "source_scope": "vehicle-3-latest-current-filesystem",
            "semantic_fingerprint": _semantic_fingerprint(semantic),
            "evidence_fingerprint": sha256_json(normalized_evidence),
            "evidence": normalized_evidence,
            **extra,
        }

    package_by_name = {package.name: package for package in packages}
    for package in packages:
        uid = identity_index.package_uid(package.name)
        package_xml = f"{package.relative_dir}/package.xml"
        semantic = {
            "type": "ros_package",
            "status": package.status,
            "ros_name": "",
            "executable": "",
            "interface_kind": "",
            "message_type": "",
            "version": package.version,
            "vehicles": ["三号车"],
        }
        add_entity(
            uid, "ros_package", package.name, package_xml, package.status, semantic,
            [_evidence(package_xml, 1, "package_manifest", file_hashes)],
            external_dependencies=[dep for dep in package.dependencies if dep not in package_by_name],
        )
    for package in packages:
        source_uid = identity_index.package_uid(package.name)
        for dependency in package.dependencies:
            if dependency in package_by_name:
                add_relation(source_uid, "depends_on", identity_index.package_uid(dependency))

    node_by_uid: dict[str, NodeInfo] = {}
    executable_counts = Counter(_executable_key(node.executable) for node in nodes)
    for node in nodes:
        uid = identity_index.node_uid(
            node.executable,
            node.ros_name,
            node.identity_name,
            node.package.name,
            executable_counts[_executable_key(node.executable)] == 1,
        )
        node_by_uid[uid] = node
        primary_path = node.source_paths[0] if node.source_paths else f"{node.package.relative_dir}/package.xml"
        node_evidence = [_evidence(path, 1, "node_source", file_hashes) for path in node.source_paths]
        semantic = {
            "type": "ros_node",
            "status": node.status,
            "ros_name": node.ros_name,
            "executable": node.executable,
            "interface_kind": "",
            "message_type": "",
            "version": "",
            "vehicles": ["三号车"],
        }
        add_entity(
            uid, "ros_node", node.identity_name, primary_path, node.status, semantic,
            node_evidence,
            package_uid=identity_index.package_uid(node.package.name),
            launch_names=sorted(set(node.launch_names)),
        )
        add_relation(uid, "package", identity_index.package_uid(node.package.name))

    interface_uses: dict[tuple[str, str], list[EndpointUse]] = defaultdict(list)
    for use in uses:
        interface_uses[(use.interface_kind, use.ros_name)].append(use)
    for (kind, ros_name), endpoint_uses in sorted(interface_uses.items()):
        uid = identity_index.interface_uid(ros_name, kind)
        message_types = sorted({use.message_type for use in endpoint_uses if use.message_type})
        status_candidates = [node_by_uid[use.node_uid].status for use in endpoint_uses if use.node_uid in node_by_uid]
        if "diagnostic" in status_candidates or "probe" in ros_name:
            status = "diagnostic"
        elif "active" in status_candidates:
            status = "active"
        elif "compatibility" in status_candidates or "archived" in status_candidates:
            status = "compatibility"
        else:
            status = "available"
        semantic = {
            "type": "ros_interface",
            "status": status,
            "ros_name": ros_name,
            "executable": "",
            "interface_kind": kind,
            "message_type": "; ".join(message_types) or "unknown",
            "version": "",
            "vehicles": ["三号车"],
        }
        evidence_rows = [
            _evidence(use.path, use.line, use.predicate, file_hashes) for use in endpoint_uses
        ]
        add_entity(
            uid, "ros_interface", ros_name, endpoint_uses[0].path, status, semantic,
            evidence_rows,
        )
        for use in endpoint_uses:
            add_relation(use.node_uid, use.predicate, uid)
            add_relation(uid, "related_packages", use.package_uid)

    for package in packages:
        package_uid = identity_index.package_uid(package.name)
        for kind, folder, suffix in (
            ("message_type", "msg", ".msg"),
            ("service_type", "srv", ".srv"),
        ):
            directory = package.absolute_dir / folder
            if not directory.exists():
                continue
            for definition in sorted(directory.glob(f"*{suffix}"), key=lambda p: p.name):
                relative = _relative(definition, source_root)
                type_name = definition.stem
                uid = identity_index.type_uid(package.name, type_name, kind)
                semantic = {
                    "type": "ros_interface",
                    "status": package.status,
                    "ros_name": f"{package.name}/{type_name}",
                    "executable": "",
                    "interface_kind": kind,
                    "message_type": f"{package.name}/{type_name}",
                    "version": package.version,
                    "vehicles": ["三号车"],
                }
                add_entity(
                    uid, "ros_interface", f"{package.name}/{type_name}", relative,
                    package.status, semantic,
                    [_evidence(relative, 1, "interface_definition", file_hashes)],
                )
                add_relation(package_uid, "defines", uid)

    relation_rows = sorted(relations.values(), key=canonical_json)
    relations_by_entity: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for relation in relation_rows:
        relations_by_entity[relation["from_entity_uid"]].append(relation)
        relations_by_entity[relation["to_entity_uid"]].append(relation)
    for uid, entity in entities.items():
        entity["relation_fingerprint"] = sha256_json(sorted(relations_by_entity[uid], key=canonical_json))
    return GraphResult(
        entities=sorted(entities.values(), key=lambda row: row["entity_uid"]),
        relations=relation_rows,
        warnings=sorted(warnings, key=canonical_json),
    )


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def _jsonl_bytes(rows: Sequence[Mapping[str, Any]]) -> bytes:
    return "".join(canonical_json(dict(row)) + "\n" for row in rows).encode("utf-8")


def _write_jsonl(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.write_bytes(_jsonl_bytes(rows))


def _write_json(path: Path, value: Mapping[str, Any]) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def _documented_migrations(
    baseline_entities: Sequence[Mapping[str, Any]],
    target_entities: Sequence[Mapping[str, Any]],
    baseline_snapshot: str,
    target_snapshot: str,
    file_hashes: Mapping[str, str],
    v1_root: Path | None = None,
) -> list[dict[str, Any]]:
    baseline_by_uid = {str(row["entity_uid"]): row for row in baseline_entities}
    baseline_uids = set(baseline_by_uid)
    target_uids = {str(row["entity_uid"]) for row in target_entities}
    target_entities_sha256 = sha256_bytes(_jsonl_bytes(target_entities))
    target_entity_set_sha256 = sha256_json(sorted(target_uids))
    mappings = [
        (
            "agv:ros:node:trajectory_tracker",
            "decomposed_into",
            [
                "agv:ros:node:vehicle_state_estimator_node",
                "agv:ros:node:trajectory_follower_node",
                "agv:ros:node:left_wall_node",
                "agv:ros:node:mag_guidance_node",
                "agv:ros:node:tight_turn_node",
                "agv:ros:node:motion_arbiter_node",
                "agv:ros:node:safety_supervisor_node",
                "agv:ros:node:chassis_gateway_node",
            ],
            "AGV_MIGRATION_MAP rows 12-18",
            "docs/AGV_MIGRATION_MAP.md",
        ),
        (
            "agv:ros:node:remote_controller",
            "parallel_replacement",
            ["agv:ros:node:teleop_node"],
            "AGV_ALGORITHM_PARITY remote intent row",
            "docs/AGV_ALGORITHM_PARITY.md",
        ),
        (
            "agv:ros:node:magnetic_follower",
            "parallel_replacement",
            ["agv:ros:node:mag_guidance_node"],
            "AGV_MIGRATION_MAP magnetic guidance row",
            "docs/AGV_MIGRATION_MAP.md",
        ),
        (
            "agv:ros:node:ultrasonic_follower",
            "decomposed_into",
            ["agv:ros:node:left_wall_node", "agv:ros:node:safety_supervisor_node"],
            "AGV_MIGRATION_MAP wall-follow and safety rows",
            "docs/AGV_MIGRATION_MAP.md",
        ),
        (
            "agv:ros:node:drive_feedback_odom",
            "superseded_by",
            ["agv:ros:node:vehicle_state_estimator_node"],
            "AGV_ODOM_OWNERSHIP unique owner",
            "docs/AGV_ODOM_OWNERSHIP.md",
        ),
        (
            "agv:ros:interface:odom",
            "owner_changed",
            ["agv:ros:interface:odom"],
            "AGV_ODOM_OWNERSHIP unique owner table",
            "docs/AGV_ODOM_OWNERSHIP.md",
        ),
        (
            "agv:ros:interface:chassis-cmd",
            "publisher_changed",
            ["agv:ros:interface:chassis-cmd"],
            "AGV_TOPIC_PORT_MATRIX chassis command publishers",
            "docs/AGV_TOPIC_PORT_MATRIX.md",
        ),
        (
            "agv:ros:package:agv_mqtt_bridge",
            "capability_extracted_to",
            ["agv:ros:package:agv_telemetry", "agv:ros:package:agv_mission"],
            "AGV_MIGRATION_MAP row 26",
            "docs/AGV_MIGRATION_MAP.md",
        ),
        (
            "agv:ros:node:agv_mqtt_bridge",
            "capability_extracted_to",
            ["agv:ros:node:telemetry_node", "agv:ros:node:mission_node"],
            "AGV_MIGRATION_MAP row 26",
            "docs/AGV_MIGRATION_MAP.md",
        ),
    ]
    rows: list[dict[str, Any]] = []
    fallback_path = "docs/AGV_MIGRATION_MAP.md"
    for source_uid, predicate, targets, locator, preferred_path in mappings:
        if source_uid not in baseline_uids:
            continue
        evidence_path = preferred_path if preferred_path in file_hashes else fallback_path
        if evidence_path not in file_hashes:
            continue
        for target_uid in targets:
            if target_uid is not None and target_uid not in target_uids:
                continue
            rows.append({
                "from_snapshot": baseline_snapshot,
                "from_entity_uid": source_uid,
                "predicate": predicate,
                "to_snapshot": target_snapshot if target_uid is not None else None,
                "to_entity_uid": target_uid,
                "confidence": 1.0,
                "match_method": "documented_migration_map",
                "evidence": {
                    "path": evidence_path,
                    "locator": locator,
                    "file_sha256": file_hashes[evidence_path],
                },
            })
    terminal_mappings = [
        (
            "agv:ros:node:gps_nmea_to_fix_json",
            "removed_without_replacement",
            "Exact V1 entity is absent from V2 and no explicit replacement target exists in the audited graph.",
        ),
        (
            "agv:ros:node:encoder_probe",
            "removed_diagnostic",
            "Diagnostic entity is present in V1 and absent from the V2 primary graph.",
        ),
        (
            "agv:ros:node:yz_aim_probe",
            "removed_diagnostic",
            "Diagnostic entity is present in V1 and absent from the V2 primary graph.",
        ),
    ]
    for source_uid, predicate, locator in terminal_mappings:
        if source_uid not in baseline_by_uid or source_uid in target_uids:
            continue
        baseline_entity = baseline_by_uid[source_uid]
        baseline_artifact = _v1_entity_evidence(
            v1_root,
            source_uid,
            "Exact immutable V1 entity row used by the terminal set-difference audit.",
        )
        baseline_artifact["semantic_fingerprint"] = baseline_entity.get("semantic_fingerprint", "")
        rows.append({
            "from_snapshot": baseline_snapshot,
            "from_entity_uid": source_uid,
            "predicate": predicate,
            "to_snapshot": None,
            "to_entity_uid": None,
            "confidence": 0.9,
            "match_method": "explicit_snapshot_set_difference",
            "evidence": {
                "locator": locator,
                "baseline_artifact": baseline_artifact,
                "target_artifact": {
                    "path": "entities.jsonl",
                    "file_sha256": target_entities_sha256,
                    "entity_set_sha256": target_entity_set_sha256,
                    "absence_entity_uid": source_uid,
                    "expected_count": 0,
                },
            },
        })
    return rows


def build_migration_relations(
    baseline_entities: Sequence[Mapping[str, Any]],
    target_entities: Sequence[Mapping[str, Any]],
    baseline_snapshot: str,
    target_snapshot: str,
    file_hashes: Mapping[str, str],
    v1_root: Path | None = None,
) -> list[dict[str, Any]]:
    rows = build_group_decompositions(
        baseline_entities, target_entities, baseline_snapshot, target_snapshot
    )
    rows.extend(_documented_migrations(
        baseline_entities,
        target_entities,
        baseline_snapshot,
        target_snapshot,
        file_hashes,
        v1_root,
    ))
    return sorted({canonical_json(row): row for row in rows}.values(), key=canonical_json)


def _static_evidence(
    source_root: Path,
    file_hashes: Mapping[str, str],
    path: str,
    needle: str,
    locator: str,
) -> dict[str, Any]:
    line = 0
    full_path = source_root / PurePosixPath(path)
    if full_path.exists() and full_path.is_file():
        for index, text in enumerate(_read_text(full_path).splitlines(), start=1):
            if needle in text:
                line = index
                break
    return {
        "scope": "source",
        "path": path,
        "line": line,
        "locator": locator,
        "file_sha256": file_hashes.get(path, ""),
    }


def _static_absence_evidence(
    source_root: Path,
    file_hashes: Mapping[str, str],
    path: str,
    needle: str,
    locator: str,
) -> dict[str, Any]:
    full_path = source_root / PurePosixPath(path)
    content = _read_text(full_path) if full_path.is_file() else ""
    return {
        "scope": "source_absence",
        "path": path,
        "line": 0,
        "locator": locator,
        "needle": needle,
        "expected_count": 0,
        "actual_count": content.count(needle),
        "file_sha256": file_hashes.get(path, ""),
    }


def _v1_entity_evidence(v1_root: Path | None, entity_uid: str, locator: str) -> dict[str, Any]:
    evidence: dict[str, Any] = {
        "scope": "v1_snapshot",
        "path": "entities.jsonl",
        "line": 0,
        "locator": locator,
        "entity_uid": entity_uid,
        "file_sha256": "",
        "source_page": "",
        "vault_blob_oid": "",
    }
    if v1_root is None or not (v1_root / "entities.jsonl").is_file():
        return evidence
    path = v1_root / "entities.jsonl"
    evidence["file_sha256"] = sha256_bytes(path.read_bytes())
    for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), start=1):
        row = json.loads(line)
        if row.get("entity_uid") == entity_uid:
            evidence["line"] = line_number
            evidence["source_page"] = row.get("path", "")
            evidence["vault_blob_oid"] = row.get("vault_blob_oid", "")
            break
    return evidence


def _v1_relation_evidence(
    v1_root: Path | None,
    from_uid: str,
    predicate: str,
    to_uid: str,
    locator: str,
) -> dict[str, Any]:
    evidence: dict[str, Any] = {
        "scope": "v1_snapshot",
        "path": "relations.jsonl",
        "line": 0,
        "locator": locator,
        "from_entity_uid": from_uid,
        "predicate": predicate,
        "to_entity_uid": to_uid,
        "file_sha256": "",
    }
    if v1_root is None or not (v1_root / "relations.jsonl").is_file():
        return evidence
    path = v1_root / "relations.jsonl"
    evidence["file_sha256"] = sha256_bytes(path.read_bytes())
    for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), start=1):
        row = json.loads(line)
        if (
            row.get("from_entity_uid") == from_uid
            and row.get("predicate") == predicate
            and row.get("to_entity_uid") == to_uid
        ):
            evidence["line"] = line_number
            break
    return evidence


def _git_head_evidence(source_root: Path, path: str, needle: str, locator: str) -> dict[str, Any]:
    code, content = _run_git(source_root, "show", f"HEAD:{path}")
    line = 0
    if code == 0:
        decoded = content.decode("utf-8", errors="replace")
        for line_number, text in enumerate(decoded.splitlines(), start=1):
            if needle in text:
                line = line_number
                break
    return {
        "scope": "git_head",
        "path": path,
        "line": line,
        "locator": locator,
        "file_sha256": sha256_bytes(content) if code == 0 else "",
    }


def _baseline_source_evidence(
    baseline_source_root: Path | None,
    path: str,
    needle: str,
    locator: str,
) -> dict[str, Any]:
    line = 0
    digest = ""
    if baseline_source_root is not None:
        full_path = baseline_source_root / PurePosixPath(path)
        if full_path.is_file():
            digest = sha256_bytes(full_path.read_bytes())
            for line_number, text in enumerate(_read_text(full_path).splitlines(), start=1):
                if needle in text:
                    line = line_number
                    break
    return {
        "scope": "baseline_source_worktree",
        "path": path,
        "line": line,
        "locator": locator,
        "file_sha256": digest,
        "integrity_limitation": "Contextual current-machine hash; immutable V1 retained only an aggregate source-set hash, not a per-file manifest.",
    }


def _migration_evidence(
    migrations: Sequence[Mapping[str, Any]],
    from_uid: str,
    predicate: str,
    locator: str,
) -> dict[str, Any]:
    row = next(
        (
            dict(candidate) for candidate in migrations
            if candidate.get("from_entity_uid") == from_uid
            and candidate.get("predicate") == predicate
        ),
        {},
    )
    return {
        "scope": "graph_comparison",
        "path": "migration-relations.jsonl",
        "line": 0,
        "locator": locator,
        "from_entity_uid": from_uid,
        "predicate": predicate,
        "relation_sha256": sha256_json(row) if row else "",
    }


def build_risk_register(
    source_root: Path,
    git_state: Mapping[str, Any],
    file_hashes: Mapping[str, str] | None = None,
    v1_root: Path | None = None,
    migration_relations: Sequence[Mapping[str, Any]] = (),
    baseline_source_root: Path | None = None,
) -> list[dict[str, Any]]:
    hashes = file_hashes or {}
    modified_count = int((git_state.get("status_counts") or {}).get(" M", 0))
    untracked_count = int((git_state.get("status_counts") or {}).get("??", 0))
    templates = [
        ("R01", "release_risk", "critical", f"V2 含 {modified_count} 个 modified 与 {untracked_count} 个 untracked 文件，Git HEAD 不能单独还原当前快照。", [
            {"scope": "git_state", "path": ".git", "line": 0, "locator": "git status --porcelain and git HEAD", "git_status_sha256": git_state.get("status_sha256", "")},
        ]),
        ("R02", "breaking", "high", "trajectory_tracker 的 control_output_mode 默认值由 V1 的 chassis_cmd 改为 V2 的 legacy；V2 默认会禁用 /chassis/cmd 发布。", [
            _baseline_source_evidence(baseline_source_root, "src/trajectory_recorder/src/trajectory_tracker.cpp", 'std::string("chassis_cmd")', "V1 tracker control_output_mode default"),
            _baseline_source_evidence(baseline_source_root, "src/trajectory_recorder/launch/integrated.launch", 'value="chassis_cmd"', "V1 integrated launch control_output_mode"),
            _static_evidence(source_root, hashes, "src/trajectory_recorder/config/vehicle.yaml", 'control_output_mode: "legacy"', "control_output_mode default"),
            _static_evidence(source_root, hashes, "src/trajectory_recorder/launch/tracker.launch", 'default="legacy"', "tracker launch default"),
            _v1_relation_evidence(v1_root, "agv:ros:node:trajectory_tracker", "publishes", "agv:ros:interface:chassis-cmd", "V1 trajectory_tracker publishes /chassis/cmd"),
        ]),
        ("R03", "breaking", "high", "remote_controller 在 V1 默认发布 /chassis/cmd 并支持 remote_joy 云端输入；V2 改为直接发布 /motor_speed 与 /motor_brake，且云端输入路径已删除。", [
            _baseline_source_evidence(baseline_source_root, "src/remote_ctrl/src/remote_controller.cpp", 'output_mode_("chassis_cmd")', "V1 remote controller chassis_cmd default"),
            _baseline_source_evidence(baseline_source_root, "src/remote_ctrl/src/remote_controller.cpp", 'cloud_joy_topic_("remote_joy")', "V1 cloud joystick topic"),
            _baseline_source_evidence(baseline_source_root, "src/remote_ctrl/src/remote_controller.cpp", "cloudJoyCallback", "V1 cloud joystick callback/subscription"),
            _static_evidence(source_root, hashes, "src/remote_ctrl/src/remote_controller.cpp", 'advertise<std_msgs::Float32>("/motor_speed"', "direct motor speed publisher"),
            _static_evidence(source_root, hashes, "src/remote_ctrl/src/remote_controller.cpp", 'advertise<std_msgs::UInt8>("/motor_brake"', "direct motor brake publisher"),
            _static_absence_evidence(source_root, hashes, "src/remote_ctrl/src/remote_controller.cpp", "cloud_joy_topic_", "V2 cloud joystick path absence"),
            _v1_relation_evidence(v1_root, "agv:ros:node:remote_controller", "publishes", "agv:ros:interface:chassis-cmd", "V1 remote_controller publishes /chassis/cmd"),
        ]),
        ("R04", "breaking", "high", "V1 chassis_bridge 的 OID 重连、通信丢失后运动抑制与 HuakongAoBackend 实现，在 V2 当前文件中均不再存在；Huakong 后端被明确标记为已移除。", [
            _baseline_source_evidence(baseline_source_root, "src/chassis_controller/src/chassis_bridge.cpp", "reconnectLocked", "V1 OID reconnect implementation"),
            _baseline_source_evidence(baseline_source_root, "src/chassis_controller/src/chassis_bridge.cpp", "comm_lost_after_failures", "V1 communication-loss handling"),
            _baseline_source_evidence(baseline_source_root, "src/chassis_controller/src/chassis_bridge.cpp", "enterMotionInhibit", "V1 post-reconnect motion inhibition"),
            _baseline_source_evidence(baseline_source_root, "src/chassis_controller/src/chassis_bridge.cpp", "class HuakongAoBackend", "V1 Huakong analog backend"),
            _git_head_evidence(source_root, "src/chassis_controller/src/chassis_bridge.cpp", "class HuakongAoBackend", "Git HEAD contains HuakongAoBackend"),
            _static_evidence(source_root, hashes, "src/chassis_controller/src/chassis_bridge.cpp", "已废弃并移除", "current worktree removal marker"),
            _static_absence_evidence(source_root, hashes, "src/chassis_controller/src/chassis_bridge.cpp", "reconnectLocked", "V2 OID reconnect implementation absence"),
            _static_absence_evidence(source_root, hashes, "src/chassis_controller/src/chassis_bridge.cpp", "comm_lost_after_failures", "V2 communication-loss handling absence"),
            _static_absence_evidence(source_root, hashes, "src/chassis_controller/src/chassis_bridge.cpp", "enterMotionInhibit", "V2 motion-inhibit implementation absence"),
        ]),
        ("R05", "breaking", "high", "/odom 唯一所有者改为 vehicle_state_estimator_node；与旧发布者并跑会发生多发布者冲突。", [
            _static_evidence(source_root, hashes, "docs/AGV_ODOM_OWNERSHIP.md", "唯一所有者", "unique /odom owner table"),
        ]),
        ("R06", "breaking", "high", "GPS NMEA 节点、launch、/gps/fix_json 与 MQTT GPS 遥测链在 V2 中删除且无替代。", [
            _v1_entity_evidence(v1_root, "agv:ros:node:gps_nmea_to_fix_json", "V1 GPS converter node and source-page provenance"),
            _v1_entity_evidence(v1_root, "agv:ros:interface:gps-fix-json", "V1 /gps/fix_json interface and source-page provenance"),
            _baseline_source_evidence(baseline_source_root, "src/agv_mqtt_bridge/scripts/gps_nmea_to_fix_json.py", '"/gps/fix_json"', "V1 GPS converter publishes configurable /gps/fix_json"),
            _baseline_source_evidence(baseline_source_root, "src/agv_mqtt_bridge/launch/gps_nmea.launch", 'type="gps_nmea_to_fix_json.py"', "V1 GPS launch starts converter"),
            _baseline_source_evidence(baseline_source_root, "src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py", 'self._param_topic("gps_fix_json", "/gps/fix_json")', "V1 MQTT bridge subscribes GPS JSON"),
            _migration_evidence(migration_relations, "agv:ros:node:gps_nmea_to_fix_json", "removed_without_replacement", "explicit V1-present/V2-absent graph audit"),
        ]),
        ("R07", "breaking", "high", "drive_feedback_odom 链删除，录制与跟踪里程转为 FT-EPC 累计脉冲；encoder_ppr 未配置时无有效里程。", [
            _v1_entity_evidence(v1_root, "agv:ros:node:drive_feedback_odom", "V1 drive_feedback_odom entity and source-page provenance"),
            _static_evidence(source_root, hashes, "src/trajectory_recorder/config/vehicle.yaml", "encoder_ppr: 0", "FT-EPC pulses per revolution default"),
        ]),
        ("R08", "integration_gap", "high", "vehicle.launch 不启动传感器驱动或真实底盘驱动，单独启动不能形成完整实车链。", [
            _static_evidence(source_root, hashes, "src/agv_bringup/launch/vehicle.launch", "底层传感器驱动", "launch header dependency statement"),
        ]),
        ("R09", "integration_gap", "high", "teleop_node 需要 /teleop/cmd 与 /teleop/stop，但生产 launch 没有输入转换生产者。", [
            _static_evidence(source_root, hashes, "src/agv_decision/src/teleop_node.cpp", 'subscribe("/teleop/cmd"', "teleop input subscription"),
            _static_evidence(source_root, hashes, "src/agv_bringup/launch/vehicle.launch", 'type="teleop_node"', "production teleop node without input adapter"),
        ]),
        ("R10", "validation_blocker", "high", "MagFrame.line_position 尚未换算为真实 magnetic_error_m，必须进行实车标定。", [
            _static_evidence(source_root, hashes, "docs/AGV_ALGORITHM_PARITY.md", "magnetic_error_m", "B3 magnetic unit calibration gap"),
            _static_evidence(source_root, hashes, "src/agv_perception/src/perception_aggregator_node.cpp", "setMagnetic(m->line_position", "raw channel index assignment"),
        ]),
        ("R11", "deployment_change", "medium", "V1→V2 的 IMU 与磁传感器默认端口均发生变化，部署映射需复核。", [
            _baseline_source_evidence(baseline_source_root, "src/trajectory_recorder/config/hardware.yaml", 'imu_port: "/dev/ttyUSB_IMU_UNASSIGNED"', "V1 IMU default"),
            _baseline_source_evidence(baseline_source_root, "src/trajectory_recorder/config/hardware.yaml", 'mag_sensor_port: "/dev/serial/by-id/', "V1 magnetic sensor by-id default"),
            _static_evidence(source_root, hashes, "src/trajectory_recorder/config/hardware.yaml", 'mag_sensor_port: "/dev/agv_mag_sensor"', "current magnetic sensor default"),
            _static_evidence(source_root, hashes, "src/trajectory_recorder/config/hardware.yaml", 'imu_port: "/dev/ttyUSB3"', "current IMU default"),
        ]),
        ("R12", "deployment_change", "medium", "旧栈与新栈必须互斥，否则会争抢 /odom、电机话题和串口。", [
            _static_evidence(source_root, hashes, "docs/AGV_HARDWARE_ENABLE_CHECKLIST.md", "旧入口", "preflight mutual-exclusion check"),
        ]),
        ("R13", "scope_contraction", "medium", "encoder_probe 与 yz_aim_probe 删除，硬件探针能力收缩。", [
            _v1_entity_evidence(v1_root, "agv:ros:node:encoder_probe", "V1 encoder_probe diagnostic entity"),
            _v1_entity_evidence(v1_root, "agv:ros:node:yz_aim_probe", "V1 yz_aim_probe diagnostic entity"),
        ]),
        ("R14", "parity_gap", "medium", "磁转向保持/释放、精确磁钉触发、滑移检测及部分高级 EKF 未迁移。", [
            _static_evidence(source_root, hashes, "docs/AGV_ALGORITHM_PARITY.md", "B1", "remaining parity gaps B1/B4/B5 and advanced EKF"),
        ]),
        ("R15", "breaking", "medium", "agv_mqtt_bridge 默认 vehicle_id 从 V1 的 agv_002 改为 V2 的 agv_001。", [
            _baseline_source_evidence(baseline_source_root, "src/agv_mqtt_bridge/config/agv_mqtt_bridge.yaml", 'vehicle_id: "agv_002"', "V1 default vehicle_id"),
            _baseline_source_evidence(baseline_source_root, "src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py", '"agv_002"', "V1 Python fallback vehicle_id"),
            _static_evidence(source_root, hashes, "src/agv_mqtt_bridge/config/agv_mqtt_bridge.yaml", 'vehicle_id: "agv_001"', "current default vehicle_id"),
            _v1_entity_evidence(v1_root, "agv:ros:package:agv_mqtt_bridge", "V1 package graph provenance"),
        ]),
        ("R16", "safe_default_change", "medium", "vehicle.launch 默认 backend=mock 且 hardware_enabled=false，显式启用前车辆不会运动。", [
            _static_evidence(source_root, hashes, "src/agv_bringup/launch/vehicle.launch", 'name="backend" default="mock"', "safe backend default"),
            _static_evidence(source_root, hashes, "src/agv_bringup/launch/vehicle.launch", 'name="hardware_enabled" default="false"', "hardware disabled default"),
        ]),
    ]
    return [
        {
            "risk_id": risk_id,
            "risk_kind": risk_kind,
            "severity": severity,
            "statement": statement,
            "breaking": risk_kind == "breaking",
            "validation_state": "static_evidence_only",
            "independent_tests_run": False,
            "review": "needs-review",
            "evidence": evidence,
        }
        for risk_id, risk_kind, severity, statement, evidence in templates
    ]


def _changed_semantic_fields(before: Mapping[str, Any], after: Mapping[str, Any]) -> list[str]:
    before_semantic = before.get("semantic") or {}
    after_semantic = after.get("semantic") or {}
    return sorted({
        key for key in set(before_semantic) | set(after_semantic)
        if before_semantic.get(key) != after_semantic.get(key)
    })


def build_diff_payload(
    baseline_entities: Sequence[Mapping[str, Any]],
    target_entities: Sequence[Mapping[str, Any]],
    baseline_relations: Sequence[Mapping[str, Any]],
    target_relations: Sequence[Mapping[str, Any]],
    migration_relations: Sequence[Mapping[str, Any]],
    baseline_snapshot: str,
    target_snapshot: str,
    baseline_has_file_manifest: bool,
    risks: Sequence[Mapping[str, Any]] = (),
    baseline_extractor_version: str = "",
    target_extractor_version: str = EXTRACTOR_VERSION,
) -> dict[str, Any]:
    summary = diff_entities(baseline_entities, target_entities)
    baseline_by_uid = {str(row["entity_uid"]): row for row in baseline_entities}
    target_by_uid = {str(row["entity_uid"]): row for row in target_entities}
    migrated_from = defaultdict(list)
    for row in migration_relations:
        migrated_from[str(row["from_entity_uid"])].append({
            "predicate": row["predicate"],
            "to_entity_uid": row["to_entity_uid"],
        })
    changes: list[dict[str, Any]] = []
    for uid in summary["added"]:
        changes.append({
            "entity_uid": uid,
            "change_kind": "added",
            "before_fingerprint": "",
            "after_fingerprint": target_by_uid[uid].get("semantic_fingerprint", ""),
            "changed_fields": [],
            "breaking": False,
            "match_method": "target_only",
            "match_confidence": 1.0,
            "review": "generated",
        })
    for uid in summary["removed"]:
        migrations = sorted(migrated_from.get(uid, []), key=canonical_json)
        predicates = {row["predicate"] for row in migrations}
        if "removed_without_replacement" in predicates:
            change_kind = "removed_without_replacement"
            breaking = True
            review = "needs-review"
        elif migrations and predicates == {"removed_diagnostic"}:
            change_kind = "removed_diagnostic"
            breaking = True
            review = "needs-review"
        elif migrations:
            change_kind = "removed_with_migration"
            breaking = False
            review = "generated"
        else:
            change_kind = "removed_needs_review"
            breaking = True
            review = "needs-review"
        changes.append({
            "entity_uid": uid,
            "change_kind": change_kind,
            "before_fingerprint": baseline_by_uid[uid].get("semantic_fingerprint", ""),
            "after_fingerprint": "",
            "changed_fields": [],
            "breaking": breaking,
            "match_method": "baseline_only",
            "match_confidence": 1.0,
            "review": review,
            "migration_targets": migrations,
        })
    for uid in summary["modified"]:
        changes.append({
            "entity_uid": uid,
            "change_kind": "modified",
            "before_fingerprint": baseline_by_uid[uid].get("semantic_fingerprint", ""),
            "after_fingerprint": target_by_uid[uid].get("semantic_fingerprint", ""),
            "changed_fields": _changed_semantic_fields(baseline_by_uid[uid], target_by_uid[uid]),
            "breaking": False,
            "match_method": "exact_entity_uid",
            "match_confidence": 1.0,
            "review": "generated",
        })

    baseline_relation_map = {canonical_json(dict(row)): dict(row) for row in baseline_relations}
    target_relation_map = {canonical_json(dict(row)): dict(row) for row in target_relations}
    relation_added = [target_relation_map[key] for key in sorted(target_relation_map.keys() - baseline_relation_map.keys())]
    relation_removed_raw = [baseline_relation_map[key] for key in sorted(baseline_relation_map.keys() - target_relation_map.keys())]
    relation_removed = [
        {
            **row,
            "comparison_classification": "extraction_limited",
            "breaking": False,
            "review": "needs-review",
        }
        for row in relation_removed_raw
    ]
    relation_matched = len(baseline_relation_map.keys() & target_relation_map.keys())
    assert len(baseline_relation_map) == relation_matched + len(relation_removed_raw)
    assert len(target_relation_map) == relation_matched + len(relation_added)
    scope_changes = classify_scope_changes(
        baseline_entities,
        target_entities,
        baseline_has_file_manifest=baseline_has_file_manifest,
    )
    predicate_counts = Counter(str(row["predicate"]) for row in migration_relations)
    if predicate_counts:
        scope_changes.append({
            "change_kind": "documented_architecture_migration",
            "classification": "scope_change",
            "relation_counts": dict(sorted(predicate_counts.items())),
        })
    return {
        "baseline_snapshot": baseline_snapshot,
        "target_snapshot": target_snapshot,
        "comparison_scope": {
            "baseline_filter": "comparison_scope=code and type in ros_package,ros_node,ros_interface",
            "target_filter": "all generated entities",
            "baseline_source_file_manifest_available": baseline_has_file_manifest,
            "relation_removal_policy": "V1-only relations are extraction_limited and are not definitive breaking removals.",
            "baseline_extractor_version": baseline_extractor_version,
            "target_extractor_version": target_extractor_version,
            "entity_unchanged_meaning": "unchanged_graph_semantics_only",
            "source_code_unchanged_supported": False,
            "relation_delta_meaning": "semantic graph delta mixed with extractor coverage/schema drift; needs review",
        },
        "comparison_limitations": [
            ENTITY_COMPARISON_LIMITATION,
            {
                "limitation_id": "cross-extractor-relation-drift",
                "detail": f"V1 relations use {baseline_extractor_version or 'unknown'} while V2 uses {target_extractor_version}; relation deltas can reflect extractor coverage/schema drift as well as architecture changes.",
            },
        ],
        "entity_counts": summary["counts"],
        "entity_changes": sorted(changes, key=lambda row: row["entity_uid"]),
        "relation_counts": {
            "baseline": len(baseline_relation_map),
            "target": len(target_relation_map),
            "matched": relation_matched,
            "added": len(relation_added),
            "removed": len(relation_removed),
            "removed_extraction_limited": len(relation_removed),
        },
        "relation_added": relation_added,
        "relation_removed": relation_removed,
        "scope_changes": scope_changes,
        "migration_relation_count": len(migration_relations),
        "risk_count": len(risks),
        "risk_counts": {
            "by_kind": dict(sorted(Counter(str(row["risk_kind"]) for row in risks).items())),
            "by_severity": dict(sorted(Counter(str(row["severity"]) for row in risks).items())),
        },
        "risks": [dict(row) for row in risks],
    }


def _diff_markdown(diff: Mapping[str, Any], manifest_seed: Mapping[str, Any]) -> str:
    counts = diff["entity_counts"]
    relation_counts = diff["relation_counts"]
    package_scope = next(
        (row for row in diff["scope_changes"] if row["change_kind"] == "expanded_package_scope"),
        {"entity_uids": []},
    )
    packages = "、".join(uid.rsplit(":", 1)[-1] for uid in package_scope.get("entity_uids", [])) or "无"
    risk_rows = "\n".join(
        f"| {row['risk_id']} | {row['severity']} | {row['risk_kind']} | {row['statement']} |"
        for row in diff.get("risks", [])
    )
    return f"""# V1 → V2 代码图谱差异摘要

- 基线：`{diff['baseline_snapshot']}`
- 目标：`{diff['target_snapshot']}`
- 源码 Git HEAD：`{manifest_seed['git_state'].get('head') or '非 Git 仓库'}`
- 工作区脏状态：`{manifest_seed['git_state'].get('dirty')}`

## 实体守恒

| 项目 | 数量 |
| --- | ---: |
| V1 代码实体 | {counts['baseline']} |
| V2 代码实体 | {counts['target']} |
| 稳定 ID 匹配 | {counts['matched']} |
| 未变化 | {counts['unchanged']} |
| 语义变化 | {counts['modified']} |
| 新增 | {counts['added']} |
| V1 独有 | {counts['removed']} |

数量校验：`V1 = matched + removed`，`V2 = matched + added`，已由生成器验证。

> `unchanged` 仅表示图谱身份与声明的 ROS 语义字段未变，**不等于源代码或配置未变**。V1 没有逐文件清单，内部实现变化只能由单独静态风险证据补充。本报告是图谱级代码实体差异，不是完整源代码 diff。

## 关系差异

- V1 关系：{relation_counts['baseline']}
- V2 关系：{relation_counts['target']}
- 新增关系：{relation_counts['added']}
- V1 独有关系：{relation_counts['removed']}
- 其中解析受限候选：{relation_counts['removed_extraction_limited']}（不作为确定性破坏删除）
- 显式迁移关系：{diff['migration_relation_count']}

## 扫描范围变化

- 新增包范围：{packages}
- V1 没有逐文件清单，因此不能从文件级差异直接断言删除；此限制已单列为 `scope_change`。
- 分解与替代不覆盖 V1 实体，详见 `migration-relations.jsonl`。

## 静态风险审计（R01–R16）

> 以下 16 条来自静态代码、配置、launch、V1 图谱与 Git 工作区证据；本次未独立运行 ROS 单元测试、集成测试或实车测试。

| ID | 级别 | 类型 | 风险 |
| --- | --- | --- | --- |
{risk_rows}

## 提取与发布限制

- launch 解析不展开 `include`、`arg/替换表达式`、`if/unless` 或 `remap`。
- 端点解析仍是静态语法扫描；宏、运行时拼接名称和动态循环可能缺失。
- V1 独有关系统一标为 `extraction_limited`，不是已确认的运行时删除。
- 快照包含源目录定位与相对证据路径；仅用于私有仓库，公开前必须脱敏。
"""


def generate_snapshot(
    source_root: Path,
    v1_root: Path,
    output_root: Path,
    *,
    created: str,
    baseline_source_root: Path | None = None,
) -> dict[str, Any]:
    source_root = source_root.resolve()
    v1_root = v1_root.resolve()
    output_root = output_root.resolve()
    baseline_source_root = baseline_source_root.resolve() if baseline_source_root is not None else None
    validate_non_overlapping_roots(source_root, v1_root, output_root, baseline_source_root)
    risk_evidence_required = (source_root / "src/trajectory_recorder/config/vehicle.yaml").is_file()
    if risk_evidence_required and baseline_source_root is None:
        raise ValueError("--v1-source is required for strict V1-to-V2 risk evidence validation")
    baseline_source_context = load_baseline_source_context(v1_root, baseline_source_root)
    baseline_tree_before = tree_sha256(v1_root)
    output_root.mkdir(parents=True, exist_ok=True)
    unsafe_entries = sorted(
        path.name for path in output_root.iterdir()
        if is_unsafe_linked_artifact(path)
    )
    if unsafe_entries:
        raise ValueError(f"output contains unsafe linked artifacts: {unsafe_entries}")
    stale_entries = sorted(
        path.name for path in output_root.iterdir()
        if path.name not in OUTPUT_ARTIFACTS or not path.is_file()
    )
    if stale_entries:
        raise ValueError(f"output contains stale/unexpected artifacts: {stale_entries}")
    source_files, file_hashes, source_fingerprint = scan_source_files(source_root)
    git_state = inspect_git_state(source_root)
    baseline_manifest = json.loads((v1_root / "manifest.json").read_text(encoding="utf-8-sig"))
    baseline_all = _load_jsonl(v1_root / "entities.jsonl")
    allowed_types = {"ros_package", "ros_node", "ros_interface"}
    baseline_entities = [
        row for row in baseline_all
        if row.get("comparison_scope") == "code" and row.get("type") in allowed_types
    ]
    baseline_uids = {str(row["entity_uid"]) for row in baseline_entities}
    baseline_relations = [
        row for row in _load_jsonl(v1_root / "relations.jsonl")
        if row.get("from_entity_uid") in baseline_uids and row.get("to_entity_uid") in baseline_uids
    ]
    identity_index = V1IdentityIndex(baseline_entities)
    graph = extract_graph(source_root, identity_index, file_hashes)
    head_short = (git_state.get("head") or "filesystem")[:8]
    dirty_marker = "-wt" if git_state.get("dirty") else ""
    snapshot_id = f"code-v2-{head_short}{dirty_marker}-{source_fingerprint[:12]}"
    for entity in graph.entities:
        entity["source_snapshot"] = source_fingerprint
    migration_relations = build_migration_relations(
        baseline_entities,
        graph.entities,
        str(baseline_manifest["snapshot_id"]),
        snapshot_id,
        file_hashes,
        v1_root,
    )
    risks = build_risk_register(
        source_root,
        git_state,
        file_hashes,
        v1_root,
        migration_relations,
        baseline_source_root,
    )
    diff = build_diff_payload(
        baseline_entities,
        graph.entities,
        baseline_relations,
        graph.relations,
        migration_relations,
        str(baseline_manifest["snapshot_id"]),
        snapshot_id,
        bool(baseline_manifest.get("source_file_manifest_available")),
        risks,
        str(baseline_manifest.get("extractor_version", "")),
        EXTRACTOR_VERSION,
    )
    manifest_seed = {"git_state": git_state}
    summary = _diff_markdown(diff, manifest_seed)

    _write_jsonl(output_root / "source-files.jsonl", source_files)
    _write_jsonl(output_root / "entities.jsonl", graph.entities)
    _write_jsonl(output_root / "relations.jsonl", graph.relations)
    _write_jsonl(output_root / "migration-relations.jsonl", migration_relations)
    _write_jsonl(output_root / "extraction-warnings.jsonl", graph.warnings)
    _write_json(output_root / "v1-to-v2-diff.json", diff)
    (output_root / "V1-to-V2差异摘要.md").write_text(summary, encoding="utf-8", newline="\n")

    artifact_names = [
        "source-files.jsonl", "entities.jsonl", "relations.jsonl",
        "migration-relations.jsonl", "extraction-warnings.jsonl",
        "v1-to-v2-diff.json", "V1-to-V2差异摘要.md",
    ]
    artifact_hashes = {
        name: sha256_bytes((output_root / name).read_bytes()) for name in artifact_names
    }
    type_counts = Counter(str(entity["type"]) for entity in graph.entities)
    interface_kind_counts = Counter(
        str(entity["semantic"]["interface_kind"])
        for entity in graph.entities if entity["type"] == "ros_interface"
    )
    included_count = sum(row["disposition"] == "included" for row in source_files)
    context_count = sum(row["disposition"] == "context" for row in source_files)
    excluded_count = sum(row["disposition"] == "excluded" for row in source_files)
    manifest = {
        "snapshot_id": snapshot_id,
        "graph_version": "v2",
        "immutable": True,
        "created": created,
        "graph_schema_version": SCHEMA_VERSION,
        "extractor_version": EXTRACTOR_VERSION,
        "scope_id": "agv-code-graph-v2-vehicle-3-latest",
        "source_locator": source_root.as_posix(),
        "source_kind": "current_filesystem_git_worktree_snapshot",
        "source_file_manifest_available": True,
        "source_file_count": len(source_files),
        "included_source_file_count": included_count,
        "context_source_file_count": context_count,
        "excluded_source_file_count": excluded_count,
        "source_fingerprint": source_fingerprint,
        "git_state": git_state,
        "baseline_snapshot": str(baseline_manifest["snapshot_id"]),
        "baseline_tree_sha256": baseline_tree_before,
        "baseline_manifest_limitation": baseline_manifest.get("source_manifest_limitation", ""),
        "baseline_source_context": baseline_source_context,
        "baseline_source_context_fingerprint": sha256_json(baseline_source_context),
        "extraction_limitations": EXTRACTION_LIMITATIONS,
        "comparison_limitations": diff["comparison_limitations"],
        "baseline_extractor_version": baseline_manifest.get("extractor_version", ""),
        "entity_count": len(graph.entities),
        "semantic_relation_count": len(graph.relations),
        "migration_relation_count": len(migration_relations),
        "warning_count": len(graph.warnings),
        "risk_count": len(risks),
        "risk_evidence_required": risk_evidence_required,
        "risk_counts": diff["risk_counts"],
        "entity_type_counts": dict(sorted(type_counts.items())),
        "interface_kind_counts": dict(sorted(interface_kind_counts.items())),
        "artifact_sha256": artifact_hashes,
        "snapshot_fingerprint": sha256_json({
            "source_fingerprint": source_fingerprint,
            "git_head": git_state.get("head", ""),
            "git_status_sha256": git_state.get("status_sha256", ""),
            "baseline_source_context_fingerprint": sha256_json(baseline_source_context),
            "artifact_sha256": artifact_hashes,
        }),
    }
    _write_json(output_root / "manifest.json", manifest)
    validate_output(output_root, source_root, v1_root, baseline_source_root)
    baseline_tree_after = tree_sha256(v1_root)
    if baseline_tree_after != baseline_tree_before:
        raise ValueError("V1 snapshot tree changed during generation/validation")
    return manifest


def _validate_risk_evidence(
    risks: Sequence[Mapping[str, Any]],
    manifest: Mapping[str, Any],
    source_root: Path,
    v1_root: Path,
    migrations: Sequence[Mapping[str, Any]],
    baseline_source_root: Path | None = None,
) -> None:
    migration_by_key = {
        (str(row.get("from_entity_uid")), str(row.get("predicate"))): dict(row)
        for row in migrations
    }
    for risk in risks:
        if risk.get("validation_state") != "static_evidence_only":
            raise ValueError(f"risk validation state is not static-only: {risk.get('risk_id')}")
        if risk.get("independent_tests_run") is not False:
            raise ValueError(f"risk incorrectly claims independent tests: {risk.get('risk_id')}")
        evidence_rows = risk.get("evidence") or []
        if not evidence_rows:
            raise ValueError(f"risk has no evidence: {risk.get('risk_id')}")
        for evidence in evidence_rows:
            scope = evidence.get("scope")
            if not evidence.get("path") or not evidence.get("locator"):
                raise ValueError(f"risk evidence lacks path/locator: {risk.get('risk_id')}")
            if scope == "source":
                path = (source_root / PurePosixPath(str(evidence["path"]))).resolve()
                if source_root != path and source_root not in path.parents:
                    raise ValueError(f"risk source evidence escapes source root: {path}")
                if not path.is_file() or sha256_bytes(path.read_bytes()) != evidence.get("file_sha256"):
                    raise ValueError(f"risk source evidence hash mismatch: {risk.get('risk_id')} {path}")
                lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
                line = int(evidence.get("line", 0))
                if line < 1 or line > len(lines):
                    raise ValueError(f"risk source evidence line unresolved: {risk.get('risk_id')} {path}")
            elif scope == "source_absence":
                path = (source_root / PurePosixPath(str(evidence["path"]))).resolve()
                if source_root != path and source_root not in path.parents:
                    raise ValueError(f"risk source-absence evidence escapes source root: {path}")
                if not path.is_file() or sha256_bytes(path.read_bytes()) != evidence.get("file_sha256"):
                    raise ValueError(f"risk source-absence evidence hash mismatch: {risk.get('risk_id')} {path}")
                needle = str(evidence.get("needle", ""))
                expected_count = int(evidence.get("expected_count", -1))
                actual_count = _read_text(path).count(needle) if needle else -1
                if expected_count != 0 or actual_count != 0 or evidence.get("actual_count") != actual_count:
                    raise ValueError(f"risk source-absence assertion failed: {risk.get('risk_id')} {path}")
            elif scope == "v1_snapshot":
                path = (v1_root / PurePosixPath(str(evidence["path"]))).resolve()
                if v1_root != path and v1_root not in path.parents:
                    raise ValueError(f"risk V1 evidence escapes snapshot root: {path}")
                if not path.is_file() or sha256_bytes(path.read_bytes()) != evidence.get("file_sha256"):
                    raise ValueError(f"risk V1 evidence hash mismatch: {risk.get('risk_id')} {path}")
                lines = path.read_text(encoding="utf-8-sig").splitlines()
                line = int(evidence.get("line", 0))
                if line < 1 or line > len(lines):
                    raise ValueError(f"risk V1 evidence line unresolved: {risk.get('risk_id')} {path}")
                row = json.loads(lines[line - 1])
                if evidence.get("entity_uid"):
                    if row.get("entity_uid") != evidence["entity_uid"]:
                        raise ValueError(f"risk V1 entity evidence mismatch: {risk.get('risk_id')}")
                    if row.get("path", "") != evidence.get("source_page", ""):
                        raise ValueError(f"risk V1 source-page evidence mismatch: {risk.get('risk_id')}")
                    if row.get("vault_blob_oid", "") != evidence.get("vault_blob_oid", ""):
                        raise ValueError(f"risk V1 blob evidence mismatch: {risk.get('risk_id')}")
                elif evidence.get("from_entity_uid"):
                    for key in ("from_entity_uid", "predicate", "to_entity_uid"):
                        if row.get(key) != evidence.get(key):
                            raise ValueError(f"risk V1 relation evidence mismatch: {risk.get('risk_id')}")
            elif scope == "baseline_source_worktree":
                if baseline_source_root is None:
                    raise ValueError(f"risk baseline-source evidence has no source root: {risk.get('risk_id')}")
                path = (baseline_source_root / PurePosixPath(str(evidence["path"]))).resolve()
                if baseline_source_root != path and baseline_source_root not in path.parents:
                    raise ValueError(f"risk baseline-source evidence escapes source root: {path}")
                if not evidence.get("integrity_limitation"):
                    raise ValueError(f"risk baseline-source evidence lacks integrity limitation: {risk.get('risk_id')}")
                if not path.is_file() or sha256_bytes(path.read_bytes()) != evidence.get("file_sha256"):
                    raise ValueError(f"risk baseline-source evidence hash mismatch: {risk.get('risk_id')} {path}")
                lines = _read_text(path).splitlines()
                line = int(evidence.get("line", 0))
                if line < 1 or line > len(lines):
                    raise ValueError(f"risk baseline-source evidence line unresolved: {risk.get('risk_id')} {path}")
            elif scope == "git_head":
                code, content = _run_git(source_root, "show", f"HEAD:{evidence['path']}")
                if code != 0 or sha256_bytes(content) != evidence.get("file_sha256"):
                    raise ValueError(f"risk Git HEAD evidence hash mismatch: {risk.get('risk_id')}")
                lines = content.decode("utf-8", errors="replace").splitlines()
                line = int(evidence.get("line", 0))
                if line < 1 or line > len(lines):
                    raise ValueError(f"risk Git HEAD evidence line unresolved: {risk.get('risk_id')}")
            elif scope == "git_state":
                if evidence.get("git_status_sha256") != manifest.get("git_state", {}).get("status_sha256"):
                    raise ValueError(f"risk Git state evidence mismatch: {risk.get('risk_id')}")
            elif scope == "graph_comparison":
                key = (str(evidence.get("from_entity_uid")), str(evidence.get("predicate")))
                row = migration_by_key.get(key)
                if row is None or sha256_json(row) != evidence.get("relation_sha256"):
                    raise ValueError(f"risk graph-comparison evidence mismatch: {risk.get('risk_id')}")
            else:
                raise ValueError(f"unknown risk evidence scope: {risk.get('risk_id')} {scope}")


def validate_output(
    output_root: Path,
    source_root: Path,
    v1_root: Path,
    baseline_source_root: Path | None = None,
) -> None:
    output_root = output_root.resolve()
    source_root = source_root.resolve()
    v1_root = v1_root.resolve()
    baseline_source_root = baseline_source_root.resolve() if baseline_source_root is not None else None
    validate_non_overlapping_roots(source_root, v1_root, output_root, baseline_source_root)
    unsafe_entries = sorted(
        path.name for path in output_root.iterdir()
        if is_unsafe_linked_artifact(path)
    )
    if unsafe_entries:
        raise ValueError(f"output contains unsafe linked artifacts: {unsafe_entries}")
    actual_artifacts = {path.name for path in output_root.iterdir() if path.is_file()}
    unexpected_entries = [path.name for path in output_root.iterdir() if not path.is_file()]
    if actual_artifacts != OUTPUT_ARTIFACTS or unexpected_entries:
        raise ValueError(
            f"output artifact set mismatch: files={sorted(actual_artifacts)}, non_files={sorted(unexpected_entries)}"
        )
    validate_utf8_text_artifacts(output_root)
    manifest = json.loads((output_root / "manifest.json").read_text(encoding="utf-8-sig"))
    baseline_context = manifest.get("baseline_source_context") or {}
    expected_context_fingerprint = manifest.get("baseline_source_context_fingerprint", "")
    if expected_context_fingerprint != sha256_json(baseline_context):
        raise ValueError("baseline source context fingerprint mismatch")
    if baseline_context.get("available"):
        if baseline_source_root is None:
            locator = str(baseline_context.get("source_locator", ""))
            if not locator:
                raise ValueError("baseline source context has no source locator")
            baseline_source_root = Path(locator).resolve()
        validate_non_overlapping_roots(source_root, v1_root, output_root, baseline_source_root)
        recomputed_context = load_baseline_source_context(v1_root, baseline_source_root)
        for key in (
            "available",
            "source_kind",
            "git_state",
            "v1_source_set",
            "git_head_matches_v1_source_set",
            "aggregate_hash_reverified",
            "integrity_limitation",
        ):
            if recomputed_context.get(key) != baseline_context.get(key):
                raise ValueError(f"baseline source context changed: {key}")
    elif manifest.get("risk_evidence_required"):
        raise ValueError("strict risk evidence requires an available baseline source context")
    if manifest.get("baseline_tree_sha256") != tree_sha256(v1_root):
        raise ValueError("V1 snapshot tree hash mismatch")
    entities = _load_jsonl(output_root / "entities.jsonl")
    relations = _load_jsonl(output_root / "relations.jsonl")
    migrations = _load_jsonl(output_root / "migration-relations.jsonl")
    source_files = _load_jsonl(output_root / "source-files.jsonl")
    baseline_entities = _load_jsonl(v1_root / "entities.jsonl")
    baseline_uids = {str(row["entity_uid"]) for row in baseline_entities}
    entity_by_uid = {str(row["entity_uid"]): row for row in entities}
    if len(entity_by_uid) != len(entities):
        raise ValueError("duplicate entity_uid in V2 entities.jsonl")
    target_uids = set(entity_by_uid)
    for relation in relations:
        if relation["from_entity_uid"] not in target_uids or relation["to_entity_uid"] not in target_uids:
            raise ValueError(f"unresolved V2 relation endpoint: {canonical_json(relation)}")
    for migration in migrations:
        if migration["from_entity_uid"] not in baseline_uids:
            raise ValueError(f"unresolved V1 migration endpoint: {canonical_json(migration)}")
        target_uid = migration.get("to_entity_uid")
        if target_uid is None:
            if migration.get("predicate") not in TERMINAL_MIGRATION_PREDICATES:
                raise ValueError(f"non-terminal migration has no V2 endpoint: {canonical_json(migration)}")
            if migration.get("to_snapshot") is not None:
                raise ValueError(f"terminal migration must not name a V2 snapshot: {canonical_json(migration)}")
            evidence = migration.get("evidence") or {}
            baseline_artifact = evidence.get("baseline_artifact") or {}
            target_artifact = evidence.get("target_artifact") or {}
            baseline_path = (v1_root / PurePosixPath(str(baseline_artifact.get("path", "")))).resolve()
            if v1_root != baseline_path and v1_root not in baseline_path.parents:
                raise ValueError(f"terminal migration baseline evidence escapes V1 root: {baseline_path}")
            if not baseline_path.is_file() or sha256_bytes(baseline_path.read_bytes()) != baseline_artifact.get("file_sha256"):
                raise ValueError(f"terminal migration baseline artifact mismatch: {canonical_json(migration)}")
            baseline_lines = baseline_path.read_text(encoding="utf-8-sig").splitlines()
            baseline_line = int(baseline_artifact.get("line", 0))
            if baseline_line < 1 or baseline_line > len(baseline_lines):
                raise ValueError(f"terminal migration baseline row unresolved: {canonical_json(migration)}")
            baseline_row = json.loads(baseline_lines[baseline_line - 1])
            if baseline_row.get("entity_uid") != migration["from_entity_uid"]:
                raise ValueError(f"terminal migration baseline UID mismatch: {canonical_json(migration)}")
            if baseline_row.get("semantic_fingerprint", "") != baseline_artifact.get("semantic_fingerprint", ""):
                raise ValueError(f"terminal migration baseline fingerprint mismatch: {canonical_json(migration)}")
            target_path = (output_root / PurePosixPath(str(target_artifact.get("path", "")))).resolve()
            if output_root != target_path and output_root not in target_path.parents:
                raise ValueError(f"terminal migration target evidence escapes output root: {target_path}")
            if target_path != output_root / "entities.jsonl":
                raise ValueError(f"terminal migration target artifact must be entities.jsonl: {target_path}")
            if not target_path.is_file() or sha256_bytes(target_path.read_bytes()) != target_artifact.get("file_sha256"):
                raise ValueError(f"terminal migration target artifact mismatch: {canonical_json(migration)}")
            absence_uid = str(target_artifact.get("absence_entity_uid", ""))
            actual_count = sum(row.get("entity_uid") == absence_uid for row in entities)
            if (
                absence_uid != migration["from_entity_uid"]
                or int(target_artifact.get("expected_count", -1)) != 0
                or actual_count != 0
                or target_artifact.get("entity_set_sha256") != sha256_json(sorted(target_uids))
            ):
                raise ValueError(f"terminal migration absence assertion failed: {canonical_json(migration)}")
        elif target_uid not in target_uids:
            raise ValueError(f"unresolved V2 migration endpoint: {canonical_json(migration)}")
    relations_by_entity: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for relation in relations:
        relations_by_entity[relation["from_entity_uid"]].append(relation)
        relations_by_entity[relation["to_entity_uid"]].append(relation)
    for uid, entity in entity_by_uid.items():
        if entity["type"] == "ros_node" and not any(
            evidence.get("operation") == "node_source" for evidence in entity["evidence"]
        ):
            raise ValueError(f"ROS node has no node_source evidence: {uid}")
        if entity["semantic_fingerprint"] != sha256_json(entity["semantic"]):
            raise ValueError(f"semantic fingerprint mismatch: {uid}")
        if entity["evidence_fingerprint"] != sha256_json(sorted(entity["evidence"], key=canonical_json)):
            raise ValueError(f"evidence fingerprint mismatch: {uid}")
        expected_relations = sha256_json(sorted(relations_by_entity[uid], key=canonical_json))
        if entity["relation_fingerprint"] != expected_relations:
            raise ValueError(f"relation fingerprint mismatch: {uid}")
    hashed_sources = [
        row for row in source_files if row["disposition"] in {"included", "context"}
    ]
    for row in hashed_sources:
        actual = sha256_bytes((source_root / PurePosixPath(row["path"])).read_bytes())
        if actual != row["sha256"]:
            raise ValueError(f"source file changed during/after scan: {row['path']}")
    if manifest["entity_count"] != len(entities):
        raise ValueError("manifest entity_count mismatch")
    if manifest["semantic_relation_count"] != len(relations):
        raise ValueError("manifest semantic_relation_count mismatch")
    if manifest["migration_relation_count"] != len(migrations):
        raise ValueError("manifest migration_relation_count mismatch")
    for name, expected in manifest["artifact_sha256"].items():
        actual = sha256_bytes((output_root / name).read_bytes())
        if actual != expected:
            raise ValueError(f"artifact hash mismatch: {name}")
    diff = json.loads((output_root / "v1-to-v2-diff.json").read_text(encoding="utf-8-sig"))
    if manifest.get("risk_evidence_required"):
        _validate_risk_evidence(
            diff.get("risks") or [],
            manifest,
            source_root,
            v1_root,
            migrations,
            baseline_source_root,
        )
    counts = diff["entity_counts"]
    if counts["baseline"] != counts["matched"] + counts["removed"]:
        raise ValueError("V1 entity conservation failed")
    if counts["target"] != counts["matched"] + counts["added"]:
        raise ValueError("V2 entity conservation failed")
    if counts["matched"] != counts["unchanged"] + counts["modified"]:
        raise ValueError("matched entity conservation failed")
    relation_counts = diff["relation_counts"]
    if relation_counts["baseline"] != relation_counts["matched"] + relation_counts["removed"]:
        raise ValueError("V1 relation conservation failed")
    if relation_counts["target"] != relation_counts["matched"] + relation_counts["added"]:
        raise ValueError("V2 relation conservation failed")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--v1", type=Path, required=True)
    parser.add_argument(
        "--v1-source",
        type=Path,
        help="Optional V1 source worktree used only for contextual per-file risk evidence.",
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--created",
        required=True,
        help="Snapshot date (YYYY-MM-DD); explicit input keeps output deterministic.",
    )
    args = parser.parse_args(argv)
    manifest = generate_snapshot(
        args.source,
        args.v1,
        args.output,
        created=args.created,
        baseline_source_root=args.v1_source,
    )
    print(canonical_json({
        "snapshot_id": manifest["snapshot_id"],
        "snapshot_fingerprint": manifest["snapshot_fingerprint"],
        "entity_count": manifest["entity_count"],
        "semantic_relation_count": manifest["semantic_relation_count"],
        "migration_relation_count": manifest["migration_relation_count"],
        "warning_count": manifest["warning_count"],
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
