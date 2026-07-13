---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_mqtt_bridge"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:agv_mqtt_bridge"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_mqtt_bridge"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "agv_mqtt_bridge"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "7e1cf51a745dc15072bd61a369e0cfabea65c9d308e1089ced8a474e9119f872"
relation_fingerprint: "7f448f010d8ae21f4e0cea432d5d8aeac70f389383be3423543e054f9ef1a5f0"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# agv_mqtt_bridge

- 逻辑实体：`agv:ros:package:agv_mqtt_bridge`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_mqtt_bridge`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/agv_mqtt_bridge/package.xml`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` |  |
| `status` | active |
| `type` | ros_package |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` | 0.1.0 |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_mqtt_bridge/package.xml` | 1 | `package_manifest` | `e5f26fa90caac77c64645a276f60cdc7d6882e85dc9712dc7f0c3a6aa3ca9919` |

## 出向关系

- `depends_on` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/h56br_driver--8cf5e3bb73a1|agv:ros:package:h56br_driver]]
- `depends_on` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/magnetic_controlled_motor--8bee0b922a0e|agv:ros:package:magnetic_controlled_motor]]
- `depends_on` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/ultrasonic_controlled_motor--2e98007ce616|agv:ros:package:ultrasonic_controlled_motor]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/agv_mqtt_bridge--81622ebf066a|agv:ros:node:agv_mqtt_bridge]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv-task_state--5dfdad5e839f|agv:ros:interface:agv-task-state]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-current--994c4cef7d41|agv:ros:interface:battery-h56br-current]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-soc--fb01514bedd7|agv:ros:interface:battery-h56br-soc]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-status--355f7fc2c130|agv:ros:interface:battery-h56br-status]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-voltage--dbc3b1489da1|agv:ros:interface:battery-h56br-voltage]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/fused_odom--e73c04c78ed4|agv:ros:interface:fused-odom]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu--4caf2e58d1e5|agv:ros:interface:imu]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_line_position--13fdee899244|agv:ros:interface:mag-line-position]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_sensor-frame--dec47a778ef7|agv:ros:interface:mag-sensor-frame]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_sensor-nail_event--f74eeb1e095f|agv:ros:interface:mag-sensor-nail-event]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_brake--1d9a50d19a77|agv:ros:interface:motor-brake]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/odom--1e74762c157b|agv:ros:interface:odom]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/PowerVoltage--a406ef04e1cc|agv:ros:interface:powervoltage]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory_status--d64b6a185c5c|agv:ros:interface:trajectory-status]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-ultrasonic_state--c42cfd559c46|agv:ros:interface:trajectory-ultrasonic-state]] → `related_packages`

## 相对 V1 的变化

- `unchanged`：语义指纹与 V1 一致。
