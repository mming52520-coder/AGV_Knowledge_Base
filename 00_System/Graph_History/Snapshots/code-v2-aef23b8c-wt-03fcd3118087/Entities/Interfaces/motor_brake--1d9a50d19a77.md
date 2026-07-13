---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:motor-brake"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:motor-brake"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:motor-brake"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/motor_brake"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "360a4893b869afc99c399102ba25ae22d2b7bb460b394f10e1ba6e87fbd8b017"
relation_fingerprint: "6812620a016ff201e5995c82c00ca20137e06f550ae986c9fa69d8bf0924d5da"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /motor_brake

- 逻辑实体：`agv:ros:interface:motor-brake`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:motor-brake`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | std_msgs/UInt8 |
| `ros_name` | /motor_brake |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | [] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py` | 418 | `subscribes` | `e424ea32f29a7a5ba2b1e946cebd289ef2c0f4092b76dc1ebffc0db0b25116a2` |
| `src/relay/src/hk_dio_remote.cpp` | 131 | `subscribes` | `1fd77d8d9fba04ed1d9fa044a699462373798f299e3c105179bb8c910e966857` |
| `src/remote_ctrl/src/remote_controller.cpp` | 73 | `publishes` | `6487d9d6f0dbdbb257a4a21816c73c5f056dd26a987b8d1eba132452d1c9b98d` |
| `src/wheeltec_base/src/cmd_vel_adapter.cpp` | 50 | `subscribes` | `68c1dcce28d60b85c990697c7cbe394a3fc4d99035eb4f6a13440fc69665359c` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mqtt_bridge--001d465b2aae|agv:ros:package:agv_mqtt_bridge]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/relay--7e8f04764da5|agv:ros:package:relay]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/remote_ctrl--081aafab18b5|agv:ros:package:remote_ctrl]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/wheeltec_base--57353db6783a|agv:ros:package:wheeltec_base]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/remote_controller--64f1746fd3dc|agv:ros:node:remote_controller]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/agv_mqtt_bridge--81622ebf066a|agv:ros:node:agv_mqtt_bridge]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/cmd_vel_adapter--fcd537fae350|agv:ros:node:cmd_vel_adapter]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/hk_dio_remote--d5b6ebdf80e7|agv:ros:node:hk_dio_remote]] → `subscribes`

## 相对 V1 的变化

- `unchanged`：语义指纹与 V1 一致。
