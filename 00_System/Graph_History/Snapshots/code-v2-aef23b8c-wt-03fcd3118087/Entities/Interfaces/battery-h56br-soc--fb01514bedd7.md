---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:battery-h56br-soc"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:battery-h56br-soc"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:battery-h56br-soc"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/battery/h56br/soc"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "5660ff1e9acec3afa554740443d63ca0ea7c587fe00569d991a7db5786c51215"
relation_fingerprint: "bb637cbc6cc50dd176f597f04fe1d4b0998c95a58524b05bfe8893f7876dea9d"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /battery/h56br/soc

- 逻辑实体：`agv:ros:interface:battery-h56br-soc`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:battery-h56br-soc`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | std_msgs/Float32 |
| `ros_name` | /battery/h56br/soc |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | [] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py` | 443 | `subscribes` | `e424ea32f29a7a5ba2b1e946cebd289ef2c0f4092b76dc1ebffc0db0b25116a2` |
| `src/agv_perception/src/perception_aggregator_node.cpp` | 58 | `subscribes` | `5b988700b3ea59236ab37c28ca7d0b4bd1dc66b69bf3328b71245d703f16d089` |
| `src/h56br_driver/src/h56br_node.cpp` | 60 | `publishes` | `06f7026c7a5db41028e34932d7965102ec7826445214637c7be0cf841c003b24` |
| `src/trajectory_recorder/src/trajectory_tracker.cpp` | 3745 | `subscribes` | `b13ba9a028ec7abd7b3956173e7cc20bc3a123038872ec4ea9c3a159ccf795c7` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mqtt_bridge--001d465b2aae|agv:ros:package:agv_mqtt_bridge]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_perception--b3844e0c0c3f|agv:ros:package:agv_perception]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/h56br_driver--8cf5e3bb73a1|agv:ros:package:h56br_driver]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/h56br_node--74030e2108af|agv:ros:node:h56br_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/agv_mqtt_bridge--81622ebf066a|agv:ros:node:agv_mqtt_bridge]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/perception_aggregator_node--38fa4d21e1c4|agv:ros:node:perception_aggregator_node]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_tracker--3031ab8e89fc|agv:ros:node:trajectory_tracker]] → `subscribes`

## 相对 V1 的变化

- `unchanged`：语义指纹与 V1 一致。
