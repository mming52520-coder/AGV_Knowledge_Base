---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_decision"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:agv_decision"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_decision"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "agv_decision"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "337668df6728636b5bc3ee462212c1ad5f18a388606726596b922537d8fd874f"
relation_fingerprint: "8fac71142814f8ec224d8e1519ce9241217b32a79d42ea351c93be8c426c38c8"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# agv_decision

- 逻辑实体：`agv:ros:package:agv_decision`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_decision`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/agv_decision/package.xml`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` |  |
| `status` | active |
| `type` | ros_package |
| `vehicles` | ["三号车"] |
| `version` | 0.0.1 |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_decision/package.xml` | 1 | `package_manifest` | `f18856c8dfca90ade2f11579b5e8265bfc4f47319fae1222459f16dfcc792828` |

## 出向关系

- `depends_on` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_interfaces--7060d62ebf45|agv:ros:package:agv_interfaces]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_bringup--4378167611a3|agv:ros:package:agv_bringup]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/left_wall_node--fdb9bf57d711|agv:ros:node:left_wall_node]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/mag_guidance_node--57ab4596f322|agv:ros:node:mag_guidance_node]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/teleop_node--46ce150fbd13|agv:ros:node:teleop_node]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/tight_turn_node--fafce7d62191|agv:ros:node:tight_turn_node]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_follower_node--983183f9b80a|agv:ros:node:trajectory_follower_node]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-left_wall_intent--8c1624b405c7|agv:ros:interface:decision-left-wall-intent]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-magnetic_intent--b3456506e926|agv:ros:interface:decision-magnetic-intent]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-teleop_intent--f636270024da|agv:ros:interface:decision-teleop-intent]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-tight_turn_intent--f3e83fac1cd0|agv:ros:interface:decision-tight-turn-intent]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-trajectory_intent--1a822f17b0b7|agv:ros:interface:decision-trajectory-intent]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-state--1bf376c688d5|agv:ros:interface:mission-state]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-trajectory_file--3e1456a7d19b|agv:ros:interface:mission-trajectory-file]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/perception-state--9e4cc739ed14|agv:ros:interface:perception-state]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/teleop-cmd--cbd3a6af2f03|agv:ros:interface:teleop-cmd]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/teleop-stop--23faf388f567|agv:ros:interface:teleop-stop]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/vehicle-state--f1837ba03534|agv:ros:interface:vehicle-state]] → `related_packages`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]]
