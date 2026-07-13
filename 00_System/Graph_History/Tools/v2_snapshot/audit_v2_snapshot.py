#!/usr/bin/env python3
"""Audit the staged V2 graph against the agreed snapshot invariants."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

import generate_v2_snapshot as graph


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def relation_keys(rows: Iterable[dict[str, Any]]) -> set[tuple[str, str, str | None]]:
    return {
        (row["from_entity_uid"], row["predicate"], row.get("to_entity_uid"))
        for row in rows
    }


def audit(
    output: Path,
    source: Path,
    v1: Path,
    v1_source: Path | None = None,
) -> dict[str, Any]:
    graph.validate_output(output, source, v1, v1_source)
    manifest = load_json(output / "manifest.json")
    diff = load_json(output / "v1-to-v2-diff.json")
    entities = load_jsonl(output / "entities.jsonl")
    migrations = load_jsonl(output / "migration-relations.jsonl")
    sources = load_jsonl(output / "source-files.jsonl")
    warnings = load_jsonl(output / "extraction-warnings.jsonl")
    by_uid = {row["entity_uid"]: row for row in entities}
    nodes = [row for row in entities if row["type"] == "ros_node"]

    require({path.name for path in output.iterdir()} == graph.OUTPUT_ARTIFACTS, "output artifact allowlist mismatch")
    baseline_context = manifest.get("baseline_source_context") or {}
    require(baseline_context.get("available") is True, "V1 source context is not available")
    require(bool(baseline_context.get("integrity_limitation")), "V1 source integrity limitation is missing")
    require(baseline_context.get("aggregate_hash_reverified") is False, "V1 aggregate hash is overstated as reverified")
    limitation_ids = {row["limitation_id"] for row in manifest.get("extraction_limitations", [])}
    require({
        "launch-static-xml-only",
        "endpoint-static-syntax-only",
        "relation-removal-not-definitive",
        "private-path-disclosure",
    }.issubset(limitation_ids), "required extraction limitations are missing")
    comparison_ids = {row["limitation_id"] for row in diff.get("comparison_limitations", [])}
    require("unchanged-graph-semantics-not-source-code" in comparison_ids, "entity comparison limitation is missing")
    require("cross-extractor-relation-drift" in comparison_ids, "relation drift limitation is missing")

    require(len(nodes) == 39, f"expected 39 primary ROS nodes, got {len(nodes)}")
    require(sum(row["type"] == "ros_package" for row in entities) == 25, "expected 25 packages")
    forbidden = {"coulomb_meter", "joy_turtlebot", "joy_turtlesim"}
    require(not forbidden.intersection(row["title"] for row in nodes), "context node leaked into primary graph")
    context_paths = {row["path"] for row in sources if row["disposition"] == "context"}
    require("src/_archived_battery_management/src/coulomb_meter.cpp" in context_paths, "archived battery source is not context")
    require("src/remote_ctrl/scripts/joy_turtlebot.py" in context_paths, "joy_turtlebot is not context")
    require("src/remote_ctrl/scripts/joy_turtlesim.py" in context_paths, "joy_turtlesim is not context")

    decision_nodes = {
        "trajectory_follower_node",
        "left_wall_node",
        "mag_guidance_node",
        "tight_turn_node",
        "teleop_node",
    }
    for title in decision_nodes:
        entity = by_uid[f"agv:ros:node:{title}"]
        require(entity["semantic"]["ros_name"] == f"/decision/{title}", f"bad production namespace for {title}")
        require(f"/decision/{title}" in entity["launch_names"], f"missing production alias for {title}")
        require(f"/{title}" in entity["launch_names"], f"missing alternate alias for {title}")

    motor_expectations = {
        "agv:ros:node:magnetic_motor_control": (
            "motor_control",
            "agv:ros:package:magnetic_controlled_motor",
            "src/magnetic_controlled_motor/src/motor_control.cpp",
        ),
        "agv:ros:node:ultrasonic_motor_control": (
            "motor_control_node",
            "agv:ros:package:ultrasonic_controlled_motor",
            "src/ultrasonic_controlled_motor/src/motor_control.cpp",
        ),
    }
    for uid, (executable, package_uid, source_path) in motor_expectations.items():
        entity = by_uid[uid]
        require(entity["semantic"]["executable"] == executable, f"bad executable for {uid}")
        require(entity["package_uid"] == package_uid, f"bad package for {uid}")
        require(any(evidence["path"] == source_path for evidence in entity["evidence"]), f"bad source evidence for {uid}")
    require(all(any(e.get("operation") == "node_source" for e in row["evidence"]) for row in nodes), "node without source evidence")

    semantic_keys = relation_keys(load_jsonl(output / "relations.jsonl"))
    representative_mqtt_edges = {
        ("agv:ros:node:agv_mqtt_bridge", "subscribes", "agv:ros:interface:odom"),
        ("agv:ros:node:agv_mqtt_bridge", "subscribes", "agv:ros:interface:imu"),
        ("agv:ros:node:agv_mqtt_bridge", "subscribes", "agv:ros:interface:mag-sensor-frame"),
    }
    require(representative_mqtt_edges.issubset(semantic_keys), "representative MQTT wrapper edges are missing")
    require(by_uid["agv:ros:interface:odom"]["semantic"]["message_type"] == "nav_msgs/Odometry", "MQTT /odom type is unresolved")
    require(by_uid["agv:ros:interface:imu"]["semantic"]["message_type"] == "sensor_msgs/Imu", "MQTT /imu type is unresolved")
    require(
        by_uid["agv:ros:interface:mag-sensor-frame"]["semantic"]["message_type"]
        == "magnetic_controlled_motor/MagFrame",
        "MQTT magnetic frame type is unresolved",
    )

    keys = relation_keys(migrations)
    expected = {
        ("agv:ros:node:remote_controller", "parallel_replacement", "agv:ros:node:teleop_node"),
        ("agv:ros:node:magnetic_follower", "parallel_replacement", "agv:ros:node:mag_guidance_node"),
        ("agv:ros:node:ultrasonic_follower", "decomposed_into", "agv:ros:node:left_wall_node"),
        ("agv:ros:node:ultrasonic_follower", "decomposed_into", "agv:ros:node:safety_supervisor_node"),
        ("agv:ros:node:drive_feedback_odom", "superseded_by", "agv:ros:node:vehicle_state_estimator_node"),
        ("agv:ros:node:gps_nmea_to_fix_json", "removed_without_replacement", None),
        ("agv:ros:node:encoder_probe", "removed_diagnostic", None),
        ("agv:ros:node:yz_aim_probe", "removed_diagnostic", None),
        ("agv:ros:interface:odom", "owner_changed", "agv:ros:interface:odom"),
        ("agv:ros:interface:chassis-cmd", "publisher_changed", "agv:ros:interface:chassis-cmd"),
        ("agv:ros:package:agv_mqtt_bridge", "capability_extracted_to", "agv:ros:package:agv_telemetry"),
        ("agv:ros:package:agv_mqtt_bridge", "capability_extracted_to", "agv:ros:package:agv_mission"),
    }
    require(expected.issubset(keys), f"missing required migration keys: {sorted(expected - keys)}")
    trajectory_targets = {
        target
        for source_uid, predicate, target in keys
        if source_uid == "agv:ros:node:trajectory_tracker" and predicate == "decomposed_into"
    }
    require(trajectory_targets == {
        "agv:ros:node:vehicle_state_estimator_node",
        "agv:ros:node:trajectory_follower_node",
        "agv:ros:node:left_wall_node",
        "agv:ros:node:mag_guidance_node",
        "agv:ros:node:tight_turn_node",
        "agv:ros:node:motion_arbiter_node",
        "agv:ros:node:safety_supervisor_node",
        "agv:ros:node:chassis_gateway_node",
    }, f"trajectory decomposition mismatch: {sorted(trajectory_targets)}")
    for migration in migrations:
        if migration["predicate"] in graph.TERMINAL_MIGRATION_PREDICATES:
            require(migration["to_entity_uid"] is None and migration["to_snapshot"] is None, "terminal migration has a target")
            evidence = migration["evidence"]
            require(evidence.get("baseline_artifact", {}).get("path") == "entities.jsonl", "terminal V1 artifact evidence missing")
            require(evidence.get("target_artifact", {}).get("path") == "entities.jsonl", "terminal V2 artifact evidence missing")
            require(evidence.get("target_artifact", {}).get("expected_count") == 0, "terminal absence assertion missing")

    risks = diff["risks"]
    require([row["risk_id"] for row in risks] == [f"R{i:02d}" for i in range(1, 17)], "risk IDs are not exactly R01-R16")
    require(all(row["validation_state"] == "static_evidence_only" for row in risks), "risk has non-static validation state")
    require(all(row["independent_tests_run"] is False for row in risks), "risk incorrectly claims independent tests")
    require(all(row["review"] == "needs-review" for row in risks), "risk is missing review flag")
    require(all(row["evidence"] for row in risks), "risk is missing evidence")
    require(all(item.get("path") and item.get("locator") for row in risks for item in row["evidence"]), "risk evidence lacks path/locator")
    require(manifest["git_state"]["status_counts"] == {" M": 31, "??": 126}, "R01 Git status counts drifted")

    counts = diff["entity_counts"]
    require(counts["baseline"] == counts["matched"] + counts["removed"], "V1 conservation failed")
    require(counts["target"] == counts["matched"] + counts["added"], "V2 conservation failed")
    require(counts["matched"] == counts["unchanged"] + counts["modified"], "matched conservation failed")
    relation_counts = diff["relation_counts"]
    require(relation_counts["baseline"] == relation_counts["matched"] + relation_counts["removed"], "V1 relation conservation failed")
    require(relation_counts["target"] == relation_counts["matched"] + relation_counts["added"], "V2 relation conservation failed")
    require(relation_counts["removed"] == relation_counts["removed_extraction_limited"], "relation removal classification mismatch")
    require(all(
        row.get("comparison_classification") == "extraction_limited"
        and row.get("breaking") is False
        and row.get("review") == "needs-review"
        for row in diff["relation_removed"]
    ), "V1-only relation is overstated as definitive removal")
    require(not any("fuzzy" in row["match_method"] or "heuristic" in row["match_method"] for row in diff["entity_changes"]), "fuzzy/heuristic entity match detected")
    require(not any(row["kind"] == "launch_node_without_source_evidence" for row in warnings), "launch-only node warning remains")
    require(warnings == [{
        "detail": "not well-formed (invalid token): line 40, column 33",
        "kind": "invalid_launch_xml",
        "path": "src/wheeltec_base/launch/wheeltec_base.launch",
    }], f"unexpected extraction warnings: {warnings}")

    return {
        "status": "ok",
        "snapshot_id": manifest["snapshot_id"],
        "snapshot_fingerprint": manifest["snapshot_fingerprint"],
        "source_fingerprint": manifest["source_fingerprint"],
        "counts": {
            "source_files": manifest["source_file_count"],
            "included_sources": manifest["included_source_file_count"],
            "context_sources": manifest["context_source_file_count"],
            "excluded_sources": manifest["excluded_source_file_count"],
            "packages": sum(row["type"] == "ros_package" for row in entities),
            "nodes": len(nodes),
            "interfaces": sum(row["type"] == "ros_interface" for row in entities),
            "entities": len(entities),
            "semantic_relations": len(load_jsonl(output / "relations.jsonl")),
            "migration_relations": len(migrations),
            "risks": len(risks),
            "warnings": len(warnings),
        },
        "diff": counts,
        "risk_severities": dict(Counter(row["severity"] for row in risks)),
        "warning_kinds": dict(Counter(row["kind"] for row in warnings)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--v1", type=Path, required=True)
    parser.add_argument("--v1-source", type=Path)
    args = parser.parse_args()
    result = audit(
        args.output.resolve(),
        args.source.resolve(),
        args.v1.resolve(),
        args.v1_source.resolve() if args.v1_source is not None else None,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
