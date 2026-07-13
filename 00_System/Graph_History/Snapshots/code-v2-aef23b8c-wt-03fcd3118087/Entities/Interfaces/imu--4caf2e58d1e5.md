---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:imu"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:imu"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:imu"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/imu"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "3b0f5dc7b340c66e3b8578e19fc4142fce5a5f2910239bf2416db1c9d582b020"
relation_fingerprint: "bdb6fea47cc83c2bb821d05ce057611a1ec4cf4f674ca528ab243624806d8a0e"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /imu

- 逻辑实体：`agv:ros:interface:imu`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:imu`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | sensor_msgs/Imu |
| `ros_name` | /imu |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | [] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py` | 392 | `subscribes` | `e424ea32f29a7a5ba2b1e946cebd289ef2c0f4092b76dc1ebffc0db0b25116a2` |
| `src/wheeltec_base/src/wheeltec_robot.cpp` | 301 | `publishes` | `48ac16949d4c430b1c20fd50685f08402e2dbd589ef9b8e353255d916dc77bdc` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mqtt_bridge--001d465b2aae|agv:ros:package:agv_mqtt_bridge]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/wheeltec_base--57353db6783a|agv:ros:package:wheeltec_base]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/wheeltec_robot_node--790717f1d34c|agv:ros:node:wheeltec_robot_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/agv_mqtt_bridge--81622ebf066a|agv:ros:node:agv_mqtt_bridge]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/imu--4caf2e58d1e5|agv:ros:interface:imu]]
