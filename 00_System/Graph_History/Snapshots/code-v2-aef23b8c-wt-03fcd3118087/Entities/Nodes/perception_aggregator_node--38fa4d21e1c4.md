---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:perception_aggregator_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:perception_aggregator_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:perception_aggregator_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "perception_aggregator_node"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "aff886d8d8b4008ca5d1e1f37a6dace6cb44d4113f2c028732744d5607fcd94c"
relation_fingerprint: "d391b0db63333077ee1e175732463fb3f5df03028a675e4adf4f2d5c6fc10dfd"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# perception_aggregator_node

- 逻辑实体：`agv:ros:node:perception_aggregator_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:perception_aggregator_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_perception/src/perception_aggregator_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | perception_aggregator_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /perception_aggregator_node |
| `status` | active |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_perception/src/perception_aggregator_node.cpp` | 1 | `node_source` | `5b988700b3ea59236ab37c28ca7d0b4bd1dc66b69bf3328b71245d703f16d089` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_perception--b3844e0c0c3f|agv:ros:package:agv_perception]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/perception-health--8c7afd3dc0e7|agv:ros:interface:perception-health]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/perception-state--9e4cc739ed14|agv:ros:interface:perception-state]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-soc--fb01514bedd7|agv:ros:interface:battery-h56br-soc]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-voltage--dbc3b1489da1|agv:ros:interface:battery-h56br-voltage]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/encoder_twist--e5de60543d8b|agv:ros:interface:encoder-twist]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu-data--db8576d5b420|agv:ros:interface:imu-data]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_sensor-frame--dec47a778ef7|agv:ros:interface:mag-sensor-frame]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-distances--95d581d0b6c4|agv:ros:interface:ultrasonic-distances]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/perception_aggregator_node--38fa4d21e1c4|agv:ros:node:perception_aggregator_node]]
