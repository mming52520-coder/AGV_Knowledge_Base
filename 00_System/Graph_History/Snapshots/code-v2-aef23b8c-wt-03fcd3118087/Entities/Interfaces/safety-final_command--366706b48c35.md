---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:safety-final-command"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:safety-final-command"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:safety-final-command"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/safety/final_command"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "6f6aedc80d3f4e0c2446a170d47727a194e18cf9e5ddcaf8fad9e7d3d3012cec"
relation_fingerprint: "64da0e21a123e2d05ab2523d3c4b4e137ca1bfc196dc418c2374f0a3c8608b34"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /safety/final_command

- 逻辑实体：`agv:ros:interface:safety-final-command`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:safety-final-command`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_execution/src/chassis_gateway_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | agv_interfaces/MotionCommand |
| `ros_name` | /safety/final_command |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_execution/src/chassis_gateway_node.cpp` | 42 | `subscribes` | `f30568932c8e70e73f4ee7677a7d3905faa2e11bc0864fa8547c64a92e3b60b7` |
| `src/agv_legacy/src/legacy_command_adapter.cpp` | 19 | `subscribes` | `fa4aef04bb56c36e83a3ca8f01ef53b7482c8583a11473a4a6a74259e2fa3901` |
| `src/agv_safety/src/safety_supervisor_node.cpp` | 29 | `publishes` | `6fc04009a55824b6cbbf37ed22b770e68164645af33b7f4b84a8fd6908c74b8a` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_execution--855e548bdcfd|agv:ros:package:agv_execution]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_legacy--db70b74c409e|agv:ros:package:agv_legacy]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_safety--2cb0a140ec4e|agv:ros:package:agv_safety]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/safety_supervisor_node--c235eb005bf0|agv:ros:node:safety_supervisor_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/chassis_gateway_node--e753a2e58776|agv:ros:node:chassis_gateway_node]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/legacy_command_adapter--30863753bf07|agv:ros:node:legacy_command_adapter]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/safety-final-command--366706b48c35|agv:ros:interface:safety-final-command]]
