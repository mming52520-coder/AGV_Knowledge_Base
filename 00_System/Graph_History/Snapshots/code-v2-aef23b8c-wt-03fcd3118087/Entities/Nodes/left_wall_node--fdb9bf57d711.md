---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:left_wall_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:left_wall_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:left_wall_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "left_wall_node"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "80999f98e999535e24c2fe17eff88e78fb7253cb4addc06bca6e62508db39df9"
relation_fingerprint: "64db286c7e5a1c64dd1545153812ce5ef87bc242dbfb4e2c5bfa40af78c02095"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# left_wall_node

- 逻辑实体：`agv:ros:node:left_wall_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:left_wall_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_decision/src/left_wall_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | left_wall_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /decision/left_wall_node |
| `status` | active |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_decision/src/left_wall_node.cpp` | 1 | `node_source` | `c20f48e877a36e5a382864cd88b6b387483b57b78515b5381aa592200cb73735` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-left_wall_intent--8c1624b405c7|agv:ros:interface:decision-left-wall-intent]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/perception-state--9e4cc739ed14|agv:ros:interface:perception-state]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/left_wall_node--fdb9bf57d711|agv:ros:node:left_wall_node]]
