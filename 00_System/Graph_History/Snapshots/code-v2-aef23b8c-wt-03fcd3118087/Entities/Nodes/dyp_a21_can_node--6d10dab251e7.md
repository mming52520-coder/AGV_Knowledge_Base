---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:dyp_a21_can_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:dyp_a21_can_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:dyp_a21_can_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "dyp_a21_can_node"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "b7cba7ca882e01699374ff9d4d181e23aa379f7e08dd9982bf5c671a02959da3"
relation_fingerprint: "362158f421a9f4db7f78bcb1bb2da3161964c006f6f17b0547d86eded3cd2202"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# dyp_a21_can_node

- 逻辑实体：`agv:ros:node:dyp_a21_can_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:dyp_a21_can_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/ultrasonic_controlled_motor/src/dyp_a21_can.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | dyp_a21_can_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /dyp_a21_can_node |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/ultrasonic_controlled_motor/src/dyp_a21_can.cpp` | 1 | `node_source` | `40320a951b654ddb496e01d793b0b4939a47cf9cde3f54c541d4a232bc2305d5` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/ultrasonic_controlled_motor--2e98007ce616|agv:ros:package:ultrasonic_controlled_motor]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_distance--1240d1cca41f|agv:ros:interface:ultrasonic-left-distance]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_status--076d80f3e514|agv:ros:interface:ultrasonic-left-status]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/dyp_a21_can_node--6d10dab251e7|agv:ros:node:dyp_a21_can_node]]
