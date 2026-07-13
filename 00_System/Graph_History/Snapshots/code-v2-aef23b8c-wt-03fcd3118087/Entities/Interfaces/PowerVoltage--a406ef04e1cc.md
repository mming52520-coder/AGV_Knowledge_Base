---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:powervoltage"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:powervoltage"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:powervoltage"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/PowerVoltage"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "2d88b3c6cca929ac1b42dec5feaa322b39e03a5e7e814441e79f586743f43ca8"
relation_fingerprint: "e545f246c39223652fd223a0fe89b9f8e83632c09269f9bf3d7f26b8260b05b8"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /PowerVoltage

- 逻辑实体：`agv:ros:interface:powervoltage`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:powervoltage`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | std_msgs/Float32 |
| `ros_name` | /PowerVoltage |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py` | 393 | `subscribes` | `e424ea32f29a7a5ba2b1e946cebd289ef2c0f4092b76dc1ebffc0db0b25116a2` |
| `src/wheeltec_base/src/wheeltec_robot.cpp` | 299 | `publishes` | `48ac16949d4c430b1c20fd50685f08402e2dbd589ef9b8e353255d916dc77bdc` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mqtt_bridge--001d465b2aae|agv:ros:package:agv_mqtt_bridge]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/wheeltec_base--57353db6783a|agv:ros:package:wheeltec_base]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/wheeltec_robot_node--790717f1d34c|agv:ros:node:wheeltec_robot_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/agv_mqtt_bridge--81622ebf066a|agv:ros:node:agv_mqtt_bridge]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/powervoltage--a406ef04e1cc|agv:ros:interface:powervoltage]]
