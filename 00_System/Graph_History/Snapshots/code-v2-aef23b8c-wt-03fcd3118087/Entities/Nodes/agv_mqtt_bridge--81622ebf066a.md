---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:agv_mqtt_bridge"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:agv_mqtt_bridge"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:agv_mqtt_bridge"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "agv_mqtt_bridge"
status: "available"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "69d985143a60158cc46ddf6b8480a58973088cd7757a8adc455b25c9f481cfa4"
relation_fingerprint: "20310cb0c4e5e988a3bbcaea15e8f7104d59e8d13e851b0b427f8d86ad84d490"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# agv_mqtt_bridge

- 逻辑实体：`agv:ros:node:agv_mqtt_bridge`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:agv_mqtt_bridge`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | agv_mqtt_bridge |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /agv_mqtt_bridge |
| `status` | available |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py` | 1 | `node_source` | `e424ea32f29a7a5ba2b1e946cebd289ef2c0f4092b76dc1ebffc0db0b25116a2` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mqtt_bridge--001d465b2aae|agv:ros:package:agv_mqtt_bridge]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv-task_state--5dfdad5e839f|agv:ros:interface:agv-task-state]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-current--994c4cef7d41|agv:ros:interface:battery-h56br-current]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-soc--fb01514bedd7|agv:ros:interface:battery-h56br-soc]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-status--355f7fc2c130|agv:ros:interface:battery-h56br-status]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-voltage--dbc3b1489da1|agv:ros:interface:battery-h56br-voltage]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/fused_odom--e73c04c78ed4|agv:ros:interface:fused-odom]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu--4caf2e58d1e5|agv:ros:interface:imu]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_line_position--13fdee899244|agv:ros:interface:mag-line-position]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_sensor-frame--dec47a778ef7|agv:ros:interface:mag-sensor-frame]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_sensor-nail_event--f74eeb1e095f|agv:ros:interface:mag-sensor-nail-event]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_brake--1d9a50d19a77|agv:ros:interface:motor-brake]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/odom--1e74762c157b|agv:ros:interface:odom]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/PowerVoltage--a406ef04e1cc|agv:ros:interface:powervoltage]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory_status--d64b6a185c5c|agv:ros:interface:trajectory-status]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-ultrasonic_state--c42cfd559c46|agv:ros:interface:trajectory-ultrasonic-state]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`executable`, `status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/agv_mqtt_bridge--81622ebf066a|agv:ros:node:agv_mqtt_bridge]]
