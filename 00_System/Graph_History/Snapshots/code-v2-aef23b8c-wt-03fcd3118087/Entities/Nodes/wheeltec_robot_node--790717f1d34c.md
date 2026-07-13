---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:wheeltec_robot_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:wheeltec_robot_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:wheeltec_robot_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "wheeltec_robot_node"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "5a4664313edc5d5f03a4c8491f80b78906f694a58fac566cc0bc47c1a180028f"
relation_fingerprint: "2b1137af33d5eb30ef2d5ba7eb6c717fa7d621b62b15970b8189aedf168042e1"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# wheeltec_robot_node

- 逻辑实体：`agv:ros:node:wheeltec_robot_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:wheeltec_robot_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/wheeltec_base/src/wheeltec_robot.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | wheeltec_robot_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /wheeltec_robot |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/wheeltec_base/src/Quaternion_Solution.cpp` | 1 | `node_source` | `99510b32fcb41a6db4a813707b236180546ec3024ad21d02df9e61f8e5fad0a5` |
| `src/wheeltec_base/src/wheeltec_robot.cpp` | 1 | `node_source` | `48ac16949d4c430b1c20fd50685f08402e2dbd589ef9b8e353255d916dc77bdc` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/wheeltec_base--57353db6783a|agv:ros:package:wheeltec_base]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu--4caf2e58d1e5|agv:ros:interface:imu]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/odom--1e74762c157b|agv:ros:interface:odom]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/PowerVoltage--a406ef04e1cc|agv:ros:interface:powervoltage]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/cmd_vel--64adee285a61|agv:ros:interface:cmd-vel]]

## 入向关系

- 无

## 相对 V1 的变化

- `unchanged`：语义指纹与 V1 一致。
