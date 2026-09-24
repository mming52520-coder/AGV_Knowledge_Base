#!/usr/bin/env python3
"""Deterministic, read-only-on-source index for the AGV Obsidian vault."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

SCHEMA_VERSION = 1
TOOL_VERSION = "1.0"
INDEX_FILES = ("manifest.json", "documents.jsonl", "relations.jsonl")
PROTECTED = (
    "00_System/Graph_History/Snapshots/",
    "00_System/Graph_History/Changes/",
    "00_System/Graph_History/Tools/",
)
WIKILINK = re.compile(r"\[\[([^\[\]]+)\]\]")
FIELD = re.compile(r"^([A-Za-z_][A-Za-z_0-9-]*):\s*(.*)$")


class IndexErrorWithContext(ValueError):
    pass


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        return value[1:-1]
    return value


def string_list(value: str) -> list[str]:
    value = value.strip()
    if not value:
        return []
    if not (value.startswith("[") and value.endswith("]")):
        raise IndexErrorWithContext("expected an inline list: " + value)
    return [scalar(item) for item in next(csv.reader([value[1:-1]], skipinitialspace=True)) if item.strip()]


def frontmatter(source: str) -> tuple[dict[str, str | list[str]], str]:
    if not source.startswith("---\n"):
        return {}, source
    close = source.find("\n---\n", 4)
    if close < 0:
        raise IndexErrorWithContext("unclosed frontmatter")
    fields: dict[str, str | list[str]] = {}
    current_list: str | None = None
    for line in source[4:close].splitlines():
        match = FIELD.match(line)
        if match:
            key, raw = match.groups()
            if key in fields:
                raise IndexErrorWithContext("duplicate frontmatter key: " + key)
            fields[key] = string_list(raw) if raw.startswith("[") else scalar(raw)
            current_list = key if not raw else None
        elif current_list and line.startswith("  - "):
            if not isinstance(fields[current_list], list):
                fields[current_list] = []
            assert isinstance(fields[current_list], list)
            fields[current_list].append(scalar(line[4:]))
        else:
            current_list = None
    return fields, source[close + 5:]


def field(fields: dict[str, str | list[str]], key: str) -> str | None:
    value = fields.get(key)
    return value if isinstance(value, str) and value else None


def list_field(fields: dict[str, str | list[str]], key: str) -> list[str]:
    value = fields.get(key)
    return value if isinstance(value, list) else []


def markdown_files(vault: Path) -> list[Path]:
    return sorted(
        path for path in vault.rglob("*.md")
        if not any(part.startswith(".") for part in path.relative_to(vault).parts)
    )


def load_config(config_path: Path) -> dict:
    data = json.loads(config_path.read_text(encoding="utf-8"))
    if data.get("schema_version") != SCHEMA_VERSION:
        raise IndexErrorWithContext("unsupported config schema")
    return data


def read_documents(vault: Path) -> dict[str, dict]:
    documents: dict[str, dict] = {}
    instance_keys: set[tuple[str, str, str]] = set()
    for path in markdown_files(vault):
        relative = path.relative_to(vault).as_posix()
        raw = path.read_bytes()
        fields, body = frontmatter(raw.decode("utf-8"))
        doc_id = field(fields, "id")
        if not doc_id:
            continue
        if doc_id in documents:
            raise IndexErrorWithContext(f"duplicate document id {doc_id}: {documents[doc_id]['path']} and {relative}")
        title_match = re.search(r"^# (.+)$", body, flags=re.MULTILINE)
        title = field(fields, "title") or (title_match.group(1).strip() if title_match else path.stem)
        snapshot = field(fields, "snapshot_id")
        logical_uid = field(fields, "logical_entity_uid")
        instance = field(fields, "snapshot_instance_id")
        if instance:
            if not (snapshot and logical_uid and instance == snapshot + "::" + logical_uid):
                raise IndexErrorWithContext(f"invalid instance key in {relative}")
            key = (field(fields, "project") or "", snapshot, logical_uid)
            if key in instance_keys:
                raise IndexErrorWithContext(f"duplicate scoped instance {key}")
            instance_keys.add(key)
        documents[doc_id] = {
            "id": doc_id,
            "path": relative,
            "title": title,
            "type": field(fields, "type"),
            "entity_type": field(fields, "entity_type"),
            "project": field(fields, "project"),
            "vehicles": list_field(fields, "vehicles"),
            "scope": field(fields, "source_scope"),
            "snapshot": snapshot,
            "logical_entity_uid": logical_uid,
            "instance_key": instance,
            "status": field(fields, "status"),
            "review": field(fields, "review"),
            "source_snapshot": field(fields, "source_snapshot"),
            "aliases": list_field(fields, "aliases"),
            "tags": list_field(fields, "tags"),
            "sha256": digest(raw),
        }
    return documents


def classify(doc: dict, pointer: dict) -> str:
    snapshot = doc["snapshot"]
    if doc["type"] == "graph_change" or "/Changes/" in doc["path"]:
        return "historical"
    if doc["path"].startswith("03_ROS/"):
        return "logical_reference"
    if doc["type"] == "graph_entity_instance" or doc["path"].startswith("00_System/Graph_History/Snapshots/"):
        if snapshot == pointer.get("current_snapshot"):
            return "current_snapshot"
        if snapshot == pointer.get("candidate_snapshot"):
            return "candidate"
        return "historical"
    return "document"


def add_enrichments(vault: Path, docs: dict[str, dict], config: dict) -> None:
    for doc_id, extra in config.get("enrichments", {}).items():
        if doc_id not in docs:
            raise IndexErrorWithContext("missing enriched document: " + doc_id)
        doc = docs[doc_id]
        doc["aliases"] = sorted(set(doc["aliases"] + extra.get("aliases", [])))
        doc["summary"] = extra.get("summary")
        evidence = []
        for item in extra.get("evidence", []):
            relative = item["path"]
            target = vault / relative
            if not target.is_file() or not target.resolve().is_relative_to(vault.resolve()):
                raise IndexErrorWithContext("missing or unsafe evidence: " + relative)
            evidence.append({
                "path": relative,
                "locator": item["locator"],
                "kind": item["kind"],
                "state": item["state"],
                "summary": item["summary"],
                "sha256": digest(target.read_bytes()),
            })
        doc["evidence"] = sorted(evidence, key=lambda item: (item["path"], item["locator"]))
    for doc in docs.values():
        doc.setdefault("summary", None)
        doc.setdefault("evidence", [])


def enrich_snapshot_instances(vault: Path, docs: dict[str, dict]) -> None:
    machines: dict[str, tuple[dict[str, dict], str, str] | None] = {}
    for doc in docs.values():
        if doc["type"] != "graph_entity_instance" or not doc["snapshot"]:
            continue
        snapshot = doc["snapshot"]
        if snapshot not in machines:
            relative = f"00_System/Graph_History/Snapshots/{snapshot}/Machine/entities.jsonl"
            machine_file = vault / relative
            if machine_file.is_file():
                raw = machine_file.read_bytes()
                rows = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
                by_uid = {row["entity_uid"]: row for row in rows}
                if len(by_uid) != len(rows):
                    raise IndexErrorWithContext("duplicate machine entity UID in " + relative)
                machines[snapshot] = (by_uid, relative, digest(raw))
            else:
                machines[snapshot] = None
        machine = machines[snapshot]
        if machine is None:
            continue
        rows, relative, file_hash = machine
        row = rows.get(doc["logical_entity_uid"])
        if row is None:
            raise IndexErrorWithContext("snapshot instance absent from machine data: " + doc["id"])
        doc["project"] = doc["project"] or ("AGV" if "AGV" in doc["tags"] else None)
        doc["scope"] = doc["scope"] or row.get("source_scope")
        doc["vehicles"] = doc["vehicles"] or row.get("semantic", {}).get("vehicles", [])
        doc["evidence"].append({
            "path": relative,
            "locator": "entity_uid=" + doc["logical_entity_uid"],
            "kind": "archived-machine-row",
            "state": "static-candidate",
            "summary": "归档机器条目；原始 ROS 源码不在本知识库内。",
            "sha256": file_hash,
        })


def build_model(vault: Path, config_path: Path) -> dict:
    config = load_config(config_path)
    pointer = json.loads((vault / "00_System/Graph_History/current.json").read_text(encoding="utf-8"))
    docs = read_documents(vault)
    add_enrichments(vault, docs, config)
    enrich_snapshot_instances(vault, docs)
    relations = config.get("relations", [])
    for relation in relations:
        if relation["from"] not in docs or relation["to"] not in docs:
            raise IndexErrorWithContext("dangling relation: " + str(relation))
    for doc in docs.values():
        doc["class"] = classify(doc, pointer)
    return {
        "schema_version": SCHEMA_VERSION,
        "tool_version": TOOL_VERSION,
        "current_snapshot": pointer["current_snapshot"],
        "candidate_snapshot": pointer.get("candidate_snapshot"),
        "documents": sorted(docs.values(), key=lambda item: item["id"]),
        "relations": sorted(relations, key=lambda item: (item["from"], item["relation"], item["to"])),
    }


def index_bytes(model: dict) -> dict[str, bytes]:
    documents = b"".join(canonical(doc) for doc in model["documents"])
    relations = b"".join(canonical(relation) for relation in model["relations"])
    manifest = {
        "schema_version": model["schema_version"],
        "tool_version": model["tool_version"],
        "current_snapshot": model["current_snapshot"],
        "candidate_snapshot": model["candidate_snapshot"],
        "document_count": len(model["documents"]),
        "relation_count": len(model["relations"]),
        "documents_sha256": digest(documents),
        "relations_sha256": digest(relations),
    }
    return {
        "manifest.json": (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8"),
        "documents.jsonl": documents,
        "relations.jsonl": relations,
    }


def write_index(index_dir: Path, model: dict) -> None:
    index_dir.mkdir(parents=True, exist_ok=True)
    for name, data in index_bytes(model).items():
        target = index_dir / name
        temporary = target.with_name(target.name + ".tmp")
        temporary.write_bytes(data)
        os.replace(temporary, target)


def read_index(index_dir: Path) -> dict:
    manifest = json.loads((index_dir / "manifest.json").read_text(encoding="utf-8"))
    documents = [json.loads(line) for line in (index_dir / "documents.jsonl").read_text(encoding="utf-8").splitlines()]
    relations = [json.loads(line) for line in (index_dir / "relations.jsonl").read_text(encoding="utf-8").splitlines()]
    return {
        "schema_version": manifest["schema_version"],
        "tool_version": manifest["tool_version"],
        "current_snapshot": manifest["current_snapshot"],
        "candidate_snapshot": manifest["candidate_snapshot"],
        "documents": documents,
        "relations": relations,
    }


def protected_digest(vault: Path) -> str:
    result = subprocess.check_output(["git", "-C", str(vault), "ls-files", "-z"])
    paths = sorted(path.decode("utf-8") for path in result.split(b"\0") if path)
    selected = [
        path for path in paths
        if path == "00_System/Graph_History/current.json" or path.startswith(PROTECTED)
    ]
    sha = hashlib.sha256()
    for path in selected:
        sha.update(path.encode("utf-8") + b"\0" + digest((vault / path).read_bytes()).encode("ascii") + b"\n")
    return sha.hexdigest()


def verify_protected(vault: Path, config: dict) -> None:
    if protected_digest(vault) != config["protected_tree_sha256"]:
        raise IndexErrorWithContext("immutable graph history or current pointer changed")
    for tag, expected in config.get("protected_tags", {}).items():
        result = subprocess.run(
            ["git", "-C", str(vault), "rev-parse", "--verify", tag + "^{commit}"],
            capture_output=True, text=True, check=False,
        )
        if result.returncode != 0 or result.stdout.strip() != expected:
            raise IndexErrorWithContext("immutable tag changed or missing: " + tag)


def _headings_and_blocks(text: str) -> tuple[set[str], set[str]]:
    headings = set(re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.MULTILINE))
    blocks = set(re.findall(r"\^([A-Za-z0-9-]+)\s*$", text, re.MULTILINE))
    return headings, blocks


def _resolve_link(vault: Path, source: Path, target: str, files: list[Path]) -> tuple[Path | None, str]:
    target = target.split("|", 1)[0].strip()
    anchor = ""
    if "#" in target:
        target, anchor = target.split("#", 1)
    if not target:
        return source, anchor
    suffixes = ("",) if Path(target).suffix else (".md", ".canvas", "")
    candidate_roots = [source.parent / target, vault / target] if target.startswith(".") else [vault / target, source.parent / target]
    for root in candidate_roots:
        for suffix in suffixes:
            candidate = Path(str(root) + suffix).resolve()
            if candidate.is_relative_to(vault.resolve()) and candidate.is_file():
                return candidate, anchor
    if "/" not in target:
        matches = [path for path in files if path.stem == target or path.name == target]
        if len(matches) == 1:
            return matches[0], anchor
        if len(matches) > 1:
            return None, "ambiguous: " + target
    return None, "missing: " + target


def link_failures(vault: Path, paths: list[str]) -> list[str]:
    files = sorted(path.resolve() for path in vault.rglob("*") if path.is_file() and ".git" not in path.parts)
    failures = []
    for relative in paths:
        source = vault / relative
        if not source.is_file():
            failures.append(relative + ": missing page")
            continue
        text = source.read_text(encoding="utf-8")
        _, body = frontmatter(text)
        in_fence = False
        for number, line in enumerate(body.splitlines(), 1):
            if line.lstrip().startswith(("~~~", chr(96) * 3)):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for match in WIKILINK.finditer(line):
                target, detail = _resolve_link(vault, source, match.group(1), files)
                if target is None:
                    failures.append(f"{relative}:{number}: {detail}")
                elif detail and target.suffix == ".md":
                    headings, blocks = _headings_and_blocks(target.read_text(encoding="utf-8"))
                    if (detail[1:] not in blocks if detail.startswith("^") else detail not in headings):
                        failures.append(f"{relative}:{number}: missing anchor {detail}")
    return failures


def check(vault: Path, config_path: Path, index_dir: Path) -> dict:
    config = load_config(config_path)
    verify_protected(vault, config)
    model = build_model(vault, config_path)
    expected = index_bytes(model)
    if (index_dir / "index.json").exists() or any(
        not (index_dir / name).is_file() or (index_dir / name).read_bytes() != data
        for name, data in expected.items()
    ):
        raise IndexErrorWithContext("index missing or stale; run build")
    failures = link_failures(vault, config.get("critical_pages", []))
    if failures:
        raise IndexErrorWithContext("critical links invalid:\n" + "\n".join(failures))
    return read_index(index_dir)


def query(model: dict, vault: Path, term: str, args: argparse.Namespace) -> list[dict]:
    needle = term.casefold()
    exact = []
    partial = []
    for doc in model["documents"]:
        if args.project and doc["project"] != args.project:
            continue
        if args.vehicle and args.vehicle not in doc["vehicles"]:
            continue
        if args.scope and (not doc["scope"] or args.scope.casefold() not in doc["scope"].casefold()):
            continue
        if args.snapshot and doc["snapshot"] != args.snapshot:
            continue
        if not args.snapshot:
            if doc["class"] == "candidate" and not args.include_candidate:
                continue
            if doc["class"] == "historical" and not args.include_history:
                continue
        names = [doc["id"], doc["title"], *doc["aliases"]]
        if needle in [value.casefold() for value in names]:
            exact.append(doc)
        elif any(needle in str(value).casefold() for value in [*names, doc["path"], doc["summary"] or "", *doc["tags"]]):
            partial.append(doc)
        elif needle in (vault / doc["path"]).read_text(encoding="utf-8").casefold():
            partial.append(doc)
    matches = (exact + partial)[:args.limit]
    return [{
        **{key: doc[key] for key in ("id", "title", "path", "type", "entity_type", "project", "vehicles", "scope", "snapshot", "class", "status", "review", "aliases", "summary", "evidence", "sha256")},
        "relations": [item for item in model["relations"] if item["from"] == doc["id"] or item["to"] == doc["id"]],
    } for doc in matches]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--config", type=Path)
    parser.add_argument("--index-dir", type=Path)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("build")
    commands.add_parser("check")
    search = commands.add_parser("query")
    search.add_argument("term")
    search.add_argument("--project")
    search.add_argument("--vehicle")
    search.add_argument("--scope")
    search.add_argument("--snapshot")
    search.add_argument("--include-candidate", action="store_true")
    search.add_argument("--include-history", action="store_true")
    search.add_argument("--limit", type=int, default=10)
    args = parser.parse_args(argv)
    vault = args.vault.resolve()
    config = args.config or vault / "00_System/AI_Index/config.json"
    index_dir = args.index_dir or vault / "00_System/AI_Index"
    try:
        if args.command == "build":
            model = build_model(vault, config)
            verify_protected(vault, load_config(config))
            write_index(index_dir, model)
            print(f"indexed {len(model['documents'])} documents")
        elif args.command == "check":
            model = check(vault, config, index_dir)
            print(f"PASS: {len(model['documents'])} documents; immutable history and critical links verified")
        else:
            if args.limit < 1 or args.limit > 100:
                raise IndexErrorWithContext("limit must be 1..100")
            model = check(vault, config, index_dir)
            print(json.dumps(query(model, vault, args.term, args), ensure_ascii=False, indent=2))
    except (IndexErrorWithContext, OSError, UnicodeError, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
