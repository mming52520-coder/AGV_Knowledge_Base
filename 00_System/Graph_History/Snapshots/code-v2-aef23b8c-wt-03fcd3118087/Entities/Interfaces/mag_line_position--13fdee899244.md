---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mag-line-position"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:mag-line-position"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mag-line-position"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/mag_line_position"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "7a55aee9c8696b7d66c37bad71f200b082ed573ea3a1be6651bb5d4c81885a36"
relation_fingerprint: "83a4eb359e89dd3f5333fb43cdddaf3e493e633efefcc21336ebc61612e04c73"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /mag_line_position

- 逻辑实体：`agv:ros:interface:mag-line-position`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mag-line-position`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | std_msgs/Float32 |
| `ros_name` | /mag_line_position |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | [] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py` | 483 | `subscribes` | `e424ea32f29a7a5ba2b1e946cebd289ef2c0f4092b76dc1ebffc0db0b25116a2` |
| `src/magnetic_controlled_motor/src/magnetic_follower.cpp` | 58 | `publishes` | `d938df1cb95b9ed230679ae2dbf2b39ab2fd982dde3b6623cbdc6bcbafa89f3e` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mqtt_bridge--001d465b2aae|agv:ros:package:agv_mqtt_bridge]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/magnetic_controlled_motor--8bee0b922a0e|agv:ros:package:magnetic_controlled_motor]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/magnetic_follower--7aec69b0ba38|agv:ros:node:magnetic_follower]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/agv_mqtt_bridge--81622ebf066a|agv:ros:node:agv_mqtt_bridge]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/mag-line-position--13fdee899244|agv:ros:interface:mag-line-position]]
