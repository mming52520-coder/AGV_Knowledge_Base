---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:safety-estop-request"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:safety-estop-request"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:safety-estop-request"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/safety/estop_request"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "067272ed8e8daf609b320c2ccfe467b8f570faa8e2266fac9645067050318172"
relation_fingerprint: "546db6678c98cf916fb547005853e72839530415846c9b72d6f8be06c11fb7ac"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /safety/estop_request

- 逻辑实体：`agv:ros:interface:safety-estop-request`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:safety-estop-request`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_safety/src/safety_supervisor_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | unknown |
| `ros_name` | /safety/estop_request |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_safety/src/safety_supervisor_node.cpp` | 27 | `subscribes` | `6fc04009a55824b6cbbf37ed22b770e68164645af33b7f4b84a8fd6908c74b8a` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_safety--2cb0a140ec4e|agv:ros:package:agv_safety]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/safety_supervisor_node--c235eb005bf0|agv:ros:node:safety_supervisor_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/safety-estop-request--ac3e325e6d4c|agv:ros:interface:safety-estop-request]]
