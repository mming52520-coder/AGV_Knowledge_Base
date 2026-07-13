---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:magnetic_follower"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:magnetic_follower"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:magnetic_follower"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "magnetic_follower"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "1cf77b91eaacfa3ab9a9bb9070e28888e2b962bddaf8aa504dcb54073fb5cb65"
relation_fingerprint: "d679fc4431320375b480a1b5e89b250e4770b0ef9c2de431adb517082859fc57"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# magnetic_follower

- 逻辑实体：`agv:ros:node:magnetic_follower`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:magnetic_follower`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/magnetic_controlled_motor/src/magnetic_follower.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | magnetic_follower |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /magnetic_follower |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/magnetic_controlled_motor/src/magnetic_follower.cpp` | 1 | `node_source` | `d938df1cb95b9ed230679ae2dbf2b39ab2fd982dde3b6623cbdc6bcbafa89f3e` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/magnetic_controlled_motor--8bee0b922a0e|agv:ros:package:magnetic_controlled_motor]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_line_position--13fdee899244|agv:ros:interface:mag-line-position]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_sensor-raw_data--3fe1ffbe0e59|agv:ros:interface:mag-sensor-raw-data]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`ros_name`, `status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/magnetic_follower--7aec69b0ba38|agv:ros:node:magnetic_follower]]
