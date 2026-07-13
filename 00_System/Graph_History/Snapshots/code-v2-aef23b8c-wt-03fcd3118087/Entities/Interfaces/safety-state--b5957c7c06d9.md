---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:safety-state"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:safety-state"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:safety-state"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/safety/state"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "4c36ac751719e02294e9d27f9d067b8bb1ccc00d8807fab2d37af28069f1134c"
relation_fingerprint: "39a6abe6e0cd1146e0fccff07cd6b4575d4338def324fc34eceedce6b638849c"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /safety/state

- 逻辑实体：`agv:ros:interface:safety-state`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:safety-state`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_safety/src/safety_supervisor_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | agv_interfaces/SafetyState |
| `ros_name` | /safety/state |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_safety/src/safety_supervisor_node.cpp` | 30 | `publishes` | `6fc04009a55824b6cbbf37ed22b770e68164645af33b7f4b84a8fd6908c74b8a` |
| `src/agv_telemetry/src/telemetry_node.cpp` | 26 | `subscribes` | `54f7e54df3144dcd25b9fafd5e316ba1b17b5bb1eb92f9b79beae2ecfa7fb2b6` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_safety--2cb0a140ec4e|agv:ros:package:agv_safety]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_telemetry--948609af5cdf|agv:ros:package:agv_telemetry]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/safety_supervisor_node--c235eb005bf0|agv:ros:node:safety_supervisor_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/telemetry_node--8a7add193f0d|agv:ros:node:telemetry_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/safety-state--b5957c7c06d9|agv:ros:interface:safety-state]]
