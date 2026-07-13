---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mag-sensor-raw-data"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:mag-sensor-raw-data"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mag-sensor-raw-data"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/mag_sensor/raw_data"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "994b520c8e61e067a3ad6aef055ac0f297cffcc30f62f6e889ad5ea0881d2a2c"
relation_fingerprint: "cec6b281c1ba2a2acd938f878e1b454ee7928d7777dd7ae840f93edd1dae924a"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /mag_sensor/raw_data

- 逻辑实体：`agv:ros:interface:mag-sensor-raw-data`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mag-sensor-raw-data`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/magnetic_controlled_motor/src/mag_sensor_reader.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | std_msgs/UInt16 |
| `ros_name` | /mag_sensor/raw_data |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | [] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/magnetic_controlled_motor/src/mag_sensor_reader.cpp` | 70 | `publishes` | `797901497a916acd47ee0239f4aad93751863125c85f5b8ab633c5d4d8238480` |
| `src/magnetic_controlled_motor/src/magnetic_follower.cpp` | 53 | `subscribes` | `d938df1cb95b9ed230679ae2dbf2b39ab2fd982dde3b6623cbdc6bcbafa89f3e` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/magnetic_controlled_motor--8bee0b922a0e|agv:ros:package:magnetic_controlled_motor]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/mag_sensor_reader--75b37905e1ad|agv:ros:node:mag_sensor_reader]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/magnetic_follower--7aec69b0ba38|agv:ros:node:magnetic_follower]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/mag-sensor-raw-data--3fe1ffbe0e59|agv:ros:interface:mag-sensor-raw-data]]
