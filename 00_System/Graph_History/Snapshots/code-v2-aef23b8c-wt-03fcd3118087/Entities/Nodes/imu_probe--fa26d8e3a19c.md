---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:imu_probe"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:imu_probe"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:imu_probe"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "imu_probe"
status: "diagnostic"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "357858530d7937a4393e033063362d05206b08a8f64c1145a632386c9cdb95f7"
relation_fingerprint: "c4d59b649400f87c94090e837b96002d8d125e726acb129319bafb9eae29f40a"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# imu_probe

- 逻辑实体：`agv:ros:node:imu_probe`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:imu_probe`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/trajectory_recorder/src/imu_probe_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | imu_probe |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /imu_probe |
| `status` | diagnostic |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/trajectory_recorder/src/imu_probe_node.cpp` | 1 | `node_source` | `d399fcd6ee93484284c6bda916e1112cf92cd5a3c8aed27faf58446e3c81bb0f` |
| `src/trajectory_recorder/src/imu_sensor.cpp` | 1 | `node_source` | `656f10b54cdc8479217a97688811263b1c7c5f466faf93838aa68f090d201c1b` |
| `src/trajectory_recorder/src/serial_port.cpp` | 1 | `node_source` | `7755904f6bf452fe9e6247621e14eef23031735825301b448ba6ac762096791f` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu-probe_data--dd6a95a4889e|agv:ros:interface:imu-probe-data]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu-probe_rpy_deg--fb8aa34c79ce|agv:ros:interface:imu-probe-rpy-deg]]

## 入向关系

- 无

## 相对 V1 的变化

- `unchanged`：语义指纹与 V1 一致。
