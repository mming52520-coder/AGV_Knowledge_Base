from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping, Sequence


PROJECT_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = PROJECT_DIR.parents[1]
DEFAULT_MACHINE_DIR = WORKSPACE_ROOT / "work" / "v2_staging" / "output"
DEFAULT_V1_DIR = Path(
    r"D:\AGV_Knowledge_Base\00_System\Graph_History\Snapshots\code-v1"
)
DEFAULT_VAULT_DIR = Path(r"D:\AGV_Knowledge_Base")
DEFAULT_OUTPUT_DIR = PROJECT_DIR / "output"

ENTITY_GROUPS = {
    "ros_package": "Packages",
    "ros_node": "Nodes",
    "ros_interface": "Interfaces",
}
CHANGE_GROUPS = {
    "added": "Added",
    "modified": "Modified",
    "removed": "Removed",
}
INVALID_FILENAME = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")


class ProjectionError(RuntimeError):
    pass


@dataclass(frozen=True)
class ProjectionInputs:
    machine_dir: Path
    v1_dir: Path
    machine_bytes: Mapping[str, bytes]
    v1_bytes: Mapping[str, bytes]
    manifest: dict
    v1_manifest: dict
    entities: tuple[dict, ...]
    v1_entities: tuple[dict, ...]
    relations: tuple[dict, ...]
    v1_relations: tuple[dict, ...]
    migrations: tuple[dict, ...]
    warnings: tuple[dict, ...]
    diff: dict


@dataclass(frozen=True)
class ProjectionResult:
    vault_root: Path
    snapshot_id: str
    baseline_snapshot: str
    entity_page_count: int
    change_page_count: int
    tree_sha256: str


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _read_tree(root: Path) -> dict[str, bytes]:
    if not root.is_dir():
        raise ProjectionError(f"input directory does not exist: {root}")
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(root.rglob("*"), key=lambda item: item.as_posix())
        if path.is_file()
    }


def _decode_utf8_without_replacement(data: bytes, label: str) -> str:
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ProjectionError(f"invalid UTF-8 in {label}: {exc}") from exc
    if "\ufffd" in text:
        raise ProjectionError(f"Unicode replacement character U+FFFD in {label}")
    return text


def _json(data: bytes, label: str) -> dict:
    try:
        value = json.loads(_decode_utf8_without_replacement(data, label))
    except json.JSONDecodeError as exc:
        raise ProjectionError(f"invalid JSON in {label}: {exc}") from exc
    if not isinstance(value, dict):
        raise ProjectionError(f"expected JSON object in {label}")
    return value


def _jsonl(data: bytes, label: str) -> tuple[dict, ...]:
    rows: list[dict] = []
    text = _decode_utf8_without_replacement(data, label)
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ProjectionError(f"invalid JSONL in {label}:{line_number}: {exc}") from exc
        if not isinstance(value, dict):
            raise ProjectionError(f"expected object in {label}:{line_number}")
        rows.append(value)
    return tuple(rows)


def load_inputs(machine_dir: Path, v1_dir: Path) -> ProjectionInputs:
    machine_dir = machine_dir.resolve()
    v1_dir = v1_dir.resolve()
    machine_bytes = _read_tree(machine_dir)
    v1_bytes = _read_tree(v1_dir)
    allowed_machine = {
        "manifest.json",
        "entities.jsonl",
        "relations.jsonl",
        "migration-relations.jsonl",
        "extraction-warnings.jsonl",
        "source-files.jsonl",
        "v1-to-v2-diff.json",
        "V1-to-V2差异摘要.md",
    }
    allowed_v1 = {
        "manifest.json",
        "entities.jsonl",
        "relations.jsonl",
        "source-sets.jsonl",
        "V1基线说明.md",
    }
    missing_machine = sorted(allowed_machine - machine_bytes.keys())
    extra_machine = sorted(machine_bytes.keys() - allowed_machine)
    missing_v1 = sorted(allowed_v1 - v1_bytes.keys())
    extra_v1 = sorted(v1_bytes.keys() - allowed_v1)
    if missing_machine:
        raise ProjectionError(f"missing machine artifacts: {', '.join(missing_machine)}")
    if extra_machine:
        raise ProjectionError(f"unexpected machine artifacts: {', '.join(extra_machine)}")
    if missing_v1:
        raise ProjectionError(f"missing V1 artifacts: {', '.join(missing_v1)}")
    if extra_v1:
        raise ProjectionError(f"unexpected V1 artifacts: {', '.join(extra_v1)}")

    for name, data in sorted(machine_bytes.items()):
        _decode_utf8_without_replacement(data, f"machine/{name}")
    for name, data in sorted(v1_bytes.items()):
        _decode_utf8_without_replacement(data, f"V1/{name}")

    inputs = ProjectionInputs(
        machine_dir=machine_dir,
        v1_dir=v1_dir,
        machine_bytes=machine_bytes,
        v1_bytes=v1_bytes,
        manifest=_json(machine_bytes["manifest.json"], "manifest.json"),
        v1_manifest=_json(v1_bytes["manifest.json"], "V1/manifest.json"),
        entities=_jsonl(machine_bytes["entities.jsonl"], "entities.jsonl"),
        v1_entities=_jsonl(v1_bytes["entities.jsonl"], "V1/entities.jsonl"),
        relations=_jsonl(machine_bytes["relations.jsonl"], "relations.jsonl"),
        v1_relations=_jsonl(v1_bytes["relations.jsonl"], "V1/relations.jsonl"),
        migrations=_jsonl(
            machine_bytes["migration-relations.jsonl"], "migration-relations.jsonl"
        ),
        warnings=_jsonl(
            machine_bytes["extraction-warnings.jsonl"], "extraction-warnings.jsonl"
        ),
        diff=_json(machine_bytes["v1-to-v2-diff.json"], "v1-to-v2-diff.json"),
    )
    _validate_inputs(inputs)
    return inputs


def _require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ProjectionError(f"{label}: expected {expected!r}, got {actual!r}")


def _validate_unique_uids(rows: Sequence[dict], label: str) -> set[str]:
    uids = [str(row.get("entity_uid", "")) for row in rows]
    if any(not uid for uid in uids):
        raise ProjectionError(f"{label} contains an empty entity_uid")
    duplicates = sorted(uid for uid, count in Counter(uids).items() if count > 1)
    if duplicates:
        raise ProjectionError(f"duplicate {label} entity_uid: {', '.join(duplicates)}")
    return set(uids)


def _validate_inputs(inputs: ProjectionInputs) -> None:
    manifest = inputs.manifest
    v1_manifest = inputs.v1_manifest
    snapshot_id = str(manifest.get("snapshot_id", ""))
    baseline = str(manifest.get("baseline_snapshot", ""))
    if not snapshot_id or not baseline:
        raise ProjectionError("manifest snapshot_id and baseline_snapshot are required")
    _require_equal(inputs.diff.get("target_snapshot"), snapshot_id, "diff target snapshot")
    _require_equal(inputs.diff.get("baseline_snapshot"), baseline, "diff baseline snapshot")
    _require_equal(v1_manifest.get("snapshot_id"), baseline, "V1 baseline snapshot")

    entity_uids = _validate_unique_uids(inputs.entities, "V2")
    v1_uids = _validate_unique_uids(inputs.v1_entities, "V1")
    _require_equal(manifest.get("entity_count"), len(inputs.entities), "entity count")
    actual_types = dict(sorted(Counter(row.get("type") for row in inputs.entities).items()))
    declared_types = dict(sorted((manifest.get("entity_type_counts") or {}).items()))
    _require_equal(actual_types, declared_types, "entity type counts")
    unsupported = sorted(set(actual_types) - ENTITY_GROUPS.keys())
    if unsupported:
        raise ProjectionError(f"unsupported entity types: {', '.join(unsupported)}")
    _require_equal(
        manifest.get("semantic_relation_count"), len(inputs.relations), "relation count"
    )
    _require_equal(
        manifest.get("migration_relation_count"),
        len(inputs.migrations),
        "migration relation count",
    )
    _require_equal(manifest.get("warning_count"), len(inputs.warnings), "warning count")

    for relation in inputs.relations:
        missing = [
            uid
            for uid in (relation.get("from_entity_uid"), relation.get("to_entity_uid"))
            if uid not in entity_uids
        ]
        if missing:
            raise ProjectionError(
                "missing relation endpoint: "
                + ", ".join(str(uid) for uid in missing)
                + f" in {relation!r}"
            )
    for migration in inputs.migrations:
        if migration.get("from_entity_uid") not in v1_uids:
            raise ProjectionError(
                f"missing migration V1 endpoint: {migration.get('from_entity_uid')}"
            )
        _require_equal(migration.get("from_snapshot"), baseline, "migration baseline")
        to_uid = migration.get("to_entity_uid")
        if to_uid is None:
            _require_equal(migration.get("to_snapshot"), None, "terminal migration target")
        else:
            if to_uid not in entity_uids:
                raise ProjectionError(f"missing migration V2 endpoint: {to_uid}")
            _require_equal(migration.get("to_snapshot"), snapshot_id, "migration target")

    for name, expected in sorted((manifest.get("artifact_sha256") or {}).items()):
        if name not in inputs.machine_bytes:
            raise ProjectionError(f"manifest hash references missing artifact: {name}")
        _require_equal(sha256_bytes(inputs.machine_bytes[name]), expected, f"artifact hash {name}")
    for name, key in (
        ("entities.jsonl", "entities_sha256"),
        ("relations.jsonl", "relations_sha256"),
        ("source-sets.jsonl", "source_sets_sha256"),
    ):
        if key in v1_manifest:
            if name not in inputs.v1_bytes:
                raise ProjectionError(f"V1 manifest hash references missing artifact: {name}")
            _require_equal(
                sha256_bytes(inputs.v1_bytes[name]), v1_manifest[key], f"V1 artifact hash {name}"
            )

    counts = inputs.diff.get("entity_counts") or {}
    _require_equal(counts.get("baseline"), counts.get("matched", 0) + counts.get("removed", 0), "V1 entity conservation")
    _require_equal(counts.get("target"), counts.get("matched", 0) + counts.get("added", 0), "V2 entity conservation")
    _require_equal(counts.get("matched"), counts.get("unchanged", 0) + counts.get("modified", 0), "matched entity conservation")
    _require_equal(counts.get("target"), len(inputs.entities), "diff target entity count")
    changes = inputs.diff.get("entity_changes") or []
    expected_changes = counts.get("added", 0) + counts.get("modified", 0) + counts.get("removed", 0)
    _require_equal(len(changes), expected_changes, "entity change count")
    change_uids = [change.get("entity_uid") for change in changes]
    if len(change_uids) != len(set(change_uids)):
        raise ProjectionError("duplicate entity_uid in diff entity_changes")

    relation_counts = inputs.diff.get("relation_counts") or {}
    _require_equal(relation_counts.get("target"), len(inputs.relations), "diff target relation count")
    _require_equal(
        relation_counts.get("added"), len(inputs.diff.get("relation_added") or []), "added relation count"
    )
    _require_equal(
        relation_counts.get("removed"), len(inputs.diff.get("relation_removed") or []), "removed relation count"
    )
    _require_equal(
        inputs.diff.get("migration_relation_count"), len(inputs.migrations), "diff migration count"
    )

    for relation in inputs.diff.get("relation_added") or []:
        if (
            relation.get("from_entity_uid") not in entity_uids
            or relation.get("to_entity_uid") not in entity_uids
        ):
            raise ProjectionError(f"missing added relation endpoint: {relation!r}")
    for relation in inputs.diff.get("relation_removed") or []:
        if (
            relation.get("from_entity_uid") not in v1_uids
            or relation.get("to_entity_uid") not in v1_uids
        ):
            raise ProjectionError(f"missing removed relation endpoint: {relation!r}")

    risks = inputs.diff.get("risks") or []
    _require_equal(inputs.diff.get("risk_count", len(risks)), len(risks), "diff risk count")
    _require_equal(manifest.get("risk_count", len(risks)), len(risks), "manifest risk count")
    risk_ids = [str(risk.get("risk_id", "")) for risk in risks]
    if any(not risk_id for risk_id in risk_ids):
        raise ProjectionError("risk without risk_id")
    if len(risk_ids) != len(set(risk_ids)):
        raise ProjectionError("duplicate risk_id in diff risks")

    manifest_limitations = manifest.get("comparison_limitations") or []
    diff_limitations = inputs.diff.get("comparison_limitations") or []
    _require_equal(diff_limitations, manifest_limitations, "comparison limitations")
    limitation_ids = [str(row.get("limitation_id", "")) for row in diff_limitations]
    if any(not limitation_id for limitation_id in limitation_ids):
        raise ProjectionError("comparison limitation without limitation_id")
    if len(limitation_ids) != len(set(limitation_ids)):
        raise ProjectionError("duplicate comparison limitation_id")


def tree_fingerprint(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix()):
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix().encode("utf-8")
        digest.update(len(relative).to_bytes(4, "big"))
        digest.update(relative)
        data = path.read_bytes()
        digest.update(len(data).to_bytes(8, "big"))
        digest.update(data)
    return digest.hexdigest()


def _safe_filename(title: str, uid: str) -> str:
    readable = INVALID_FILENAME.sub("-", title).strip(" .-")
    readable = re.sub(r"\s+", " ", readable)
    if not readable:
        readable = uid.rsplit(":", 1)[-1] or "entity"
    readable = readable[:48].rstrip(" .-") or "entity"
    if readable.upper() in {
        "CON",
        "PRN",
        "AUX",
        "NUL",
        *(f"COM{index}" for index in range(1, 10)),
        *(f"LPT{index}" for index in range(1, 10)),
    }:
        readable = "entity-" + readable
    suffix = hashlib.sha256(uid.encode("utf-8")).hexdigest()[:12]
    return f"{readable}--{suffix}.md"


def _vault_path(*parts: str) -> PurePosixPath:
    return PurePosixPath(*parts)


def _disk_path(root: Path, relative: PurePosixPath) -> Path:
    return root.joinpath(*relative.parts)


def _without_suffix(relative: PurePosixPath) -> str:
    return relative.with_suffix("").as_posix()


def _wiki(relative: PurePosixPath, label: str) -> str:
    return f"[[{_without_suffix(relative)}|{label}]]"


def _v1_wiki(entity: dict) -> str:
    relative = PurePosixPath(str(entity["path"]))
    return _wiki(relative, str(entity.get("title") or entity["entity_uid"]))


def _yaml_value(value: object) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def _frontmatter(fields: Sequence[tuple[str, object]]) -> str:
    lines = ["---"]
    lines.extend(f"{key}: {_yaml_value(value)}" for key, value in fields)
    lines.append("---")
    return "\n".join(lines) + "\n"


def _write_text(root: Path, relative: PurePosixPath, text: str) -> None:
    target = _disk_path(root, relative)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def _write_bytes(root: Path, relative: PurePosixPath, data: bytes) -> None:
    target = _disk_path(root, relative)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)


def _markdown_cell(value: object) -> str:
    if isinstance(value, (dict, list)):
        text = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    elif value is None:
        text = ""
    else:
        text = str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def _entity_paths(entities: Sequence[dict], snapshot_id: str) -> dict[str, PurePosixPath]:
    base = _vault_path(
        "00_System", "Graph_History", "Snapshots", snapshot_id, "Entities"
    )
    paths: dict[str, PurePosixPath] = {}
    casefolded: dict[str, str] = {}
    for entity in sorted(entities, key=lambda row: row["entity_uid"]):
        uid = str(entity["entity_uid"])
        group = ENTITY_GROUPS[str(entity["type"])]
        relative = base / group / _safe_filename(str(entity.get("title") or uid), uid)
        folded = relative.as_posix().casefold()
        if folded in casefolded:
            raise ProjectionError(
                f"entity page path collision: {uid} and {casefolded[folded]} -> {relative}"
            )
        casefolded[folded] = uid
        paths[uid] = relative
    return paths


def _change_paths(changes: Sequence[dict], baseline: str, target: str) -> dict[str, PurePosixPath]:
    base = _vault_path("00_System", "Graph_History", "Changes", f"{baseline}__{target}")
    paths: dict[str, PurePosixPath] = {}
    casefolded: dict[str, str] = {}
    for change in sorted(changes, key=lambda row: row["entity_uid"]):
        uid = str(change["entity_uid"])
        kind = str(change["change_kind"])
        category = _change_category(kind)
        relative = base / "Entities" / CHANGE_GROUPS[category] / _safe_filename(uid.rsplit(":", 1)[-1], uid)
        folded = relative.as_posix().casefold()
        if folded in casefolded:
            raise ProjectionError(
                f"change page path collision: {uid} and {casefolded[folded]} -> {relative}"
            )
        casefolded[folded] = uid
        paths[uid] = relative
    return paths


def _change_category(kind: str) -> str:
    if kind in {"added", "modified"}:
        return kind
    if kind == "removed" or kind.startswith("removed_"):
        return "removed"
    raise ProjectionError(f"unsupported change kind: {kind}")


def _entity_page(
    entity: dict,
    *,
    snapshot_id: str,
    snapshot_note: PurePosixPath,
    entity_paths: Mapping[str, PurePosixPath],
    change_paths: Mapping[str, PurePosixPath],
    change_by_uid: Mapping[str, dict],
    outgoing: Mapping[str, Sequence[dict]],
    incoming: Mapping[str, Sequence[dict]],
    created: str,
) -> str:
    uid = str(entity["entity_uid"])
    title = str(entity.get("title") or uid)
    instance_id = f"{snapshot_id}::{uid}"
    group_index = entity_paths[uid].parent / "_index.md"
    fields = [
        ("id", instance_id),
        ("type", "graph_entity_instance"),
        ("logical_entity_uid", uid),
        ("snapshot_instance_id", instance_id),
        ("snapshot_id", snapshot_id),
        ("entity_type", entity["type"]),
        ("title", title),
        ("status", entity.get("status", "")),
        ("review", entity.get("review", "generated")),
        ("source_snapshot", entity.get("source_snapshot", "")),
        ("semantic_fingerprint", entity.get("semantic_fingerprint", "")),
        ("relation_fingerprint", entity.get("relation_fingerprint", "")),
        ("updated", created),
        ("tags", ["AGV", "代码图谱", "V2", "实体实例"]),
    ]
    lines = [
        _frontmatter(fields),
        f"# {title}",
        "",
        f"- 逻辑实体：`{uid}`",
        f"- 快照实例：`{instance_id}`",
        f"- 所属快照：{_wiki(snapshot_note, snapshot_id)}",
        f"- 分组索引：{_wiki(group_index, entity_paths[uid].parent.name)}",
        f"- 代码证据主路径：`{entity.get('path', '')}`",
        "",
        "## 语义属性",
        "",
        "| 字段 | 值 |",
        "|---|---|",
    ]
    semantic_value = entity.get("semantic") or {}
    for key in sorted(semantic_value):
        lines.append(f"| `{key}` | {_markdown_cell(semantic_value[key])} |")

    evidence = entity.get("evidence") or []
    lines.extend(["", "## 证据", ""])
    if evidence:
        lines.extend(["| 路径 | 行 | 操作 | 文件 SHA-256 |", "|---|---:|---|---|"])
        for item in sorted(
            evidence,
            key=lambda row: (
                str(row.get("path", "")),
                int(row.get("line") or 0),
                str(row.get("operation", "")),
            ),
        ):
            lines.append(
                "| `{}` | {} | `{}` | `{}` |".format(
                    _markdown_cell(item.get("path", "")),
                    _markdown_cell(item.get("line", "")),
                    _markdown_cell(item.get("operation", "")),
                    _markdown_cell(item.get("file_sha256", "")),
                )
            )
    else:
        lines.append("本次抽取没有记录逐行证据；需结合机器清单复核。")

    lines.extend(["", "## 出向关系", ""])
    if outgoing.get(uid):
        for relation in sorted(
            outgoing[uid],
            key=lambda row: (row["predicate"], row["to_entity_uid"], json.dumps(row.get("qualifiers") or {}, sort_keys=True)),
        ):
            target_uid = str(relation["to_entity_uid"])
            lines.append(
                f"- `{relation['predicate']}` → {_wiki(entity_paths[target_uid], target_uid)}"
            )
    else:
        lines.append("- 无")

    lines.extend(["", "## 入向关系", ""])
    if incoming.get(uid):
        for relation in sorted(
            incoming[uid],
            key=lambda row: (row["predicate"], row["from_entity_uid"], json.dumps(row.get("qualifiers") or {}, sort_keys=True)),
        ):
            source_uid = str(relation["from_entity_uid"])
            lines.append(
                f"- {_wiki(entity_paths[source_uid], source_uid)} → `{relation['predicate']}`"
            )
    else:
        lines.append("- 无")

    change = change_by_uid.get(uid)
    lines.extend(["", "## 相对 V1 的变化", ""])
    if change:
        lines.append(f"- 变化类型：`{change['change_kind']}`")
        changed_fields = change.get("changed_fields") or []
        lines.append(
            "- 变化字段：" + (", ".join(f"`{field}`" for field in changed_fields) if changed_fields else "无")
        )
        lines.append(f"- 差异记录：{_wiki(change_paths[uid], uid)}")
    else:
        lines.append("- `unchanged`：语义指纹与 V1 一致。")
    return "\n".join(lines)


def _change_page(
    change: dict,
    *,
    baseline: str,
    target: str,
    diff_index: PurePosixPath,
    entity_paths: Mapping[str, PurePosixPath],
    v1_by_uid: Mapping[str, dict],
    v2_by_uid: Mapping[str, dict],
    created: str,
) -> str:
    uid = str(change["entity_uid"])
    kind = str(change["change_kind"])
    title = str((v2_by_uid.get(uid) or v1_by_uid.get(uid) or {}).get("title") or uid)
    change_id = f"agv:graph-change:{baseline}__{target}:{uid}"
    fields = [
        ("id", change_id),
        ("type", "graph_change"),
        ("baseline_snapshot", baseline),
        ("target_snapshot", target),
        ("logical_entity_uid", uid),
        ("change_kind", kind),
        ("before_fingerprint", change.get("before_fingerprint", "")),
        ("after_fingerprint", change.get("after_fingerprint", "")),
        ("changed_fields", change.get("changed_fields") or []),
        ("breaking", bool(change.get("breaking"))),
        ("match_method", change.get("match_method", "")),
        ("match_confidence", change.get("match_confidence", 0)),
        ("review", change.get("review", "generated")),
        ("updated", created),
        ("tags", ["AGV", "代码图谱", "V1-V2差异", kind]),
    ]
    lines = [
        _frontmatter(fields),
        f"# {kind}: {title}",
        "",
        f"- 逻辑实体：`{uid}`",
        f"- 差异索引：{_wiki(diff_index, 'V1 → V2 差异总览')}",
        f"- 匹配方法：`{change.get('match_method', '')}`",
        f"- 匹配置信度：`{change.get('match_confidence', '')}`",
        f"- 潜在破坏性：`{str(bool(change.get('breaking'))).lower()}`",
        "",
        "## 版本实例",
        "",
    ]
    if uid in v1_by_uid:
        lines.append(f"- V1 原始节点：{_v1_wiki(v1_by_uid[uid])}")
        lines.append(f"- V1 实例 ID：`{baseline}::{uid}`")
    else:
        lines.append("- V1：不存在该逻辑实体。")
    if uid in v2_by_uid:
        lines.append(f"- V2 快照节点：{_wiki(entity_paths[uid], title)}")
        lines.append(f"- V2 实例 ID：`{target}::{uid}`")
    else:
        lines.append("- V2：本次快照未抽取到该逻辑实体；这不是删除 V1 页面。")
    lines.extend(
        [
            "",
            "## 字段差异",
            "",
            "- 变化字段："
            + (
                ", ".join(f"`{field}`" for field in change.get("changed_fields") or [])
                or "无逐字段变化记录"
            ),
            f"- 变更前指纹：`{change.get('before_fingerprint', '')}`",
            f"- 变更后指纹：`{change.get('after_fingerprint', '')}`",
        ]
    )
    if _change_category(kind) == "removed":
        lines.extend(
            [
                "",
                "> [!warning] 复核要求",
                "> V1 没有逐文件清单，因此这里只能判定“V1 有、V2 当前扫描未匹配”；不能据此断言源码已删除。",
            ]
        )
    return "\n".join(lines)


def _group_index_page(
    *,
    title: str,
    group: str,
    snapshot_id: str,
    snapshot_note: PurePosixPath,
    entities: Sequence[dict],
    entity_paths: Mapping[str, PurePosixPath],
    created: str,
) -> str:
    fields = [
        ("id", f"agv:graph-snapshot-index:{snapshot_id}:{group.lower()}"),
        ("type", "index"),
        ("snapshot_id", snapshot_id),
        ("entity_group", group),
        ("entity_count", len(entities)),
        ("status", "active"),
        ("review", "generated"),
        ("updated", created),
        ("tags", ["AGV", "代码图谱", "V2", group]),
    ]
    lines = [
        _frontmatter(fields),
        f"# {title}",
        "",
        f"本组共 **{len(entities)}** 个快照实例。",
        "",
    ]
    for entity in sorted(entities, key=lambda row: (str(row.get("title", "")), row["entity_uid"])):
        uid = str(entity["entity_uid"])
        lines.append(f"- {_wiki(entity_paths[uid], str(entity.get('title') or uid))} — `{uid}`")
    lines.extend(["", f"- {_wiki(snapshot_note, '返回 V2 快照说明')}"])
    return "\n".join(lines)


def _snapshot_note_page(
    inputs: ProjectionInputs,
    *,
    snapshot_note: PurePosixPath,
    diff_index: PurePosixPath,
    group_indexes: Mapping[str, PurePosixPath],
) -> str:
    manifest = inputs.manifest
    snapshot_id = str(manifest["snapshot_id"])
    baseline = str(manifest["baseline_snapshot"])
    created = str(manifest.get("created", ""))
    artifact_hashes = manifest.get("artifact_sha256") or {}
    fields = [
        ("id", f"agv:graph-snapshot:{snapshot_id}"),
        ("type", "graph_snapshot"),
        ("snapshot_id", snapshot_id),
        ("graph_version", manifest.get("graph_version", "v2")),
        ("status", "candidate"),
        ("review", "generated"),
        ("baseline_snapshot", baseline),
        ("graph_schema_version", manifest.get("graph_schema_version")),
        ("extractor_version", manifest.get("extractor_version", "")),
        ("scope_id", manifest.get("scope_id", "")),
        ("source_snapshot", manifest.get("source_fingerprint", "")),
        ("entities_fingerprint", artifact_hashes.get("entities.jsonl", "")),
        ("relations_fingerprint", artifact_hashes.get("relations.jsonl", "")),
        ("created", created),
        ("updated", created),
        ("tags", ["AGV", "代码图谱", "V2", "候选快照"]),
    ]
    counts = manifest.get("entity_type_counts") or {}
    lines = [
        _frontmatter(fields),
        "# 代码图谱 V2 快照说明",
        "",
        f"本页描述候选快照 `{snapshot_id}`。它与 V1 并存，不修改既有 `03_ROS` 页面。",
        "",
        "## 身份与来源",
        "",
        f"- 基线：`{baseline}`",
        f"- 来源：`{manifest.get('source_locator', '')}`",
        f"- 来源指纹：`{manifest.get('source_fingerprint', '')}`",
        f"- Git HEAD：`{(manifest.get('git_state') or {}).get('head', '')}`",
        f"- 工作树含未提交变化：`{str(bool((manifest.get('git_state') or {}).get('dirty'))).lower()}`",
        "",
        "## 图谱规模",
        "",
        "| 项目 | 数量 |",
        "|---|---:|",
        f"| 实体总数 | {manifest.get('entity_count', 0)} |",
        f"| Package | {counts.get('ros_package', 0)} |",
        f"| Node | {counts.get('ros_node', 0)} |",
        f"| Interface | {counts.get('ros_interface', 0)} |",
        f"| 语义关系 | {manifest.get('semantic_relation_count', 0)} |",
        f"| 迁移/分解关系 | {manifest.get('migration_relation_count', 0)} |",
        f"| 纳入源文件 | {manifest.get('included_source_file_count', 0)} |",
        f"| 排除源文件 | {manifest.get('excluded_source_file_count', 0)} |",
        f"| 抽取警告 | {manifest.get('warning_count', 0)} |",
        "",
        "## 实体实例",
        "",
    ]
    for group, label in (("Packages", "Packages"), ("Nodes", "Nodes"), ("Interfaces", "Interfaces")):
        lines.append(f"- {_wiki(group_indexes[group], label)}")
    lines.extend(
        [
            "",
            "## 与 V1 的差异",
            "",
            f"- {_wiki(diff_index, 'V1 → V2 差异总览')}",
            "",
            "## 比较限制",
            "",
        ]
    )
    for limitation in manifest.get("comparison_limitations") or []:
        lines.append(
            f"- **`{limitation.get('limitation_id', '')}`**：{limitation.get('detail', '')}"
        )
    if not manifest.get("comparison_limitations"):
        lines.append("- 无")
    lines.extend(["", "## 抽取限制", ""])
    for limitation in manifest.get("extraction_limitations") or []:
        lines.append(
            f"- **`{limitation.get('limitation_id', '')}`**：{limitation.get('detail', '')}"
        )
    if not manifest.get("extraction_limitations"):
        lines.append("- 无")
    lines.extend(
        [
            "",
            "## 原始机器产物",
            "",
            "以下文件从机器产物目录逐字节复制，未做转码或格式化：",
            "",
        ]
    )
    for name in sorted(inputs.machine_bytes):
        lines.append(f"- [`{name}`](Machine/{name})")
    lines.extend(
        [
            "",
            "> [!warning] 候选快照",
            "> 当前来源工作树可能含未提交变化，且页面为自动生成状态；完成风险复核前不替代 V1 推荐指针。",
        ]
    )
    return "\n".join(lines)


def _diff_index_page(
    inputs: ProjectionInputs,
    *,
    snapshot_note: PurePosixPath,
    v1_note: PurePosixPath,
    entity_summary: PurePosixPath,
    relation_summary: PurePosixPath,
    migration_summary: PurePosixPath,
    risk_summary: PurePosixPath,
    canvas_path: PurePosixPath,
) -> str:
    baseline = str(inputs.manifest["baseline_snapshot"])
    target = str(inputs.manifest["snapshot_id"])
    created = str(inputs.manifest.get("created", ""))
    counts = inputs.diff["entity_counts"]
    relation_counts = inputs.diff["relation_counts"]
    fields = [
        ("id", f"agv:graph-diff:{baseline}__{target}"),
        ("type", "graph_diff"),
        ("baseline_snapshot", baseline),
        ("target_snapshot", target),
        ("status", "candidate"),
        ("review", "generated"),
        ("updated", created),
        ("tags", ["AGV", "代码图谱", "V1-V2差异"]),
    ]
    lines = [
            _frontmatter(fields),
            "# V1 → V2 差异总览",
            "",
            f"- V1：{_wiki(v1_note, baseline)}",
            f"- V2：{_wiki(snapshot_note, target)}",
            "",
            "## 数量守恒",
            "",
            "| 范围 | 基线 | 匹配 | 新增 | 修改 | 未变化 | 未匹配 | 目标 |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
            "| 实体 | {baseline} | {matched} | {added} | {modified} | {unchanged} | {removed} | {target} |".format(**counts),
            "",
            "| 关系 | V1 | 新增 | 未匹配 | V2 |",
            "|---|---:|---:|---:|---:|",
            "| 语义关系 | {baseline} | {added} | {removed} | {target} |".format(**relation_counts),
            "",
            "## 导航",
            "",
            f"- {_wiki(entity_summary, '实体差异')}",
            f"- {_wiki(relation_summary, '关系差异')}",
            f"- {_wiki(migration_summary, '迁移与分解')}",
            f"- {_wiki(risk_summary, '风险与复核')}",
            f"- {_wiki(canvas_path, 'V1 → V2 架构演化 Canvas')}",
            "",
            "## 比较限制",
            "",
        ]
    for limitation in inputs.diff.get("comparison_limitations") or []:
        lines.append(
            f"- **`{limitation.get('limitation_id', '')}`**：{limitation.get('detail', '')}"
        )
    if not inputs.diff.get("comparison_limitations"):
        lines.append("- 无")
    lines.extend(
        [
            "",
            "> [!important] 未匹配不等于删除",
            "> V1 只有来源集聚合哈希，没有逐文件清单。`removed` 仅表示 V2 当前扫描未匹配到同一逻辑实体，V1 页面继续保留。",
        ]
    )
    return "\n".join(lines)


def _entity_diff_summary_page(
    inputs: ProjectionInputs,
    *,
    diff_index: PurePosixPath,
    change_paths: Mapping[str, PurePosixPath],
    v1_by_uid: Mapping[str, dict],
    v2_by_uid: Mapping[str, dict],
) -> str:
    created = str(inputs.manifest.get("created", ""))
    fields = [
        ("id", f"agv:graph-diff-entities:{inputs.manifest['baseline_snapshot']}__{inputs.manifest['snapshot_id']}"),
        ("type", "index"),
        ("status", "candidate"),
        ("review", "generated"),
        ("updated", created),
        ("tags", ["AGV", "代码图谱", "实体差异"]),
    ]
    lines = [_frontmatter(fields), "# 实体差异", ""]
    grouped: dict[str, list[dict]] = defaultdict(list)
    for change in inputs.diff["entity_changes"]:
        grouped[_change_category(str(change["change_kind"]))].append(change)
    labels = {"added": "新增", "modified": "语义变化", "removed": "V2 未匹配"}
    for kind in ("added", "modified", "removed"):
        rows = sorted(grouped.get(kind, []), key=lambda row: row["entity_uid"])
        lines.extend([f"## {labels[kind]}（{len(rows)}）", ""])
        for change in rows:
            uid = str(change["entity_uid"])
            entity = v2_by_uid.get(uid) or v1_by_uid.get(uid) or {}
            label = str(entity.get("title") or uid)
            lines.append(f"- {_wiki(change_paths[uid], label)} — `{uid}`")
        if not rows:
            lines.append("- 无")
        lines.append("")
    lines.append(f"- {_wiki(diff_index, '返回差异总览')}")
    return "\n".join(lines)


def _relation_diff_page(
    inputs: ProjectionInputs,
    *,
    diff_index: PurePosixPath,
    v1_by_uid: Mapping[str, dict],
) -> str:
    created = str(inputs.manifest.get("created", ""))
    added = inputs.diff.get("relation_added") or []
    removed = inputs.diff.get("relation_removed") or []
    added_counts = Counter(str(row.get("predicate", "")) for row in added)
    removed_counts = Counter(str(row.get("predicate", "")) for row in removed)
    predicates = sorted(set(added_counts) | set(removed_counts))
    fields = [
        ("id", f"agv:graph-diff-relations:{inputs.manifest['baseline_snapshot']}__{inputs.manifest['snapshot_id']}"),
        ("type", "graph_relation_diff"),
        ("status", "candidate"),
        ("review", "generated"),
        ("updated", created),
        ("tags", ["AGV", "代码图谱", "关系差异"]),
    ]
    lines = [
        _frontmatter(fields),
        "# 关系差异",
        "",
        "完整逐关系记录保存在 V2 快照的 `Machine/v1-to-v2-diff.json`；本页按谓词汇总。",
        "",
        "| 谓词 | 新增 | V2 未匹配 |",
        "|---|---:|---:|",
    ]
    for predicate in predicates:
        lines.append(f"| `{predicate}` | {added_counts[predicate]} | {removed_counts[predicate]} |")
    removed_classifications = Counter(
        str(row.get("comparison_classification", "unspecified")) for row in removed
    )
    removed_reviews = Counter(str(row.get("review", "unspecified")) for row in removed)
    lines.extend(
        [
            "",
            f"- 新增关系总数：**{len(added)}**",
            f"- V2 未匹配关系总数：**{len(removed)}**",
            "- 未匹配关系分类："
            + ", ".join(
                f"`{name}` **{count}**"
                for name, count in sorted(removed_classifications.items())
            ),
            "- 复核状态："
            + ", ".join(
                f"`{name}` **{count}**" for name, count in sorted(removed_reviews.items())
            ),
            "",
            "> [!warning] 关系删除判读",
            "> V1 与 V2 使用不同抽取器；以下记录均是 V2 未匹配候选，不是运行时关系已删除的证明。",
            "",
            f"## V1-only 关系明细（{len(removed)}）",
            "",
            "| # | V1 起点 | 谓词 | V1 终点 | 比较分类 | 复核 |",
            "|---:|---|---|---|---|---|",
        ]
    )
    for index, relation in enumerate(
        sorted(
            removed,
            key=lambda row: (
                str(row.get("from_entity_uid", "")),
                str(row.get("predicate", "")),
                str(row.get("to_entity_uid", "")),
            ),
        ),
        start=1,
    ):
        from_uid = str(relation.get("from_entity_uid", ""))
        to_uid = str(relation.get("to_entity_uid", ""))
        from_cell = _v1_wiki(v1_by_uid[from_uid])
        to_cell = _v1_wiki(v1_by_uid[to_uid])
        lines.append(
            "| {} | {} | `{}` | {} | `{}` | `{}` |".format(
                index,
                from_cell,
                relation.get("predicate", ""),
                to_cell,
                relation.get("comparison_classification", ""),
                relation.get("review", ""),
            )
        )
    if not removed:
        lines.append("| - | - | - | - | - | - |")
    lines.extend(["", f"- {_wiki(diff_index, '返回差异总览')}"])
    return "\n".join(lines)


def _migration_page(
    inputs: ProjectionInputs,
    *,
    diff_index: PurePosixPath,
    entity_paths: Mapping[str, PurePosixPath],
    v1_by_uid: Mapping[str, dict],
    v2_by_uid: Mapping[str, dict],
) -> str:
    created = str(inputs.manifest.get("created", ""))
    fields = [
        ("id", f"agv:graph-migrations:{inputs.manifest['baseline_snapshot']}__{inputs.manifest['snapshot_id']}"),
        ("type", "graph_migration_index"),
        ("status", "candidate"),
        ("review", "generated"),
        ("updated", created),
        ("tags", ["AGV", "代码图谱", "迁移", "分解"]),
    ]
    lines = [
        _frontmatter(fields),
        "# 迁移与分解",
        "",
        "这些关系显式连接 V1 逻辑实体与 V2 逻辑实体，不覆盖任一版本实例。",
        "",
        "| V1 实体 | 关系 | V2 实体 | 置信度 | 方法 |",
        "|---|---|---|---:|---|",
    ]
    for relation in sorted(
        inputs.migrations,
        key=lambda row: (
            row["from_entity_uid"],
            row["predicate"],
            str(row.get("to_entity_uid") or ""),
        ),
    ):
        from_uid = str(relation["from_entity_uid"])
        to_uid = relation.get("to_entity_uid")
        if to_uid is None:
            target_cell = "V2 无替代实例"
        else:
            target_uid = str(to_uid)
            target_cell = _wiki(
                entity_paths[target_uid], str(v2_by_uid[target_uid].get("title") or target_uid)
            )
        lines.append(
            "| {} | `{}` | {} | {} | `{}` |".format(
                _v1_wiki(v1_by_uid[from_uid]),
                relation["predicate"],
                target_cell,
                relation.get("confidence", ""),
                relation.get("match_method", ""),
            )
        )
    lines.extend(["", f"- {_wiki(diff_index, '返回差异总览')}"])
    return "\n".join(lines)


def _risk_page(
    inputs: ProjectionInputs,
    *,
    diff_index: PurePosixPath,
    change_paths: Mapping[str, PurePosixPath],
    v1_by_uid: Mapping[str, dict],
    v2_by_uid: Mapping[str, dict],
) -> str:
    created = str(inputs.manifest.get("created", ""))
    fields = [
        ("id", f"agv:graph-risk-review:{inputs.manifest['baseline_snapshot']}__{inputs.manifest['snapshot_id']}"),
        ("type", "graph_review_queue"),
        ("status", "open"),
        ("review", "generated"),
        ("updated", created),
        ("tags", ["AGV", "代码图谱", "风险复核"]),
    ]
    removed = [
        row
        for row in inputs.diff["entity_changes"]
        if _change_category(str(row["change_kind"])) == "removed"
    ]
    breaking = [row for row in inputs.diff["entity_changes"] if row.get("breaking")]
    lines = [
        _frontmatter(fields),
        "# 风险与复核",
        "",
        "## 快照来源风险",
        "",
        f"- 工作树含未提交变化：`{str(bool((inputs.manifest.get('git_state') or {}).get('dirty'))).lower()}`",
        f"- 抽取警告：**{len(inputs.warnings)}**",
        f"- V1 限制：{inputs.manifest.get('baseline_manifest_limitation', '')}",
        "",
        "## 抽取警告",
        "",
    ]
    if inputs.warnings:
        lines.extend(
            [
                "| # | 类型 | 路径 | 详情 |",
                "|---:|---|---|---|",
            ]
        )
        for index, warning in enumerate(inputs.warnings, start=1):
            lines.append(
                "| {} | `{}` | `{}` | {} |".format(
                    index,
                    warning.get("kind", ""),
                    warning.get("path", ""),
                    str(warning.get("detail", "")).replace("|", "\\|"),
                )
            )
    else:
        lines.append("- 无")

    risks = inputs.diff.get("risks") or []
    lines.extend(["", f"## 风险登记（{len(risks)}）", ""])
    for risk in sorted(risks, key=lambda row: str(row.get("risk_id", ""))):
        risk_id = str(risk.get("risk_id", ""))
        lines.extend(
            [
                f"### {risk_id} · {risk.get('risk_kind', '')}",
                "",
                f"- 严重度：`{risk.get('severity', '')}`",
                f"- 潜在破坏性：`{str(bool(risk.get('breaking'))).lower()}`",
                f"- 复核状态：`{risk.get('review', '')}`",
                f"- 验证状态：`{risk.get('validation_state', '')}`",
                f"- 已运行独立测试：`{str(bool(risk.get('independent_tests_run'))).lower()}`",
                f"- 陈述：{risk.get('statement', '')}",
                f"- 证据数：**{len(risk.get('evidence') or [])}**",
                "",
                "```json",
                json.dumps(
                    risk.get("evidence") or [],
                    ensure_ascii=False,
                    sort_keys=True,
                    indent=2,
                ),
                "```",
                "",
            ]
        )
    if not risks:
        lines.append("- 无")

    lines.extend(["", f"## V2 未匹配实体（{len(removed)}）", ""])
    for change in sorted(removed, key=lambda row: row["entity_uid"]):
        uid = str(change["entity_uid"])
        label = str((v1_by_uid.get(uid) or {}).get("title") or uid)
        lines.append(f"- {_wiki(change_paths[uid], label)}")
    if not removed:
        lines.append("- 无")
    lines.extend(["", f"## 标记为潜在破坏性的变化（{len(breaking)}）", ""])
    for change in sorted(breaking, key=lambda row: row["entity_uid"]):
        uid = str(change["entity_uid"])
        label = str((v2_by_uid.get(uid) or v1_by_uid.get(uid) or {}).get("title") or uid)
        lines.append(f"- {_wiki(change_paths[uid], label)}")
    if not breaking:
        lines.append("- 机器差异未标记 breaking；仍需人工检查消息类型、ROS 名称和执行入口变化。")
    lines.extend(["", "## 扫描范围变化", ""])
    for change in inputs.diff.get("scope_changes") or []:
        lines.append(f"- `{_markdown_cell(change)}`")
    lines.extend(["", "## 比较限制", ""])
    for limitation in inputs.diff.get("comparison_limitations") or []:
        lines.append(
            f"- **`{limitation.get('limitation_id', '')}`**：{limitation.get('detail', '')}"
        )
    if not inputs.diff.get("comparison_limitations"):
        lines.append("- 无")
    lines.extend(
        [
            "",
            "## 放行条件",
            "",
            "- [ ] 复核全部抽取警告",
            "- [ ] 复核 V2 未匹配实体，不把范围变化误判为删除",
            "- [ ] 复核迁移/分解关系与新分层架构",
            "- [ ] 确认后再切换推荐快照指针",
            "",
            f"- {_wiki(diff_index, '返回差异总览')}",
        ]
    )
    return "\n".join(lines)


def _canvas_id(label: str) -> str:
    return hashlib.sha256(label.encode("utf-8")).hexdigest()[:16]


def _new_layer(package_name: str) -> str:
    if package_name == "agv_interfaces":
        return "接口契约层"
    if package_name in {"agv_perception", "agv_state_estimation"}:
        return "感知与状态估计层"
    if package_name in {"agv_decision", "agv_mission"}:
        return "任务与决策层"
    if package_name == "agv_safety":
        return "安全与仲裁层"
    if package_name == "agv_execution":
        return "执行网关层"
    return "集成、兼容与驱动层"


def _architecture_canvas(
    inputs: ProjectionInputs,
    *,
    entity_paths: Mapping[str, PurePosixPath],
    v1_by_uid: Mapping[str, dict],
    v2_by_uid: Mapping[str, dict],
) -> bytes:
    nodes: list[dict] = []
    edges: list[dict] = []

    def add_text(label: str, text: str, x: int, y: int, width: int, height: int, color: str) -> str:
        node_id = _canvas_id(label)
        nodes.append(
            {
                "id": node_id,
                "type": "text",
                "text": text,
                "x": x,
                "y": y,
                "width": width,
                "height": height,
                "color": color,
            }
        )
        return node_id

    def connect(label: str, source: str, target: str) -> None:
        edges.append(
            {
                "id": _canvas_id("edge:" + label),
                "fromNode": source,
                "fromSide": "bottom",
                "toNode": target,
                "toSide": "top",
                "label": label,
            }
        )

    baseline = str(inputs.manifest["baseline_snapshot"])
    target = str(inputs.manifest["snapshot_id"])
    root_id = add_text(
        "canvas-root",
        f"# V1 → V2 架构演化\n\n`{baseline}` → `{target}`\n\n左侧：显式分解/替换\n右侧：新增分层 Package",
        520,
        -320,
        520,
        220,
        "4",
    )

    grouped_migrations: dict[str, list[dict]] = defaultdict(list)
    for relation in inputs.migrations:
        grouped_migrations[str(relation["from_entity_uid"])].append(relation)
    y = 40
    for from_uid in sorted(grouped_migrations):
        rows = sorted(
            grouped_migrations[from_uid],
            key=lambda row: (row["predicate"], str(row.get("to_entity_uid") or "")),
        )
        source = v1_by_uid[from_uid]
        text_lines = [f"## {_v1_wiki(source)}", ""]
        for relation in rows:
            if relation.get("to_entity_uid") is None:
                text_lines.append(f"- `{relation['predicate']}` → **V2 无替代实例**")
            else:
                target_uid = str(relation["to_entity_uid"])
                target_entity = v2_by_uid[target_uid]
                text_lines.append(
                    f"- `{relation['predicate']}` → {_wiki(entity_paths[target_uid], str(target_entity.get('title') or target_uid))}"
                )
        height = max(170, 105 + 34 * len(rows))
        node_id = add_text(
            "migration:" + from_uid,
            "\n".join(text_lines),
            0,
            y,
            650,
            height,
            "2" if any(row["predicate"] == "replaced_by" for row in rows) else "3",
        )
        connect("迁移/分解", root_id, node_id)
        y += height + 50

    added_uids = {
        str(change["entity_uid"])
        for change in inputs.diff["entity_changes"]
        if change["change_kind"] == "added"
    }
    layer_packages: dict[str, list[dict]] = defaultdict(list)
    for entity in inputs.entities:
        uid = str(entity["entity_uid"])
        if entity["type"] != "ros_package" or uid not in added_uids:
            continue
        package_name = str(entity.get("title") or uid.rsplit(":", 1)[-1])
        layer_packages[_new_layer(package_name)].append(entity)
    layer_order = [
        "接口契约层",
        "感知与状态估计层",
        "任务与决策层",
        "安全与仲裁层",
        "执行网关层",
        "集成、兼容与驱动层",
    ]
    y = 40
    for layer in layer_order:
        packages = sorted(layer_packages.get(layer, []), key=lambda row: row["entity_uid"])
        if not packages:
            continue
        text_lines = [f"## {layer}", ""]
        for package in packages:
            uid = str(package["entity_uid"])
            text_lines.append(
                f"- {_wiki(entity_paths[uid], str(package.get('title') or uid))}"
            )
        height = max(160, 100 + 34 * len(packages))
        node_id = add_text(
            "layer:" + layer,
            "\n".join(text_lines),
            920,
            y,
            560,
            height,
            "5",
        )
        connect("新增分层", root_id, node_id)
        y += height + 50

    canvas = {
        "nodes": sorted(nodes, key=lambda row: row["id"]),
        "edges": sorted(edges, key=lambda row: row["id"]),
    }
    return (json.dumps(canvas, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode(
        "utf-8"
    )


def _history_index_page(
    inputs: ProjectionInputs,
    *,
    v1_note: PurePosixPath,
    snapshot_note: PurePosixPath,
    diff_index: PurePosixPath,
    current_note: PurePosixPath,
) -> str:
    baseline = str(inputs.manifest["baseline_snapshot"])
    target = str(inputs.manifest["snapshot_id"])
    created = str(inputs.manifest.get("created", ""))
    fields = [
        ("id", "agv:index:graph-history"),
        ("type", "index"),
        ("status", "active"),
        ("review", "verified"),
        ("candidate_status", "candidate_pending_review"),
        ("candidate_review", "generated"),
        ("project", "AGV"),
        ("updated", created),
        ("tags", ["AGV", "代码图谱", "快照", "差异"]),
    ]
    return "\n".join(
        [
            _frontmatter(fields),
            "# 代码图谱版本与差异",
            "",
            "## 当前指针",
            "",
            f"- 当前推荐：{_wiki(v1_note, baseline)}",
            f"- 待复核候选：{_wiki(snapshot_note, target)}",
            f"- 对比：{_wiki(diff_index, 'V1 → V2 差异总览')}",
            f"- 指针说明：{_wiki(current_note, '当前推荐快照')}",
            "",
            "V1 保持不可变；V2 使用独立快照实例页，不覆盖现有 `03_ROS` 页面。",
            "",
            "## 快照",
            "",
            "```dataview",
            "TABLE snapshot_id AS 快照, source_snapshot AS 源码哈希, status AS 状态",
            'FROM "00_System/Graph_History/Snapshots"',
            'WHERE type = "graph_snapshot"',
            "SORT file.name ASC",
            "```",
            "",
            "## 差异",
            "",
            "```dataview",
            "TABLE baseline_snapshot AS 基线, target_snapshot AS 目标, change_kind AS 类型, review AS 复核",
            'FROM "00_System/Graph_History/Changes"',
            'WHERE type = "graph_change"',
            "SORT file.name ASC",
            "```",
            "",
            "## 规范",
            "",
            "- [[图谱快照与差异Schema]]",
            "- [[../Decisions/ADR-002-代码图谱快照与增量差异]]",
            "",
            "- [[../../研发图谱工作台|返回研发图谱工作台]]",
        ]
    )


def _current_pointer(inputs: ProjectionInputs, *, diff_folder: PurePosixPath) -> bytes:
    baseline = str(inputs.manifest["baseline_snapshot"])
    target = str(inputs.manifest["snapshot_id"])
    value = {
        "candidate_snapshot": target,
        "candidate_snapshot_path": f"00_System/Graph_History/Snapshots/{target}",
        "comparison_path": diff_folder.as_posix(),
        "current_snapshot": baseline,
        "current_status": "active",
        "candidate_status": "candidate_pending_review",
        "candidate_review": "generated",
        "recommendation_status": "candidate_pending_review",
        "review": "verified",
        "snapshot_path": "00_System/Graph_History/Snapshots/code-v1",
        "updated": str(inputs.manifest.get("created", "")),
    }
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode(
        "utf-8"
    )


def _recommended_page(
    inputs: ProjectionInputs,
    *,
    v1_note: PurePosixPath,
    snapshot_note: PurePosixPath,
    diff_index: PurePosixPath,
) -> str:
    baseline = str(inputs.manifest["baseline_snapshot"])
    target = str(inputs.manifest["snapshot_id"])
    created = str(inputs.manifest.get("created", ""))
    fields = [
        ("id", "agv:graph-snapshot-pointer:current"),
        ("type", "index"),
        ("status", "active"),
        ("review", "verified"),
        ("candidate_status", "candidate_pending_review"),
        ("candidate_review", "generated"),
        ("project", "AGV"),
        ("current_snapshot", baseline),
        ("candidate_snapshot", target),
        ("updated", created),
        ("tags", ["AGV", "代码图谱", "当前版本"]),
    ]
    return "\n".join(
        [
            _frontmatter(fields),
            "# 当前推荐代码图谱快照",
            "",
            f"当前推荐仍为 {_wiki(v1_note, baseline)}。",
            "",
            f"候选快照为 {_wiki(snapshot_note, target)}；对应 {_wiki(diff_index, 'V1 → V2 差异总览')}。",
            "",
            "完成风险页的人工复核前，候选快照不会覆盖 V1，也不会把 `03_ROS` 页面改写成 V2。",
        ]
    )


def _updated_workbench(
    source_text: str,
    *,
    snapshot_note: PurePosixPath,
    diff_index: PurePosixPath,
    risk_summary: PurePosixPath,
    target: str,
) -> str:
    begin = "<!-- BEGIN CODE-V2-PROJECTION -->"
    end = "<!-- END CODE-V2-PROJECTION -->"
    block = "\n".join(
        [
            begin,
            "## 代码图谱 V2 候选",
            "",
            f"- 候选快照：{_wiki(snapshot_note, target)}",
            f"- 增量对比：{_wiki(diff_index, 'V1 → V2 差异总览')}",
            f"- 风险队列：{_wiki(risk_summary, '风险与复核')}",
            "- 原 V1 代码图谱与 `03_ROS` 页面保持不变。",
            end,
        ]
    )
    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.DOTALL)
    if pattern.search(source_text):
        return pattern.sub(block, source_text).rstrip() + "\n"
    return source_text.rstrip() + "\n\n" + block + "\n"


def _change_group_index(
    *,
    kind: str,
    changes: Sequence[dict],
    change_paths: Mapping[str, PurePosixPath],
    diff_index: PurePosixPath,
    created: str,
) -> str:
    labels = {"added": "新增实体", "modified": "语义变化实体", "removed": "V2 未匹配实体"}
    fields = [
        ("id", f"agv:graph-change-index:{kind}"),
        ("type", "index"),
        ("change_kind", kind),
        ("change_count", len(changes)),
        ("status", "candidate"),
        ("review", "generated"),
        ("updated", created),
        ("tags", ["AGV", "代码图谱", "实体差异", kind]),
    ]
    lines = [_frontmatter(fields), f"# {labels[kind]}", ""]
    for change in sorted(changes, key=lambda row: row["entity_uid"]):
        uid = str(change["entity_uid"])
        lines.append(f"- {_wiki(change_paths[uid], uid)}")
    if not changes:
        lines.append("- 无")
    lines.extend(["", f"- {_wiki(diff_index, '返回差异总览')}"])
    return "\n".join(lines)


def _render_projection(vault_out: Path, inputs: ProjectionInputs, source_vault: Path) -> None:
    manifest = inputs.manifest
    snapshot_id = str(manifest["snapshot_id"])
    baseline = str(manifest["baseline_snapshot"])
    created = str(manifest.get("created", ""))
    history = _vault_path("00_System", "Graph_History")
    v1_root = history / "Snapshots" / "code-v1"
    v1_note = v1_root / "V1基线说明.md"
    v2_root = history / "Snapshots" / snapshot_id
    snapshot_note = v2_root / "V2快照说明.md"
    diff_root = history / "Changes" / f"{baseline}__{snapshot_id}"
    diff_index = diff_root / "_index.md"
    entity_summary = diff_root / "实体差异.md"
    relation_summary = diff_root / "关系差异.md"
    migration_summary = diff_root / "迁移与分解.md"
    risk_summary = diff_root / "风险与复核.md"
    canvas_path = diff_root / "V1→V2架构演化.canvas"
    current_note = history / "当前推荐快照.md"

    for relative, data in sorted(inputs.v1_bytes.items()):
        _write_bytes(vault_out, v1_root / PurePosixPath(relative), data)
    for relative, data in sorted(inputs.machine_bytes.items()):
        _write_bytes(vault_out, v2_root / "Machine" / PurePosixPath(relative), data)

    entity_paths = _entity_paths(inputs.entities, snapshot_id)
    changes = tuple(inputs.diff["entity_changes"])
    change_paths = _change_paths(changes, baseline, snapshot_id)
    v1_by_uid = {str(row["entity_uid"]): row for row in inputs.v1_entities}
    v2_by_uid = {str(row["entity_uid"]): row for row in inputs.entities}
    change_by_uid = {str(row["entity_uid"]): row for row in changes}
    outgoing: dict[str, list[dict]] = defaultdict(list)
    incoming: dict[str, list[dict]] = defaultdict(list)
    for relation in inputs.relations:
        outgoing[str(relation["from_entity_uid"])].append(relation)
        incoming[str(relation["to_entity_uid"])].append(relation)

    group_indexes: dict[str, PurePosixPath] = {}
    for entity_type, group in ENTITY_GROUPS.items():
        group_index = v2_root / "Entities" / group / "_index.md"
        group_indexes[group] = group_index
        rows = [row for row in inputs.entities if row["type"] == entity_type]
        _write_text(
            vault_out,
            group_index,
            _group_index_page(
                title=f"V2 {group}",
                group=group,
                snapshot_id=snapshot_id,
                snapshot_note=snapshot_note,
                entities=rows,
                entity_paths=entity_paths,
                created=created,
            ),
        )
    for entity in sorted(inputs.entities, key=lambda row: row["entity_uid"]):
        uid = str(entity["entity_uid"])
        _write_text(
            vault_out,
            entity_paths[uid],
            _entity_page(
                entity,
                snapshot_id=snapshot_id,
                snapshot_note=snapshot_note,
                entity_paths=entity_paths,
                change_paths=change_paths,
                change_by_uid=change_by_uid,
                outgoing=outgoing,
                incoming=incoming,
                created=created,
            ),
        )

    for change in sorted(changes, key=lambda row: row["entity_uid"]):
        uid = str(change["entity_uid"])
        _write_text(
            vault_out,
            change_paths[uid],
            _change_page(
                change,
                baseline=baseline,
                target=snapshot_id,
                diff_index=diff_index,
                entity_paths=entity_paths,
                v1_by_uid=v1_by_uid,
                v2_by_uid=v2_by_uid,
                created=created,
            ),
        )
    for kind, folder in CHANGE_GROUPS.items():
        rows = [
            row
            for row in changes
            if _change_category(str(row["change_kind"])) == kind
        ]
        _write_text(
            vault_out,
            diff_root / "Entities" / folder / "_index.md",
            _change_group_index(
                kind=kind,
                changes=rows,
                change_paths=change_paths,
                diff_index=diff_index,
                created=created,
            ),
        )

    _write_text(
        vault_out,
        snapshot_note,
        _snapshot_note_page(
            inputs,
            snapshot_note=snapshot_note,
            diff_index=diff_index,
            group_indexes=group_indexes,
        ),
    )
    _write_text(
        vault_out,
        diff_index,
        _diff_index_page(
            inputs,
            snapshot_note=snapshot_note,
            v1_note=v1_note,
            entity_summary=entity_summary,
            relation_summary=relation_summary,
            migration_summary=migration_summary,
            risk_summary=risk_summary,
            canvas_path=canvas_path,
        ),
    )
    _write_text(
        vault_out,
        entity_summary,
        _entity_diff_summary_page(
            inputs,
            diff_index=diff_index,
            change_paths=change_paths,
            v1_by_uid=v1_by_uid,
            v2_by_uid=v2_by_uid,
        ),
    )
    _write_text(
        vault_out,
        relation_summary,
        _relation_diff_page(inputs, diff_index=diff_index, v1_by_uid=v1_by_uid),
    )
    _write_text(
        vault_out,
        migration_summary,
        _migration_page(
            inputs,
            diff_index=diff_index,
            entity_paths=entity_paths,
            v1_by_uid=v1_by_uid,
            v2_by_uid=v2_by_uid,
        ),
    )
    _write_text(
        vault_out,
        risk_summary,
        _risk_page(
            inputs,
            diff_index=diff_index,
            change_paths=change_paths,
            v1_by_uid=v1_by_uid,
            v2_by_uid=v2_by_uid,
        ),
    )
    _write_bytes(
        vault_out,
        canvas_path,
        _architecture_canvas(
            inputs,
            entity_paths=entity_paths,
            v1_by_uid=v1_by_uid,
            v2_by_uid=v2_by_uid,
        ),
    )
    _write_text(
        vault_out,
        history / "_index.md",
        _history_index_page(
            inputs,
            v1_note=v1_note,
            snapshot_note=snapshot_note,
            diff_index=diff_index,
            current_note=current_note,
        ),
    )
    _write_bytes(vault_out, history / "current.json", _current_pointer(inputs, diff_folder=diff_root))
    _write_text(
        vault_out,
        current_note,
        _recommended_page(
            inputs,
            v1_note=v1_note,
            snapshot_note=snapshot_note,
            diff_index=diff_index,
        ),
    )
    workbench_source = source_vault / "研发图谱工作台.md"
    if workbench_source.is_file():
        try:
            source_text = workbench_source.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            raise ProjectionError(f"workbench is not UTF-8: {workbench_source}") from exc
    else:
        source_text = "# 研发图谱工作台\n"
    _write_text(
        vault_out,
        _vault_path("研发图谱工作台.md"),
        _updated_workbench(
            source_text,
            snapshot_note=snapshot_note,
            diff_index=diff_index,
            risk_summary=risk_summary,
            target=snapshot_id,
        ),
    )


def _normalize_relative(path: PurePosixPath) -> PurePosixPath | None:
    parts: list[str] = []
    for part in path.parts:
        if part in {"", ".", "/"}:
            continue
        if part == "..":
            if not parts:
                return None
            parts.pop()
        else:
            parts.append(part)
    return PurePosixPath(*parts)


def _all_union_files(vault_out: Path, source_vault: Path) -> set[str]:
    files: set[str] = set()
    for root in (source_vault, vault_out):
        if not root.is_dir():
            continue
        for path in root.rglob("*"):
            if path.is_file() and ".obsidian" not in path.relative_to(root).parts:
                files.add(path.relative_to(root).as_posix())
    return files


def _wikilink_resolves(
    raw_target: str,
    *,
    document: PurePosixPath,
    union_files: set[str],
) -> bool:
    target = raw_target.split("|", 1)[0].split("#", 1)[0].split("^", 1)[0].strip()
    if not target:
        return True
    target = target.replace("\\", "/").lstrip("/")
    target_path = PurePosixPath(target)
    candidates: list[PurePosixPath] = []
    if raw_target.split("|", 1)[0].strip().startswith(("./", "../")):
        normalized = _normalize_relative(document.parent / target_path)
        if normalized is not None:
            candidates.append(normalized)
    else:
        normalized = _normalize_relative(target_path)
        if normalized is not None:
            candidates.append(normalized)
    expanded: set[str] = set()
    for candidate in candidates:
        expanded.add(candidate.as_posix())
        if not candidate.suffix:
            expanded.add(candidate.with_suffix(".md").as_posix())
            expanded.add(candidate.with_suffix(".canvas").as_posix())
    if expanded & union_files:
        return True
    if "/" not in target:
        target_name = PurePosixPath(target).name.casefold()
        for relative in union_files:
            path = PurePosixPath(relative)
            if path.name.casefold() == target_name:
                return True
            if not PurePosixPath(target).suffix and path.stem.casefold() == target_name:
                return True
    return False


def _canvas_link_failures(
    path: Path,
    *,
    vault_out: Path,
    union_files: set[str],
) -> list[str]:
    document = path.relative_to(vault_out).as_posix()
    try:
        canvas = json.loads(
            _decode_utf8_without_replacement(path.read_bytes(), document)
        )
    except (ProjectionError, json.JSONDecodeError) as exc:
        return [f"{document}: invalid canvas JSON: {exc}"]
    if not isinstance(canvas, dict):
        return [f"{document}: canvas root is not an object"]
    nodes = canvas.get("nodes") or []
    edges = canvas.get("edges") or []
    node_ids = [str(node.get("id", "")) for node in nodes if isinstance(node, dict)]
    failures: list[str] = []
    if len(nodes) != len(node_ids) or any(not node_id for node_id in node_ids):
        failures.append(f"{document}: node without id")
    if len(node_ids) != len(set(node_ids)):
        failures.append(f"{document}: duplicate node id")
    node_id_set = set(node_ids)
    for node in nodes:
        if not isinstance(node, dict) or node.get("type") != "file":
            continue
        raw_file = str(node.get("file", "")).replace("\\", "/").lstrip("/")
        normalized = _normalize_relative(PurePosixPath(raw_file))
        if normalized is None or normalized.as_posix() not in union_files:
            failures.append(
                f"{document}: file node {node.get('id', '')} -> {raw_file or '<empty>'}"
            )
    for edge in edges:
        if not isinstance(edge, dict):
            failures.append(f"{document}: non-object edge")
            continue
        for field in ("fromNode", "toNode"):
            if str(edge.get(field, "")) not in node_id_set:
                failures.append(
                    f"{document}: edge {edge.get('id', '')} has missing {field}={edge.get(field, '')}"
                )
    return failures


def validate_projection(
    machine_dir: Path,
    v1_dir: Path,
    source_vault: Path,
    vault_out: Path,
) -> dict:
    inputs = load_inputs(machine_dir, v1_dir)
    snapshot_id = str(inputs.manifest["snapshot_id"])
    baseline = str(inputs.manifest["baseline_snapshot"])
    v2_root = vault_out / "00_System" / "Graph_History" / "Snapshots" / snapshot_id
    v1_root = vault_out / "00_System" / "Graph_History" / "Snapshots" / "code-v1"
    diff_root = vault_out / "00_System" / "Graph_History" / "Changes" / f"{baseline}__{snapshot_id}"
    expected_entity_paths = _entity_paths(inputs.entities, snapshot_id)
    expected_change_paths = _change_paths(inputs.diff["entity_changes"], baseline, snapshot_id)

    byte_mismatches: list[str] = []
    for relative, data in sorted(inputs.v1_bytes.items()):
        target = _disk_path(v1_root, PurePosixPath(relative))
        if not target.is_file() or target.read_bytes() != data:
            byte_mismatches.append(f"V1/{relative}")
    for relative, data in sorted(inputs.machine_bytes.items()):
        target = _disk_path(v2_root / "Machine", PurePosixPath(relative))
        if not target.is_file() or target.read_bytes() != data:
            byte_mismatches.append(f"V2/Machine/{relative}")

    all_paths = [path.relative_to(vault_out).as_posix() for path in vault_out.rglob("*") if path.is_file()]
    folded = Counter(path.casefold() for path in all_paths)
    collisions = sorted(path for path, count in folded.items() if count > 1)
    obsidian_paths = sorted(path for path in all_paths if ".obsidian" in PurePosixPath(path).parts)
    missing_entity_pages = sorted(
        relative.as_posix()
        for relative in expected_entity_paths.values()
        if not _disk_path(vault_out, relative).is_file()
    )
    missing_change_pages = sorted(
        relative.as_posix()
        for relative in expected_change_paths.values()
        if not _disk_path(vault_out, relative).is_file()
    )

    union_files = _all_union_files(vault_out, source_vault)
    broken_wikilinks: list[str] = []
    broken_canvas_links: list[str] = []
    for path in sorted(vault_out.rglob("*"), key=lambda item: item.as_posix()):
        if not path.is_file() or path.suffix.lower() not in {".md", ".canvas"}:
            continue
        if path.suffix.lower() == ".canvas":
            broken_canvas_links.extend(
                _canvas_link_failures(
                    path,
                    vault_out=vault_out,
                    union_files=union_files,
                )
            )
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        document = PurePosixPath(path.relative_to(vault_out).as_posix())
        for raw_target in WIKILINK.findall(text):
            if not _wikilink_resolves(raw_target, document=document, union_files=union_files):
                broken_wikilinks.append(f"{document.as_posix()} -> [[{raw_target}]]")

    entity_uids = {str(row["entity_uid"]) for row in inputs.entities}
    v1_uids = {str(row["entity_uid"]) for row in inputs.v1_entities}
    broken_relations = sorted(
        json.dumps(row, ensure_ascii=False, sort_keys=True)
        for row in inputs.relations
        if row.get("from_entity_uid") not in entity_uids or row.get("to_entity_uid") not in entity_uids
    )
    broken_migrations = sorted(
        json.dumps(row, ensure_ascii=False, sort_keys=True)
        for row in inputs.migrations
        if row.get("from_entity_uid") not in v1_uids
        or (
            row.get("to_entity_uid") is not None
            and row.get("to_entity_uid") not in entity_uids
        )
    )
    report = {
        "broken_canvas_links": sorted(set(broken_canvas_links)),
        "broken_relation_endpoints": broken_relations,
        "broken_migration_endpoints": broken_migrations,
        "broken_wikilinks": sorted(set(broken_wikilinks)),
        "byte_copy_mismatches": byte_mismatches,
        "change_pages": len(expected_change_paths) - len(missing_change_pages),
        "entity_pages": len(expected_entity_paths) - len(missing_entity_pages),
        "missing_change_pages": missing_change_pages,
        "missing_entity_pages": missing_entity_pages,
        "path_collisions": collisions,
        "unexpected_obsidian_paths": obsidian_paths,
    }
    return report


def _assert_projection_report(report: Mapping[str, object], inputs: ProjectionInputs) -> None:
    list_failures = [
        "broken_canvas_links",
        "broken_relation_endpoints",
        "broken_migration_endpoints",
        "broken_wikilinks",
        "byte_copy_mismatches",
        "missing_change_pages",
        "missing_entity_pages",
        "path_collisions",
        "unexpected_obsidian_paths",
    ]
    for key in list_failures:
        if report.get(key):
            raise ProjectionError(f"projection validation failed ({key}): {report[key]!r}")
    _require_equal(report.get("entity_pages"), len(inputs.entities), "projected entity page count")
    _require_equal(
        report.get("change_pages"),
        len(inputs.diff.get("entity_changes") or []),
        "projected change page count",
    )


def _safe_output_dir(output_dir: Path) -> Path:
    resolved = output_dir.resolve()
    workspace = WORKSPACE_ROOT.resolve()
    try:
        resolved.relative_to(workspace)
    except ValueError as exc:
        raise ProjectionError(f"output must remain under workspace: {resolved}") from exc
    if resolved == workspace or resolved == PROJECT_DIR.resolve():
        raise ProjectionError(f"refusing broad output directory: {resolved}")
    return resolved


def _paths_overlap(left: Path, right: Path) -> bool:
    left = left.resolve()
    right = right.resolve()
    try:
        left.relative_to(right)
        return True
    except ValueError:
        pass
    try:
        right.relative_to(left)
        return True
    except ValueError:
        return False


def _reject_output_input_overlap(
    output_dir: Path,
    *,
    machine_dir: Path,
    v1_dir: Path,
    source_vault: Path,
) -> None:
    inputs = {
        "machine_dir": machine_dir.resolve(),
        "v1_dir": v1_dir.resolve(),
        "source_vault": source_vault.resolve(),
    }
    candidates = {
        "output_dir": output_dir.resolve(),
        "temporary_output_dir": (output_dir.parent / f".{output_dir.name}.staging").resolve(),
    }
    for output_label, candidate in candidates.items():
        for input_label, input_root in inputs.items():
            if _paths_overlap(candidate, input_root):
                raise ProjectionError(
                    f"{output_label} overlaps {input_label}: {candidate} <-> {input_root}"
                )


def build_projection(
    machine_dir: Path,
    v1_dir: Path,
    source_vault: Path,
    output_dir: Path,
) -> ProjectionResult:
    machine_dir = Path(machine_dir).resolve()
    v1_dir = Path(v1_dir).resolve()
    source_vault = Path(source_vault).resolve()
    output_dir = _safe_output_dir(Path(output_dir))
    _reject_output_input_overlap(
        output_dir,
        machine_dir=machine_dir,
        v1_dir=v1_dir,
        source_vault=source_vault,
    )
    inputs = load_inputs(machine_dir, v1_dir)
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    temporary = output_dir.parent / f".{output_dir.name}.staging"
    if temporary.exists():
        shutil.rmtree(temporary)
    temporary.mkdir()
    vault_out = temporary / "AGV_Knowledge_Base"
    try:
        vault_out.mkdir(parents=True)
        _render_projection(vault_out, inputs, source_vault)
        report = validate_projection(
            Path(machine_dir), Path(v1_dir), source_vault, vault_out
        )
        _assert_projection_report(report, inputs)
        if output_dir.exists():
            if output_dir.is_dir():
                shutil.rmtree(output_dir)
            else:
                output_dir.unlink()
        shutil.copytree(temporary, output_dir)
        shutil.rmtree(temporary)
    except Exception:
        if temporary.exists():
            shutil.rmtree(temporary, ignore_errors=True)
        raise

    final_vault = output_dir / "AGV_Knowledge_Base"
    return ProjectionResult(
        vault_root=final_vault,
        snapshot_id=str(inputs.manifest["snapshot_id"]),
        baseline_snapshot=str(inputs.manifest["baseline_snapshot"]),
        entity_page_count=len(inputs.entities),
        change_page_count=len(inputs.diff.get("entity_changes") or []),
        tree_sha256=tree_fingerprint(final_vault),
    )


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a deterministic Obsidian projection for the V2 code graph."
    )
    parser.add_argument("--machine-dir", type=Path, default=DEFAULT_MACHINE_DIR)
    parser.add_argument("--v1-dir", type=Path, default=DEFAULT_V1_DIR)
    parser.add_argument("--vault-dir", type=Path, default=DEFAULT_VAULT_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    result = build_projection(
        args.machine_dir, args.v1_dir, args.vault_dir, args.output_dir
    )
    report = validate_projection(
        args.machine_dir, args.v1_dir, args.vault_dir, result.vault_root
    )
    print(
        json.dumps(
            {
                "baseline_snapshot": result.baseline_snapshot,
                "change_pages": result.change_page_count,
                "entity_pages": result.entity_page_count,
                "output": str(result.vault_root),
                "snapshot_id": result.snapshot_id,
                "tree_sha256": result.tree_sha256,
                "validation": report,
            },
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
