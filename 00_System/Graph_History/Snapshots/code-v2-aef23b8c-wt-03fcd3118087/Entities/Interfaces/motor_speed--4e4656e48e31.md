---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:motor-speed"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:motor-speed"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:motor-speed"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/motor_speed"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "d672011f50008e1c825016c860e164de6dc107dd87a19f3ced9161bfe3315cdb"
relation_fingerprint: "1cb754144bb10d0a6c2460f188d78142062785bf9cdf19e0061419308bd27eba"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /motor_speed

- 逻辑实体：`agv:ros:interface:motor-speed`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:motor-speed`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | std_msgs/Float32 |
| `ros_name` | /motor_speed |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | [] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_execution/src/chassis_gateway_node.cpp` | 50 | `publishes` | `f30568932c8e70e73f4ee7677a7d3905faa2e11bc0864fa8547c64a92e3b60b7` |
| `src/agv_legacy/src/legacy_command_adapter.cpp` | 20 | `publishes` | `fa4aef04bb56c36e83a3ca8f01ef53b7482c8583a11473a4a6a74259e2fa3901` |
| `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py` | 413 | `subscribes` | `e424ea32f29a7a5ba2b1e946cebd289ef2c0f4092b76dc1ebffc0db0b25116a2` |
| `src/analog_controlled_motor/src/hk_ao.cpp` | 638 | `subscribes` | `4abb47a3ae0bfc52fc897c4a764b2e3e493b543be17841b8eba35fce8857ef2b` |
| `src/analog_controlled_motor/src/hk_ao_remote.cpp` | 144 | `subscribes` | `bf76aaa1481cf51f10a7cf3b259a71e486c1f6f181de400d831b0c7fe129238f` |
| `src/magnetic_controlled_motor/src/magnetic_follower.cpp` | 57 | `publishes` | `d938df1cb95b9ed230679ae2dbf2b39ab2fd982dde3b6623cbdc6bcbafa89f3e` |
| `src/relay/src/hk_dio_remote.cpp` | 130 | `subscribes` | `1fd77d8d9fba04ed1d9fa044a699462373798f299e3c105179bb8c910e966857` |
| `src/remote_ctrl/src/remote_controller.cpp` | 72 | `publishes` | `6487d9d6f0dbdbb257a4a21816c73c5f056dd26a987b8d1eba132452d1c9b98d` |
| `src/trajectory_recorder/src/trajectory_recorder.cpp` | 875 | `subscribes` | `c971b301b5907f52e00034491d77dcf5c8beb9cd04b67ef4ab2c5d5b97afa8c6` |
| `src/trajectory_recorder/src/trajectory_tracker.cpp` | 3799 | `publishes` | `b13ba9a028ec7abd7b3956173e7cc20bc3a123038872ec4ea9c3a159ccf795c7` |
| `src/ultrasonic_controlled_motor/src/ultrasonic_follower.cpp` | 60 | `publishes` | `c2e42cb4e99c9db9bcc1e01ff9cc5993f92d1f639a9091c4d6bee169b168ef87` |
| `src/wheeltec_base/src/cmd_vel_adapter.cpp` | 49 | `subscribes` | `68c1dcce28d60b85c990697c7cbe394a3fc4d99035eb4f6a13440fc69665359c` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_execution--855e548bdcfd|agv:ros:package:agv_execution]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_legacy--db70b74c409e|agv:ros:package:agv_legacy]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mqtt_bridge--001d465b2aae|agv:ros:package:agv_mqtt_bridge]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/analog_controlled_motor--7f945fabfb29|agv:ros:package:analog_controlled_motor]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/magnetic_controlled_motor--8bee0b922a0e|agv:ros:package:magnetic_controlled_motor]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/relay--7e8f04764da5|agv:ros:package:relay]]
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
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/hk_ao--b087e142fee2|agv:ros:node:hk_ao]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/hk_ao_remote--ad5e24d09dba|agv:ros:node:hk_ao_remote]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/hk_dio_remote--d5b6ebdf80e7|agv:ros:node:hk_dio_remote]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_recorder--4850a1d9f230|agv:ros:node:trajectory_recorder]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/motor-speed--4e4656e48e31|agv:ros:interface:motor-speed]]
