---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mag-sensor-nail-event"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:mag-sensor-nail-event"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mag-sensor-nail-event"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/mag_sensor/nail_event"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "50d8a21b4f23b1181055d338d6333794d3815bb38d4a8db4b5a9b4550b4cc8a8"
relation_fingerprint: "d0335c4e6072a8e15da0ce0ff2eb4409ae50b281742c78e1b67b38c7cb0c68a2"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /mag_sensor/nail_event

- 逻辑实体：`agv:ros:interface:mag-sensor-nail-event`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mag-sensor-nail-event`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | magnetic_controlled_motor/MagNailEvent |
| `ros_name` | /mag_sensor/nail_event |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | [] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py` | 478 | `subscribes` | `e424ea32f29a7a5ba2b1e946cebd289ef2c0f4092b76dc1ebffc0db0b25116a2` |
| `src/magnetic_controlled_motor/src/mag_sensor_reader.cpp` | 72 | `publishes` | `797901497a916acd47ee0239f4aad93751863125c85f5b8ab633c5d4d8238480` |
| `src/trajectory_recorder/src/trajectory_recorder.cpp` | 881 | `subscribes` | `c971b301b5907f52e00034491d77dcf5c8beb9cd04b67ef4ab2c5d5b97afa8c6` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mqtt_bridge--001d465b2aae|agv:ros:package:agv_mqtt_bridge]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/magnetic_controlled_motor--8bee0b922a0e|agv:ros:package:magnetic_controlled_motor]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/mag_sensor_reader--75b37905e1ad|agv:ros:node:mag_sensor_reader]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/agv_mqtt_bridge--81622ebf066a|agv:ros:node:agv_mqtt_bridge]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_recorder--4850a1d9f230|agv:ros:node:trajectory_recorder]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/mag-sensor-nail-event--f74eeb1e095f|agv:ros:interface:mag-sensor-nail-event]]
