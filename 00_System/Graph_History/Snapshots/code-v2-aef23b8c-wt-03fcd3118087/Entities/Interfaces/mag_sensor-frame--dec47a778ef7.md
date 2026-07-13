---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mag-sensor-frame"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:mag-sensor-frame"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mag-sensor-frame"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/mag_sensor/frame"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "75bea89dd376f87b743c877c143785895a378b2b63a65d8339c2a97f6da4be82"
relation_fingerprint: "4757422af20fd3f90c702669e6561003a3129c1f33752846a0ef747d3d2a2ba0"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /mag_sensor/frame

- 逻辑实体：`agv:ros:interface:mag-sensor-frame`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mag-sensor-frame`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | magnetic_controlled_motor/MagFrame |
| `ros_name` | /mag_sensor/frame |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | [] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py` | 473 | `subscribes` | `e424ea32f29a7a5ba2b1e946cebd289ef2c0f4092b76dc1ebffc0db0b25116a2` |
| `src/agv_perception/src/perception_aggregator_node.cpp` | 50 | `subscribes` | `5b988700b3ea59236ab37c28ca7d0b4bd1dc66b69bf3328b71245d703f16d089` |
| `src/magnetic_controlled_motor/src/mag_sensor_reader.cpp` | 71 | `publishes` | `797901497a916acd47ee0239f4aad93751863125c85f5b8ab633c5d4d8238480` |
| `src/trajectory_recorder/src/trajectory_recorder.cpp` | 879 | `subscribes` | `c971b301b5907f52e00034491d77dcf5c8beb9cd04b67ef4ab2c5d5b97afa8c6` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mqtt_bridge--001d465b2aae|agv:ros:package:agv_mqtt_bridge]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_perception--b3844e0c0c3f|agv:ros:package:agv_perception]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/magnetic_controlled_motor--8bee0b922a0e|agv:ros:package:magnetic_controlled_motor]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/mag_sensor_reader--75b37905e1ad|agv:ros:node:mag_sensor_reader]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/agv_mqtt_bridge--81622ebf066a|agv:ros:node:agv_mqtt_bridge]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/perception_aggregator_node--38fa4d21e1c4|agv:ros:node:perception_aggregator_node]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_recorder--4850a1d9f230|agv:ros:node:trajectory_recorder]] → `subscribes`

## 相对 V1 的变化

- `unchanged`：语义指纹与 V1 一致。
