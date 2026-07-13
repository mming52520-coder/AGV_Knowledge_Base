---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:imu-probe-data"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:imu-probe-data"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:imu-probe-data"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/imu/probe_data"
status: "diagnostic"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "c0694253d035e54a19b8e7363144fc8e1c90118001aced9f0442c84e0c26dcb8"
relation_fingerprint: "8886ec903082171858d73172b2179b3a8356bb7d91272905000c0134968af92c"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /imu/probe_data

- 逻辑实体：`agv:ros:interface:imu-probe-data`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:imu-probe-data`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/trajectory_recorder/src/imu_probe_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | sensor_msgs/Imu |
| `ros_name` | /imu/probe_data |
| `status` | diagnostic |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/trajectory_recorder/src/imu_probe_node.cpp` | 107 | `publishes` | `d399fcd6ee93484284c6bda916e1112cf92cd5a3c8aed27faf58446e3c81bb0f` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/imu_probe--fa26d8e3a19c|agv:ros:node:imu_probe]] → `publishes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/imu-probe-data--dd6a95a4889e|agv:ros:interface:imu-probe-data]]
