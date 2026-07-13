---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:mag_guidance_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:mag_guidance_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:mag_guidance_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "mag_guidance_node"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "85d2c494e3c844b65f1aaf9d73c419bb24ab1a5b9fd96ea5cea5e3536d33ccde"
relation_fingerprint: "d1cc2f16e1914ffcd2bb0efdbcfdcb1a2cf71d5ee94e21c9e56b7e47fa205f42"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# mag_guidance_node

- 逻辑实体：`agv:ros:node:mag_guidance_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:mag_guidance_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_decision/src/mag_guidance_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | mag_guidance_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /decision/mag_guidance_node |
| `status` | active |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_decision/src/mag_guidance_node.cpp` | 1 | `node_source` | `716d5907263ee74cc9ac8e2d602f6e1cf575a45dfa3f8d42f41484f16f82f4dd` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-magnetic_intent--b3456506e926|agv:ros:interface:decision-magnetic-intent]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/perception-state--9e4cc739ed14|agv:ros:interface:perception-state]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/mag_guidance_node--57ab4596f322|agv:ros:node:mag_guidance_node]]
