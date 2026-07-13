---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:imu-data"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:imu-data"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:imu-data"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/imu/data"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "2cdd7f4ff44ad442f2e2a581643f044c42e7a051cf712d903c2847f3f2fab2ae"
relation_fingerprint: "139fee096fe4b2badda2446ff8424ad14ec2af4b3099988025407e010baeefeb"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /imu/data

- 逻辑实体：`agv:ros:interface:imu-data`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:imu-data`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_perception/src/perception_aggregator_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | unknown |
| `ros_name` | /imu/data |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_perception/src/perception_aggregator_node.cpp` | 52 | `subscribes` | `5b988700b3ea59236ab37c28ca7d0b4bd1dc66b69bf3328b71245d703f16d089` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_perception--b3844e0c0c3f|agv:ros:package:agv_perception]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/perception_aggregator_node--38fa4d21e1c4|agv:ros:node:perception_aggregator_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/imu-data--db8576d5b420|agv:ros:interface:imu-data]]
