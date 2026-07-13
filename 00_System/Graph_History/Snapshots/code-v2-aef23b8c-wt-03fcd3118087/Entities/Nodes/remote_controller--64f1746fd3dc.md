---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:remote_controller"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:remote_controller"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:remote_controller"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "remote_controller"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "8363b791ce56ff7d8e86c1ed37fdd9593951e9eab812c4b2e7cb9b0dd5abf9fc"
relation_fingerprint: "69b109820ce50e593260e33732142b4b3f525d502eec7396b155c94e321d405c"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# remote_controller

- 逻辑实体：`agv:ros:node:remote_controller`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:remote_controller`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/remote_ctrl/src/remote_controller.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | remote_controller |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /remote_controller |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/remote_ctrl/src/remote_controller.cpp` | 1 | `node_source` | `6487d9d6f0dbdbb257a4a21816c73c5f056dd26a987b8d1eba132452d1c9b98d` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/remote_ctrl--081aafab18b5|agv:ros:package:remote_ctrl]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_brake--1d9a50d19a77|agv:ros:interface:motor-brake]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/joy--8ee95575fdb7|agv:ros:interface:joy]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-front_status--9cf5e5dd81ab|agv:ros:interface:ultrasonic-front-status]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-rear_status--4db4f184e714|agv:ros:interface:ultrasonic-rear-status]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/remote_controller--64f1746fd3dc|agv:ros:node:remote_controller]]
