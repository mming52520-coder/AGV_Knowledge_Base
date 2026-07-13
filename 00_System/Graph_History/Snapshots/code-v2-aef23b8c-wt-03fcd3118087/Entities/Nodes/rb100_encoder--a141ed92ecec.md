---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:rb100_encoder"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:rb100_encoder"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:rb100_encoder"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "rb100_encoder"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "4d005214518f5b6160e920f12562734070cb1be51bd7a82e22c7af04380058c0"
relation_fingerprint: "2f73629dcec0d8186bab1b83abe880bcfcc231686e665c55c8a8dbb1d35c4bc4"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# rb100_encoder

- 逻辑实体：`agv:ros:node:rb100_encoder`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:rb100_encoder`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/encoder/src/rb100_encoder.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | rb100_encoder |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /rb100_odometry_node |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/encoder/src/rb100_encoder.cpp` | 1 | `node_source` | `7606db8a8175b2049da2c09f11abbf03ca27b57029c298c14fd25c0a42513000` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/encoder--0240516ec77b|agv:ros:package:encoder]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/encoder_angle--bca3ba1cc686|agv:ros:interface:encoder-angle]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/encoder_twist--e5de60543d8b|agv:ros:interface:encoder-twist]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/odom--1e74762c157b|agv:ros:interface:odom]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/rb100_encoder--a141ed92ecec|agv:ros:node:rb100_encoder]]
