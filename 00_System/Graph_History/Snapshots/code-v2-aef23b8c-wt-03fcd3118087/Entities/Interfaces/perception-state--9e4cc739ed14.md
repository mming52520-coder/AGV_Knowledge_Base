---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:perception-state"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:perception-state"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:perception-state"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/perception/state"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "7ae9a7394cd23568b184f7b710a4c48d1d94f37dcfe1a890414f418913067926"
relation_fingerprint: "8c2b15a08ebabeb8b9351a3bd878134ea1c3e04ac77530d0e723e2ffb3df5eff"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /perception/state

- 逻辑实体：`agv:ros:interface:perception-state`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:perception-state`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_decision/src/left_wall_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | agv_interfaces/PerceptionState |
| `ros_name` | /perception/state |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_decision/src/left_wall_node.cpp` | 17 | `subscribes` | `c20f48e877a36e5a382864cd88b6b387483b57b78515b5381aa592200cb73735` |
| `src/agv_decision/src/mag_guidance_node.cpp` | 17 | `subscribes` | `716d5907263ee74cc9ac8e2d602f6e1cf575a45dfa3f8d42f41484f16f82f4dd` |
| `src/agv_decision/src/tight_turn_node.cpp` | 19 | `subscribes` | `91e65662a315958e30e5896c0fb267ae5a005eb59c77198075854eb97152189c` |
| `src/agv_decision/src/trajectory_follower_node.cpp` | 26 | `subscribes` | `911174c1a90ddde2bf29311d6d29b86f2dd47591c4f01c2b82c387523874a3c3` |
| `src/agv_perception/src/perception_aggregator_node.cpp` | 61 | `publishes` | `5b988700b3ea59236ab37c28ca7d0b4bd1dc66b69bf3328b71245d703f16d089` |
| `src/agv_safety/src/safety_supervisor_node.cpp` | 24 | `subscribes` | `6fc04009a55824b6cbbf37ed22b770e68164645af33b7f4b84a8fd6908c74b8a` |
| `src/agv_state_estimation/src/vehicle_state_estimator_node.cpp` | 31 | `subscribes` | `a2fcf806695f2d7e23fbdc9ac6f12ae8255ee662dbd3e24eeeac9f43c983825f` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_perception--b3844e0c0c3f|agv:ros:package:agv_perception]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_safety--2cb0a140ec4e|agv:ros:package:agv_safety]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_state_estimation--99b849143b75|agv:ros:package:agv_state_estimation]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/perception_aggregator_node--38fa4d21e1c4|agv:ros:node:perception_aggregator_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/left_wall_node--fdb9bf57d711|agv:ros:node:left_wall_node]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/mag_guidance_node--57ab4596f322|agv:ros:node:mag_guidance_node]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/safety_supervisor_node--c235eb005bf0|agv:ros:node:safety_supervisor_node]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/tight_turn_node--fafce7d62191|agv:ros:node:tight_turn_node]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_follower_node--983183f9b80a|agv:ros:node:trajectory_follower_node]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/vehicle_state_estimator_node--f5bf32466a46|agv:ros:node:vehicle_state_estimator_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/perception-state--9e4cc739ed14|agv:ros:interface:perception-state]]
