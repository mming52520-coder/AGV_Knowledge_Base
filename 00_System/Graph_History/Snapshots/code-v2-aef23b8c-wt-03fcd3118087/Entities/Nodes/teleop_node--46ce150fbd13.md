---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:teleop_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:teleop_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:teleop_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "teleop_node"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "b87e6fe94c1d3213dae852133b7d0b3eef770be224bc3667b766606d2c32070c"
relation_fingerprint: "b2b81b4cc38b9451350efd0b6510b2c094fef7c93311ea5948b9ec3eaf6d7285"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# teleop_node

- 逻辑实体：`agv:ros:node:teleop_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:teleop_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_decision/src/teleop_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | teleop_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /decision/teleop_node |
| `status` | active |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_decision/src/teleop_node.cpp` | 1 | `node_source` | `65c9f0dd0ffe21416bf2c999e3e75fd727066c7dc27a3cf1e00d483a766c038f` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-teleop_intent--f636270024da|agv:ros:interface:decision-teleop-intent]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/teleop-cmd--cbd3a6af2f03|agv:ros:interface:teleop-cmd]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/teleop-stop--23faf388f567|agv:ros:interface:teleop-stop]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/teleop_node--46ce150fbd13|agv:ros:node:teleop_node]]
