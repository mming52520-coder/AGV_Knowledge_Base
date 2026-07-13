---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:ultrasonic_follower"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:ultrasonic_follower"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:ultrasonic_follower"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "ultrasonic_follower"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "e6e815f17a5253430367a9919c31452651612d51ae02e942392ee6f447697198"
relation_fingerprint: "25ba6af307c65af450772c9d6792141d422f4a06dd173d3d4d869fcd527ff7a5"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# ultrasonic_follower

- 逻辑实体：`agv:ros:node:ultrasonic_follower`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:ultrasonic_follower`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/ultrasonic_controlled_motor/src/ultrasonic_follower.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | ultrasonic_follower |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /ultrasonic_follower |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/ultrasonic_controlled_motor/src/ultrasonic_follower.cpp` | 1 | `node_source` | `c2e42cb4e99c9db9bcc1e01ff9cc5993f92d1f639a9091c4d6bee169b168ef87` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/ultrasonic_controlled_motor--2e98007ce616|agv:ros:package:ultrasonic_controlled_motor]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_distance--1240d1cca41f|agv:ros:interface:ultrasonic-left-distance]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-right_distance--ce2626276c17|agv:ros:interface:ultrasonic-right-distance]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/ultrasonic_follower--a7eeb0b895ef|agv:ros:node:ultrasonic_follower]]
