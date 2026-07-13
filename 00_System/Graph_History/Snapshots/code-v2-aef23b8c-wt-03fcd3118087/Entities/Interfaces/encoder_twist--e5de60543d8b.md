---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:encoder-twist"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:encoder-twist"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:encoder-twist"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/encoder_twist"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "47d79fea2df961193c6b49f995bc9c2c352011b28d56fc678112b78514348797"
relation_fingerprint: "b64ca537453ec767f516b2b7bdbb857c5f77b815de0bb29a641969e5770feb0e"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /encoder_twist

- 逻辑实体：`agv:ros:interface:encoder-twist`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:encoder-twist`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/odometer/src/odometer.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | geometry_msgs/TwistStamped |
| `ros_name` | /encoder_twist |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_perception/src/perception_aggregator_node.cpp` | 54 | `subscribes` | `5b988700b3ea59236ab37c28ca7d0b4bd1dc66b69bf3328b71245d703f16d089` |
| `src/encoder/src/rb100_encoder.cpp` | 413 | `publishes` | `7606db8a8175b2049da2c09f11abbf03ca27b57029c298c14fd25c0a42513000` |
| `src/odometer/src/odometer.cpp` | 155 | `publishes` | `f1a235cae5e0fa57a303bd0b2853cf7498f75249ece10e5749a43b69210c8bb6` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_perception--b3844e0c0c3f|agv:ros:package:agv_perception]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/encoder--0240516ec77b|agv:ros:package:encoder]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/odometer--6b13553e3c5a|agv:ros:package:odometer]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/odometer--4d91289aece7|agv:ros:node:odometer]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/rb100_encoder--a141ed92ecec|agv:ros:node:rb100_encoder]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/perception_aggregator_node--38fa4d21e1c4|agv:ros:node:perception_aggregator_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/encoder-twist--e5de60543d8b|agv:ros:interface:encoder-twist]]
