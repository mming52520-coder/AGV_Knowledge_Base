---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:vehicle-state"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:vehicle-state"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:vehicle-state"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/vehicle/state"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "45bf41dcdf55441a027b70e40b0c17f02317162b3af00bf47d7cbbdde3ca6206"
relation_fingerprint: "b53b344519909a28cb6bae3509734bc43a47916e4dbdde000a2172cc6a3b913e"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /vehicle/state

- 逻辑实体：`agv:ros:interface:vehicle-state`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:vehicle-state`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_legacy/src/legacy_sensor_adapter.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | agv_interfaces/VehicleState |
| `ros_name` | /vehicle/state |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_decision/src/trajectory_follower_node.cpp` | 27 | `subscribes` | `911174c1a90ddde2bf29311d6d29b86f2dd47591c4f01c2b82c387523874a3c3` |
| `src/agv_legacy/src/legacy_sensor_adapter.cpp` | 18 | `subscribes` | `5f79e6f350f2296d63e20a6a315495ca50c9df9afabaac13718eb41917c24c3f` |
| `src/agv_safety/src/safety_supervisor_node.cpp` | 25 | `subscribes` | `6fc04009a55824b6cbbf37ed22b770e68164645af33b7f4b84a8fd6908c74b8a` |
| `src/agv_state_estimation/src/vehicle_state_estimator_node.cpp` | 37 | `publishes` | `a2fcf806695f2d7e23fbdc9ac6f12ae8255ee662dbd3e24eeeac9f43c983825f` |
| `src/agv_telemetry/src/telemetry_node.cpp` | 28 | `subscribes` | `54f7e54df3144dcd25b9fafd5e316ba1b17b5bb1eb92f9b79beae2ecfa7fb2b6` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_legacy--db70b74c409e|agv:ros:package:agv_legacy]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_safety--2cb0a140ec4e|agv:ros:package:agv_safety]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_state_estimation--99b849143b75|agv:ros:package:agv_state_estimation]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_telemetry--948609af5cdf|agv:ros:package:agv_telemetry]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/vehicle_state_estimator_node--f5bf32466a46|agv:ros:node:vehicle_state_estimator_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/legacy_sensor_adapter--19bf3fffdcd7|agv:ros:node:legacy_sensor_adapter]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/safety_supervisor_node--c235eb005bf0|agv:ros:node:safety_supervisor_node]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/telemetry_node--8a7add193f0d|agv:ros:node:telemetry_node]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_follower_node--983183f9b80a|agv:ros:node:trajectory_follower_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/vehicle-state--f1837ba03534|agv:ros:interface:vehicle-state]]
