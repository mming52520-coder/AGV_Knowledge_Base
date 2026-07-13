---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:chassis-cmd"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:chassis-cmd"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:chassis-cmd"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/chassis/cmd"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "6d5eca2a1a294ff0517b4aa7f57258897be19a18234117f8ccf11d4ada8d93c6"
relation_fingerprint: "ca849cd8a4f34978419f93768c23a994172b784ff42bc48714ebbb840ab9368f"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /chassis/cmd

- 逻辑实体：`agv:ros:interface:chassis-cmd`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:chassis-cmd`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/chassis_controller/src/chassis_bridge.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | chassis_controller/ChassisCommand |
| `ros_name` | /chassis/cmd |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | [] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_execution/src/chassis_gateway_node.cpp` | 46 | `publishes` | `f30568932c8e70e73f4ee7677a7d3905faa2e11bc0864fa8547c64a92e3b60b7` |
| `src/chassis_controller/src/chassis_bridge.cpp` | 533 | `subscribes` | `3a0cb99a9e0a47cb51c96f6034ea566cac7c9cca3146fbc295076de2ed9622f2` |
| `src/trajectory_recorder/src/trajectory_tracker.cpp` | 3809 | `publishes` | `b13ba9a028ec7abd7b3956173e7cc20bc3a123038872ec4ea9c3a159ccf795c7` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_execution--855e548bdcfd|agv:ros:package:agv_execution]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/chassis_controller--57f0aa46929c|agv:ros:package:chassis_controller]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/chassis_gateway_node--e753a2e58776|agv:ros:node:chassis_gateway_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_tracker--3031ab8e89fc|agv:ros:node:trajectory_tracker]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/chassis_bridge--f2b72fa46041|agv:ros:node:chassis_bridge]] → `subscribes`

## 相对 V1 的变化

- `unchanged`：语义指纹与 V1 一致。
