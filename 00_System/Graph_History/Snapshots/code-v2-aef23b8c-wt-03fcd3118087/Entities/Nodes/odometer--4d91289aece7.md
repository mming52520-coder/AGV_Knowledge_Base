---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:odometer"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:odometer"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:odometer"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "odometer"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "11b98a7105e49256d546ffad5627b0b3f4cd6a40547a09e21905d37b2816a5ca"
relation_fingerprint: "3206982c89785d84a6573db906463d1b14373dd751e98f03101845df8933f310"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# odometer

- 逻辑实体：`agv:ros:node:odometer`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:odometer`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/odometer/src/odometer.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | odometer |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /ackermann_odometry_node |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/odometer/src/odometer.cpp` | 1 | `node_source` | `f1a235cae5e0fa57a303bd0b2853cf7498f75249ece10e5749a43b69210c8bb6` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/odometer--6b13553e3c5a|agv:ros:package:odometer]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/encoder_twist--e5de60543d8b|agv:ros:interface:encoder-twist]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/odom--1e74762c157b|agv:ros:interface:odom]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ackermann_cmd--a9657963ea4a|agv:ros:interface:ackermann-cmd]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/wheel_encoder_data--3690ed9ff087|agv:ros:interface:wheel-encoder-data]]

## 入向关系

- 无

## 相对 V1 的变化

- `unchanged`：语义指纹与 V1 一致。
