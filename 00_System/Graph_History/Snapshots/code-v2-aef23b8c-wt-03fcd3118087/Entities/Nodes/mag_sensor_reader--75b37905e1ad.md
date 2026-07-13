---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:mag_sensor_reader"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:mag_sensor_reader"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:mag_sensor_reader"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "mag_sensor_reader"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "b6d25f3a8aa317d2e15c37c476e9525fae1dad092f7c50dd9b93c742c444324a"
relation_fingerprint: "98ac604348772287cefeabddc2ba3dd0676d20c9543aef38f50bb0c0572aa717"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# mag_sensor_reader

- 逻辑实体：`agv:ros:node:mag_sensor_reader`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:mag_sensor_reader`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/magnetic_controlled_motor/src/mag_sensor_reader.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | mag_sensor_reader |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /mag_sensor_reader |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/magnetic_controlled_motor/src/line_offset_estimator.cpp` | 1 | `node_source` | `cea39a17030e4ff2023093c414ad449ac66fd0c7376fe0a1418cbd802ec4ccfc` |
| `src/magnetic_controlled_motor/src/mag_nail_detector.cpp` | 1 | `node_source` | `238b24071dc6593d15ad437b82a8888a900a58fce3dcd521dd369b35fbf410a6` |
| `src/magnetic_controlled_motor/src/mag_sensor_reader.cpp` | 1 | `node_source` | `797901497a916acd47ee0239f4aad93751863125c85f5b8ab633c5d4d8238480` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/magnetic_controlled_motor--8bee0b922a0e|agv:ros:package:magnetic_controlled_motor]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_sensor-frame--dec47a778ef7|agv:ros:interface:mag-sensor-frame]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_sensor-nail_event--f74eeb1e095f|agv:ros:interface:mag-sensor-nail-event]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_sensor-raw_data--3fe1ffbe0e59|agv:ros:interface:mag-sensor-raw-data]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/odom--1e74762c157b|agv:ros:interface:odom]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`ros_name`, `status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/mag_sensor_reader--75b37905e1ad|agv:ros:node:mag_sensor_reader]]
