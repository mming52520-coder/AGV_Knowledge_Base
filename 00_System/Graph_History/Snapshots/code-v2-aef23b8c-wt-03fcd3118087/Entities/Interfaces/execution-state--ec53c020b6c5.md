---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:execution-state"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:execution-state"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:execution-state"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/execution/state"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "e59cfbecc0cf7931e899898dd1c02ea905d45e1851d60f68807be30c1a7f9fb7"
relation_fingerprint: "138c03027fd2c19febe16801df4af60d7cbf6304ed4a5b67ae392bea475a46ee"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /execution/state

- 逻辑实体：`agv:ros:interface:execution-state`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:execution-state`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_execution/src/chassis_gateway_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | agv_interfaces/ExecutionState |
| `ros_name` | /execution/state |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_execution/src/chassis_gateway_node.cpp` | 43 | `publishes` | `f30568932c8e70e73f4ee7677a7d3905faa2e11bc0864fa8547c64a92e3b60b7` |
| `src/agv_safety/src/safety_supervisor_node.cpp` | 26 | `subscribes` | `6fc04009a55824b6cbbf37ed22b770e68164645af33b7f4b84a8fd6908c74b8a` |
| `src/agv_state_estimation/src/vehicle_state_estimator_node.cpp` | 33 | `subscribes` | `a2fcf806695f2d7e23fbdc9ac6f12ae8255ee662dbd3e24eeeac9f43c983825f` |
| `src/agv_telemetry/src/telemetry_node.cpp` | 27 | `subscribes` | `54f7e54df3144dcd25b9fafd5e316ba1b17b5bb1eb92f9b79beae2ecfa7fb2b6` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_execution--855e548bdcfd|agv:ros:package:agv_execution]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_safety--2cb0a140ec4e|agv:ros:package:agv_safety]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_state_estimation--99b849143b75|agv:ros:package:agv_state_estimation]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_telemetry--948609af5cdf|agv:ros:package:agv_telemetry]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/chassis_gateway_node--e753a2e58776|agv:ros:node:chassis_gateway_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/safety_supervisor_node--c235eb005bf0|agv:ros:node:safety_supervisor_node]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/telemetry_node--8a7add193f0d|agv:ros:node:telemetry_node]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/vehicle_state_estimator_node--f5bf32466a46|agv:ros:node:vehicle_state_estimator_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/execution-state--ec53c020b6c5|agv:ros:interface:execution-state]]
