from __future__ import annotations

import hashlib
import json
import shutil
import sys
import unittest
from contextlib import contextmanager
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = PROJECT_DIR.parents[1]
sys.path.insert(0, str(PROJECT_DIR))

from generate_obsidian_projection import (  # noqa: E402
    ProjectionError,
    build_projection,
    tree_fingerprint,
    validate_projection,
)


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode(
        "utf-8"
    )


def jsonl_bytes(rows: list[dict]) -> bytes:
    return b"".join(
        (
            json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            + "\n"
        ).encode("utf-8")
        for row in rows
    )


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def semantic(
    entity_type: str,
    *,
    ros_name: str = "",
    interface_kind: str = "",
    message_type: str = "",
    executable: str = "",
    status: str = "active",
) -> dict:
    return {
        "executable": executable,
        "interface_kind": interface_kind,
        "message_type": message_type,
        "ros_name": ros_name,
        "status": status,
        "type": entity_type,
        "vehicles": ["三号车"],
        "version": "1.0.0",
    }


def entity(
    uid: str,
    entity_type: str,
    title: str,
    fingerprint: str,
    *,
    path: str,
    package_uid: str | None = None,
    semantic_value: dict | None = None,
) -> dict:
    value = {
        "comparison_scope": "code",
        "entity_uid": uid,
        "evidence": [],
        "evidence_fingerprint": "evidence-" + fingerprint,
        "path": path,
        "relation_fingerprint": "relations-" + fingerprint,
        "review": "generated",
        "semantic": semantic_value or semantic(entity_type),
        "semantic_fingerprint": fingerprint,
        "source_scope": "fixture",
        "source_snapshot": "fixture-source",
        "status": "active",
        "title": title,
        "type": entity_type,
    }
    if package_uid:
        value["package_uid"] = package_uid
    return value


def write_fixture(root: Path) -> tuple[Path, Path, Path]:
    machine = root / "machine"
    v1 = root / "v1"
    vault = root / "vault"
    machine.mkdir(parents=True)
    v1.mkdir(parents=True)
    (vault / "03_ROS" / "Packages").mkdir(parents=True)
    (vault / "03_ROS" / "Nodes").mkdir(parents=True)
    (vault / "03_ROS" / "Packages" / "core.md").write_text(
        "# core V1\n", encoding="utf-8"
    )
    (vault / "03_ROS" / "Nodes" / "legacy.md").write_text(
        "# legacy V1\n", encoding="utf-8"
    )
    (vault / "研发图谱工作台.md").write_text(
        "# 研发图谱工作台\n\n既有内容。\n", encoding="utf-8"
    )
    (vault / "00_System" / "Graph_History").mkdir(parents=True)
    (vault / "00_System" / "Decisions").mkdir(parents=True)
    (vault / "00_System" / "Graph_History" / "图谱快照与差异Schema.md").write_text(
        "# 图谱快照与差异 Schema\n", encoding="utf-8"
    )
    (
        vault
        / "00_System"
        / "Decisions"
        / "ADR-002-代码图谱快照与增量差异.md"
    ).write_text("# ADR-002\n", encoding="utf-8")

    baseline_snapshot = "code-v1-fixture"
    target_snapshot = "code-v2-fixture"
    core_uid = "agv:ros:package:core"
    legacy_uid = "agv:ros:node:legacy"
    new_uid = "agv:ros:node:new-controller"
    topic_uid = "agv:ros:interface:motion-command"

    v1_entities = [
        {
            **entity(
                core_uid,
                "ros_package",
                "core",
                "same-core",
                path="03_ROS/Packages/core.md",
            ),
            "vault_blob_oid": "fixture-core",
        },
        {
            **entity(
                legacy_uid,
                "ros_node",
                "legacy",
                "old-node",
                path="03_ROS/Nodes/legacy.md",
                package_uid=core_uid,
                semantic_value=semantic(
                    "ros_node", ros_name="/legacy", executable="legacy_node"
                ),
            ),
            "vault_blob_oid": "fixture-legacy",
        },
    ]
    v1_relations = [
        {
            "from_entity_uid": legacy_uid,
            "predicate": "package",
            "qualifiers": {},
            "to_entity_uid": core_uid,
        }
    ]
    v1_files = {
        "entities.jsonl": jsonl_bytes(v1_entities),
        "relations.jsonl": jsonl_bytes(v1_relations),
        "source-sets.jsonl": jsonl_bytes(
            [{"scope": "fixture", "sha256": "fixture-source-set"}]
        ),
        "V1基线说明.md": (
            "---\n"
            f'id: "agv:graph-snapshot:{baseline_snapshot}"\n'
            "type: graph_snapshot\n"
            f'snapshot_id: "{baseline_snapshot}"\n'
            "---\n\n# V1 fixture baseline\n"
        ).encode("utf-8"),
    }
    v1_manifest = {
        "entity_count": len(v1_entities),
        "entities_sha256": sha256(v1_files["entities.jsonl"]),
        "graph_schema_version": 2,
        "graph_version": "v1",
        "immutable": True,
        "relations_sha256": sha256(v1_files["relations.jsonl"]),
        "scope_id": "fixture-v1",
        "semantic_relation_count": len(v1_relations),
        "snapshot_id": baseline_snapshot,
        "source_sets_sha256": sha256(v1_files["source-sets.jsonl"]),
    }
    v1_files["manifest.json"] = json_bytes(v1_manifest)
    for name, data in v1_files.items():
        (v1 / name).write_bytes(data)

    v2_entities = [
        entity(
            core_uid,
            "ros_package",
            "core",
            "same-core",
            path="src/core/package.xml",
        ),
        entity(
            new_uid,
            "ros_node",
            "new-controller",
            "new-node",
            path="src/core/src/new_controller.cpp",
            package_uid=core_uid,
            semantic_value=semantic(
                "ros_node", ros_name="/new_controller", executable="new_controller"
            ),
        ),
        entity(
            topic_uid,
            "ros_interface",
            "/motion/command",
            "new-topic",
            path="src/core/src/new_controller.cpp",
            semantic_value=semantic(
                "ros_interface",
                ros_name="/motion/command",
                interface_kind="topic",
                message_type="geometry_msgs/Twist",
            ),
        ),
    ]
    v2_relations = [
        {
            "from_entity_uid": new_uid,
            "predicate": "package",
            "qualifiers": {},
            "to_entity_uid": core_uid,
        },
        {
            "from_entity_uid": new_uid,
            "predicate": "publishes",
            "qualifiers": {},
            "to_entity_uid": topic_uid,
        },
    ]
    migrations = [
        {
            "confidence": 1.0,
            "evidence": {"fixture": True},
            "from_entity_uid": legacy_uid,
            "from_snapshot": baseline_snapshot,
            "match_method": "fixture",
            "predicate": "replaced_by",
            "to_entity_uid": new_uid,
            "to_snapshot": target_snapshot,
        }
    ]
    changes = [
        {
            "after_fingerprint": "new-node",
            "before_fingerprint": "",
            "breaking": False,
            "change_kind": "added",
            "changed_fields": [],
            "entity_uid": new_uid,
            "match_confidence": 1.0,
            "match_method": "target_only",
            "review": "generated",
        },
        {
            "after_fingerprint": "new-topic",
            "before_fingerprint": "",
            "breaking": False,
            "change_kind": "added",
            "changed_fields": [],
            "entity_uid": topic_uid,
            "match_confidence": 1.0,
            "match_method": "target_only",
            "review": "generated",
        },
        {
            "after_fingerprint": "",
            "before_fingerprint": "old-node",
            "breaking": False,
            "change_kind": "removed",
            "changed_fields": [],
            "entity_uid": legacy_uid,
            "match_confidence": 1.0,
            "match_method": "baseline_only",
            "review": "generated",
        },
    ]
    comparison_limitations = [
        {
            "detail": "Fixture semantic equality does not prove source equality.",
            "limitation_id": "fixture-semantic-only",
        }
    ]
    fixture_risks = [
        {
            "breaking": False,
            "evidence": [
                {
                    "file_sha256": "fixture-evidence",
                    "line": 1,
                    "path": "src/core/package.xml",
                    "scope": "source",
                }
            ],
            "independent_tests_run": False,
            "review": "needs-review",
            "risk_id": "R99",
            "risk_kind": "fixture_risk",
            "severity": "medium",
            "statement": "Fixture risk statement.",
            "validation_state": "static_evidence_only",
        }
    ]
    removed_relations = [
        {
            **v1_relations[0],
            "breaking": False,
            "comparison_classification": "extraction_limited",
            "review": "needs-review",
        }
    ]
    diff = {
        "baseline_snapshot": baseline_snapshot,
        "comparison_limitations": comparison_limitations,
        "comparison_scope": {
            "baseline_filter": "fixture",
            "baseline_source_file_manifest_available": False,
            "target_filter": "fixture",
        },
        "entity_changes": changes,
        "entity_counts": {
            "added": 2,
            "baseline": 2,
            "matched": 1,
            "modified": 0,
            "removed": 1,
            "target": 3,
            "unchanged": 1,
        },
        "migration_relation_count": 1,
        "relation_added": v2_relations,
        "relation_counts": {"added": 2, "baseline": 1, "removed": 1, "target": 2},
        "relation_removed": removed_relations,
        "risk_count": len(fixture_risks),
        "risks": fixture_risks,
        "scope_changes": [
            {
                "change_kind": "baseline_manifest_limitation",
                "classification": "scope_change",
                "detail": "Fixture V1 has no per-file source manifest.",
            }
        ],
        "target_snapshot": target_snapshot,
    }
    machine_files = {
        "entities.jsonl": jsonl_bytes(v2_entities),
        "relations.jsonl": jsonl_bytes(v2_relations),
        "migration-relations.jsonl": jsonl_bytes(migrations),
        "source-files.jsonl": jsonl_bytes(
            [{"path": "src/core/package.xml", "sha256": "fixture-file"}]
        ),
        "extraction-warnings.jsonl": jsonl_bytes(
            [{"kind": "fixture_warning", "path": "src/core/package.xml"}]
        ),
        "v1-to-v2-diff.json": json_bytes(diff),
        "V1-to-V2差异摘要.md": b"# Fixture V1 to V2 summary\n",
    }
    for name, data in machine_files.items():
        (machine / name).write_bytes(data)
    manifest = {
        "artifact_sha256": {name: sha256(data) for name, data in machine_files.items()},
        "baseline_manifest_limitation": "Fixture limitation.",
        "baseline_snapshot": baseline_snapshot,
        "comparison_limitations": comparison_limitations,
        "created": "2026-07-14",
        "entity_count": len(v2_entities),
        "entity_type_counts": {
            "ros_interface": 1,
            "ros_node": 1,
            "ros_package": 1,
        },
        "excluded_source_file_count": 0,
        "extractor_version": "fixture-1",
        "git_state": {"dirty": True, "head": "fixture-head"},
        "graph_schema_version": 2,
        "graph_version": "v2",
        "immutable": True,
        "included_source_file_count": 1,
        "interface_kind_counts": {"topic": 1},
        "migration_relation_count": len(migrations),
        "risk_count": len(fixture_risks),
        "scope_id": "fixture-v2",
        "semantic_relation_count": len(v2_relations),
        "snapshot_fingerprint": "fixture-snapshot",
        "snapshot_id": target_snapshot,
        "source_file_count": 1,
        "source_file_manifest_available": True,
        "source_fingerprint": "fixture-source",
        "source_kind": "working_tree",
        "source_locator": "D:/fixture",
        "warning_count": 1,
    }
    (machine / "manifest.json").write_bytes(json_bytes(manifest))
    return machine, v1, vault


class ProjectionGeneratorTests(unittest.TestCase):
    @contextmanager
    def make_temp(self):
        path = PROJECT_DIR / "_test_runs" / self._testMethodName
        if path.exists():
            shutil.rmtree(path)
        path.mkdir(parents=True)
        try:
            yield str(path)
        finally:
            if path.exists():
                shutil.rmtree(path)

    def test_builds_dynamic_projection_and_preserves_input_bytes(self) -> None:
        with self.make_temp() as temp_name:
            temp = Path(temp_name)
            machine, v1, vault = write_fixture(temp)
            result = build_projection(machine, v1, vault, temp / "projection")

            self.assertEqual(result.snapshot_id, "code-v2-fixture")
            self.assertEqual(result.entity_page_count, 3)
            self.assertEqual(result.change_page_count, 3)

            v2_root = (
                result.vault_root
                / "00_System"
                / "Graph_History"
                / "Snapshots"
                / result.snapshot_id
            )
            self.assertEqual(
                len(list((v2_root / "Entities" / "Packages").glob("*.md"))) - 1, 1
            )
            self.assertEqual(
                len(list((v2_root / "Entities" / "Nodes").glob("*.md"))) - 1, 1
            )
            self.assertEqual(
                len(list((v2_root / "Entities" / "Interfaces").glob("*.md"))) - 1,
                1,
            )

            entity_pages = [
                path
                for path in (v2_root / "Entities").rglob("*.md")
                if path.name != "_index.md"
            ]
            page_text = entity_pages[0].read_text(encoding="utf-8")
            self.assertIn("logical_entity_uid:", page_text)
            self.assertIn("snapshot_instance_id:", page_text)

            for source in sorted(v1.rglob("*")):
                if source.is_file():
                    copied = (
                        result.vault_root
                        / "00_System"
                        / "Graph_History"
                        / "Snapshots"
                        / "code-v1"
                        / source.relative_to(v1)
                    )
                    self.assertEqual(copied.read_bytes(), source.read_bytes())
            for source in sorted(machine.iterdir()):
                if source.is_file():
                    self.assertEqual(
                        (v2_root / "Machine" / source.name).read_bytes(),
                        source.read_bytes(),
                    )

            current = json.loads(
                (
                    result.vault_root
                    / "00_System"
                    / "Graph_History"
                    / "current.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(current["current_snapshot"], "code-v1-fixture")
            self.assertEqual(current["candidate_snapshot"], "code-v2-fixture")
            self.assertEqual(current["review"], "verified")
            self.assertEqual(current["current_status"], "active")
            self.assertEqual(current["candidate_review"], "generated")
            self.assertEqual(current["candidate_status"], "candidate_pending_review")
            self.assertFalse(any(path.name == ".obsidian" for path in result.vault_root.rglob("*")))

            history_root = result.vault_root / "00_System" / "Graph_History"
            history_index = (history_root / "_index.md").read_text(encoding="utf-8")
            recommended = (history_root / "当前推荐快照.md").read_text(encoding="utf-8")
            self.assertEqual(history_index.count("```dataview"), 2)
            self.assertIn("[[图谱快照与差异Schema]]", history_index)
            self.assertIn("[[../Decisions/ADR-002-代码图谱快照与增量差异]]", history_index)
            self.assertIn("[[../../研发图谱工作台|返回研发图谱工作台]]", history_index)
            self.assertIn('review: "verified"', recommended)
            self.assertIn('candidate_review: "generated"', recommended)
            self.assertIn('candidate_status: "candidate_pending_review"', recommended)

            diff_root = (
                result.vault_root
                / "00_System"
                / "Graph_History"
                / "Changes"
                / "code-v1-fixture__code-v2-fixture"
            )
            risk_text = (diff_root / "风险与复核.md").read_text(encoding="utf-8")
            relation_text = (diff_root / "关系差异.md").read_text(encoding="utf-8")
            index_text = (diff_root / "_index.md").read_text(encoding="utf-8")
            self.assertIn("### R99 · fixture_risk", risk_text)
            self.assertIn('"file_sha256": "fixture-evidence"', risk_text)
            self.assertIn("`extraction_limited`", relation_text)
            self.assertIn("fixture-semantic-only", index_text)

    def test_relation_and_wikilink_endpoints_resolve_without_path_collisions(self) -> None:
        with self.make_temp() as temp_name:
            temp = Path(temp_name)
            machine, v1, vault = write_fixture(temp)
            result = build_projection(machine, v1, vault, temp / "projection")
            report = validate_projection(machine, v1, vault, result.vault_root)

            self.assertEqual(report["broken_relation_endpoints"], [])
            self.assertEqual(report["broken_migration_endpoints"], [])
            self.assertEqual(report["broken_wikilinks"], [])
            self.assertEqual(report["broken_canvas_links"], [])
            self.assertEqual(report["path_collisions"], [])
            self.assertEqual(report["entity_pages"], 3)
            self.assertEqual(report["change_pages"], 3)

    def test_output_is_byte_deterministic_for_fixed_inputs(self) -> None:
        with self.make_temp() as temp_name:
            temp = Path(temp_name)
            machine, v1, vault = write_fixture(temp)
            first = build_projection(machine, v1, vault, temp / "projection-one")
            second = build_projection(machine, v1, vault, temp / "projection-two")

            self.assertEqual(
                tree_fingerprint(first.vault_root), tree_fingerprint(second.vault_root)
            )

    def test_missing_relation_endpoint_is_rejected_before_output(self) -> None:
        with self.make_temp() as temp_name:
            temp = Path(temp_name)
            machine, v1, vault = write_fixture(temp)
            relations_path = machine / "relations.jsonl"
            relations = [
                json.loads(line)
                for line in relations_path.read_text(encoding="utf-8").splitlines()
                if line
            ]
            relations.append(
                {
                    "from_entity_uid": "agv:ros:node:new-controller",
                    "predicate": "publishes",
                    "qualifiers": {},
                    "to_entity_uid": "agv:ros:interface:missing",
                }
            )
            relations_path.write_bytes(jsonl_bytes(relations))
            manifest_path = machine / "manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["semantic_relation_count"] = len(relations)
            manifest["artifact_sha256"]["relations.jsonl"] = sha256(
                relations_path.read_bytes()
            )
            manifest_path.write_bytes(json_bytes(manifest))

            with self.assertRaisesRegex(ProjectionError, "missing relation endpoint"):
                build_projection(machine, v1, vault, temp / "projection")

    def test_unicode_replacement_character_is_rejected_before_output(self) -> None:
        with self.make_temp() as temp_name:
            temp = Path(temp_name)
            machine, v1, vault = write_fixture(temp)
            warnings_path = machine / "extraction-warnings.jsonl"
            warnings_path.write_bytes(
                jsonl_bytes(
                    [
                        {
                            "detail": "broken \ufffd text",
                            "kind": "fixture_warning",
                            "path": "src/core/package.xml",
                        }
                    ]
                )
            )
            manifest_path = machine / "manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["artifact_sha256"]["extraction-warnings.jsonl"] = sha256(
                warnings_path.read_bytes()
            )
            manifest_path.write_bytes(json_bytes(manifest))

            with self.assertRaisesRegex(
                ProjectionError, "Unicode replacement character U\\+FFFD"
            ):
                build_projection(machine, v1, vault, temp / "projection")

    def test_unexpected_machine_artifact_is_rejected_before_copy(self) -> None:
        with self.make_temp() as temp_name:
            temp = Path(temp_name)
            machine, v1, vault = write_fixture(temp)
            (machine / "unexpected.txt").write_text("not part of the snapshot\n", encoding="utf-8")

            with self.assertRaisesRegex(
                ProjectionError, "unexpected machine artifacts: unexpected.txt"
            ):
                build_projection(machine, v1, vault, temp / "projection")

    def test_output_must_not_overlap_any_input_tree(self) -> None:
        with self.make_temp() as temp_name:
            temp = Path(temp_name)
            machine, v1, vault = write_fixture(temp)
            manifest_before = (machine / "manifest.json").read_bytes()
            candidates = [
                machine,
                machine / "nested-output",
                v1,
                v1 / "nested-output",
                vault,
                vault / "nested-output",
                temp,
            ]
            for candidate in candidates:
                with self.subTest(output=str(candidate)):
                    with self.assertRaisesRegex(ProjectionError, "overlaps"):
                        build_projection(machine, v1, vault, candidate)
                    self.assertEqual((machine / "manifest.json").read_bytes(), manifest_before)


class ActualArtifactIntegrationTests(unittest.TestCase):
    def test_current_machine_artifacts_generate_a_valid_projection(self) -> None:
        machine = WORKSPACE_ROOT / "work" / "v2_staging" / "output"
        v1 = Path(
            r"D:\AGV_Knowledge_Base\00_System\Graph_History\Snapshots\code-v1"
        )
        vault = Path(r"D:\AGV_Knowledge_Base")
        if not (machine / "manifest.json").is_file() or not (v1 / "manifest.json").is_file():
            self.skipTest("Current V2 or immutable V1 artifacts are not available")

        output = PROJECT_DIR / "output"
        result = build_projection(machine, v1, vault, output)
        report = validate_projection(machine, v1, vault, result.vault_root)

        manifest = json.loads((machine / "manifest.json").read_text(encoding="utf-8"))
        diff = json.loads(
            (machine / "v1-to-v2-diff.json").read_text(encoding="utf-8")
        )
        self.assertEqual(result.entity_page_count, manifest["entity_count"])
        self.assertEqual(result.change_page_count, len(diff["entity_changes"]))
        self.assertEqual(result.entity_page_count, 192)
        self.assertEqual(result.change_page_count, 143 + 33 + 13)
        self.assertEqual(
            [risk["risk_id"] for risk in diff["risks"]],
            [f"R{index:02d}" for index in range(1, 17)],
        )
        self.assertEqual(len(diff["relation_removed"]), 54)
        self.assertEqual(
            {row["comparison_classification"] for row in diff["relation_removed"]},
            {"extraction_limited"},
        )
        self.assertEqual({row["review"] for row in diff["relation_removed"]}, {"needs-review"})
        warnings = [
            json.loads(line)
            for line in (machine / "extraction-warnings.jsonl")
            .read_text(encoding="utf-8")
            .splitlines()
            if line
        ]
        self.assertEqual(
            warnings,
            [
                {
                    "detail": "not well-formed (invalid token): line 40, column 33",
                    "kind": "invalid_launch_xml",
                    "path": "src/wheeltec_base/launch/wheeltec_base.launch",
                }
            ],
        )
        self.assertEqual(report["broken_relation_endpoints"], [])
        self.assertEqual(report["broken_migration_endpoints"], [])
        self.assertEqual(report["broken_wikilinks"], [])
        self.assertEqual(report["broken_canvas_links"], [])
        self.assertEqual(report["path_collisions"], [])
        self.assertEqual(report["byte_copy_mismatches"], [])
        self.assertEqual(report["unexpected_obsidian_paths"], [])

        history_root = result.vault_root / "00_System" / "Graph_History"
        current = json.loads((history_root / "current.json").read_text(encoding="utf-8"))
        self.assertEqual(current["review"], "verified")
        self.assertEqual(current["current_status"], "active")
        self.assertEqual(current["candidate_review"], "generated")
        self.assertEqual(current["candidate_status"], "candidate_pending_review")
        history_index = (history_root / "_index.md").read_text(encoding="utf-8")
        recommended = (history_root / "当前推荐快照.md").read_text(encoding="utf-8")
        self.assertEqual(history_index.count("```dataview"), 2)
        self.assertIn("[[图谱快照与差异Schema]]", history_index)
        self.assertIn("[[../Decisions/ADR-002-代码图谱快照与增量差异]]", history_index)
        self.assertIn("[[../../研发图谱工作台|返回研发图谱工作台]]", history_index)
        self.assertIn('review: "verified"', recommended)
        self.assertIn('candidate_review: "generated"', recommended)
        self.assertIn('candidate_status: "candidate_pending_review"', recommended)

        diff_root = (
            result.vault_root
            / "00_System"
            / "Graph_History"
            / "Changes"
            / f"{diff['baseline_snapshot']}__{diff['target_snapshot']}"
        )
        risk_text = (diff_root / "风险与复核.md").read_text(encoding="utf-8")
        relation_text = (diff_root / "关系差异.md").read_text(encoding="utf-8")
        index_text = (diff_root / "_index.md").read_text(encoding="utf-8")
        for risk_id in (f"R{index:02d}" for index in range(1, 17)):
            self.assertIn(f"### {risk_id} ·", risk_text)
        self.assertEqual(relation_text.count("`extraction_limited`"), 55)
        for limitation in diff["comparison_limitations"]:
            self.assertIn(limitation["limitation_id"], index_text)


if __name__ == "__main__":
    unittest.main()
