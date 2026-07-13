---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:motor-command"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:motor-command"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:motor-command"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/motor_command"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "93f861e49734ea5ab30f54a581b253265fa791f27020bfdac7e337143c8cb20a"
relation_fingerprint: "50f47a7094d90f3734256b04d0d743bd8672d8ccd7deb1a1635b867fe03f8834"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /motor_command

- 逻辑实体：`agv:ros:interface:motor-command`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:motor-command`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | std_msgs/String |
| `ros_name` | /motor_command |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | [] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_execution/src/chassis_gateway_node.cpp` | 51 | `publishes` | `f30568932c8e70e73f4ee7677a7d3905faa2e11bc0864fa8547c64a92e3b60b7` |
| `src/agv_legacy/src/legacy_command_adapter.cpp` | 21 | `publishes` | `fa4aef04bb56c36e83a3ca8f01ef53b7482c8583a11473a4a6a74259e2fa3901` |
| `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py` | 408 | `subscribes` | `e424ea32f29a7a5ba2b1e946cebd289ef2c0f4092b76dc1ebffc0db0b25116a2` |
| `src/magnetic_controlled_motor/src/magnetic_follower.cpp` | 56 | `publishes` | `d938df1cb95b9ed230679ae2dbf2b39ab2fd982dde3b6623cbdc6bcbafa89f3e` |
| `src/magnetic_controlled_motor/src/motor_control.cpp` | 363 | `subscribes` | `ab9568f051ef72710b082c9e9cec34b37bd25b5e92927022100140dce99cb235` |
| `src/remote_ctrl/src/remote_controller.cpp` | 71 | `publishes` | `6487d9d6f0dbdbb257a4a21816c73c5f056dd26a987b8d1eba132452d1c9b98d` |
| `src/trajectory_recorder/src/steering_remote.cpp` | 39 | `subscribes` | `6b7c2094990cf9c047b8febda758d18ff8d2d8e15d2f97eed2156169df2eab76` |
| `src/trajectory_recorder/src/trajectory_recorder.cpp` | 877 | `subscribes` | `c971b301b5907f52e00034491d77dcf5c8beb9cd04b67ef4ab2c5d5b97afa8c6` |
| `src/trajectory_recorder/src/trajectory_tracker.cpp` | 3800 | `publishes` | `b13ba9a028ec7abd7b3956173e7cc20bc3a123038872ec4ea9c3a159ccf795c7` |
| `src/ultrasonic_controlled_motor/src/motor_control.cpp` | 363 | `subscribes` | `ebf562123626197cefe449061c90c82f3f91198da65ef1e7ddc88f703b112269` |
| `src/ultrasonic_controlled_motor/src/ultrasonic_follower.cpp` | 59 | `publishes` | `c2e42cb4e99c9db9bcc1e01ff9cc5993f92d1f639a9091c4d6bee169b168ef87` |
| `src/wheeltec_base/src/cmd_vel_adapter.cpp` | 48 | `subscribes` | `68c1dcce28d60b85c990697c7cbe394a3fc4d99035eb4f6a13440fc69665359c` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_execution--855e548bdcfd|agv:ros:package:agv_execution]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_legacy--db70b74c409e|agv:ros:package:agv_legacy]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mqtt_bridge--001d465b2aae|agv:ros:package:agv_mqtt_bridge]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/magnetic_controlled_motor--8bee0b922a0e|agv:ros:package:magnetic_controlled_motor]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/remote_ctrl--081aafab18b5|agv:ros:package:remote_ctrl]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/ultrasonic_controlled_motor--2e98007ce616|agv:ros:package:ultrasonic_controlled_motor]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/wheeltec_base--57353db6783a|agv:ros:package:wheeltec_base]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/chassis_gateway_node--e753a2e58776|agv:ros:node:chassis_gateway_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/legacy_command_adapter--30863753bf07|agv:ros:node:legacy_command_adapter]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/magnetic_follower--7aec69b0ba38|agv:ros:node:magnetic_follower]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/remote_controller--64f1746fd3dc|agv:ros:node:remote_controller]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_tracker--3031ab8e89fc|agv:ros:node:trajectory_tracker]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/ultrasonic_follower--a7eeb0b895ef|agv:ros:node:ultrasonic_follower]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/agv_mqtt_bridge--81622ebf066a|agv:ros:node:agv_mqtt_bridge]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/cmd_vel_adapter--fcd537fae350|agv:ros:node:cmd_vel_adapter]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/magnetic_motor_control--463962ff9429|agv:ros:node:magnetic_motor_control]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/steering_remote--9fadaeb1fc6d|agv:ros:node:steering_remote]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_recorder--4850a1d9f230|agv:ros:node:trajectory_recorder]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/ultrasonic_motor_control--2b3b9310ac71|agv:ros:node:ultrasonic_motor_control]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/motor-command--6f8461f1fd20|agv:ros:interface:motor-command]]
