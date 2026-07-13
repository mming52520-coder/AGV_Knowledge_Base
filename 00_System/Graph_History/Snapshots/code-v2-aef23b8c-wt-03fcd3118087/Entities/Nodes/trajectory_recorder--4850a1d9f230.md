---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:trajectory_recorder"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:trajectory_recorder"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:trajectory_recorder"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "trajectory_recorder"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "8d28027056850417057303d73ac2728f44d0c61bfe5f70575ee079e0b20699d1"
relation_fingerprint: "f664af542d6dfa5881deb9a9baa4a5b6dcd587be3c1d7ccf7fd8d8a2dc7f703a"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# trajectory_recorder

- 逻辑实体：`agv:ros:node:trajectory_recorder`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:trajectory_recorder`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/trajectory_recorder/src/trajectory_recorder.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | trajectory_recorder |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /trajectory_recorder |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/trajectory_recorder/src/trajectory_recorder.cpp` | 1 | `node_source` | `c971b301b5907f52e00034491d77dcf5c8beb9cd04b67ef4ab2c5d5b97afa8c6` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu-reset_calibration--92101a8c204c|agv:ros:service:imu-reset-calibration]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu-set_forward--a8b86ae4edbd|agv:ros:service:imu-set-forward]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu-set_zero--cafbe217e891|agv:ros:service:imu-set-zero]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-save--b7dbb55b5e17|agv:ros:service:trajectory-save]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-start_record--d1ef1c28d4da|agv:ros:service:trajectory-start-record]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-stop_record--2819b569b2db|agv:ros:service:trajectory-stop-record]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/encoder_angle--bca3ba1cc686|agv:ros:interface:encoder-angle]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/fused_odom--e73c04c78ed4|agv:ros:interface:fused-odom]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/odom--1e74762c157b|agv:ros:interface:odom]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_sensor-frame--dec47a778ef7|agv:ros:interface:mag-sensor-frame]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_sensor-nail_event--f74eeb1e095f|agv:ros:interface:mag-sensor-nail-event]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-front_distance--f2df0d6f13fc|agv:ros:interface:ultrasonic-front-distance]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_distance--1240d1cca41f|agv:ros:interface:ultrasonic-left-distance]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-rear_distance--875cdec8b4fb|agv:ros:interface:ultrasonic-rear-distance]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-right_distance--ce2626276c17|agv:ros:interface:ultrasonic-right-distance]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/trajectory_recorder--4850a1d9f230|agv:ros:node:trajectory_recorder]]
