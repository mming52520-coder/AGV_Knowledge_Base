---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mission-trajectory-file"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:mission-trajectory-file"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mission-trajectory-file"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/mission/trajectory_file"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "6213b08107a13b0d379791cfbe9078b928ee1a74544c87900a58b9134682c773"
relation_fingerprint: "8ceaf0b494f2188565439e38bd84b53831d8c66e40eb0e36ac6b0a1e39f8d233"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /mission/trajectory_file

- 逻辑实体：`agv:ros:interface:mission-trajectory-file`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mission-trajectory-file`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_mission/src/mission_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | std_msgs/String |
| `ros_name` | /mission/trajectory_file |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_decision/src/trajectory_follower_node.cpp` | 29 | `subscribes` | `911174c1a90ddde2bf29311d6d29b86f2dd47591c4f01c2b82c387523874a3c3` |
| `src/agv_mission/src/mission_node.cpp` | 24 | `publishes` | `1ce6e64406c5c9c21829ee60cdc5c1394e054a1841944589f1cb52c644bb1927` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mission--2b7d8642ed63|agv:ros:package:agv_mission]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/mission_node--3f300b35dfe3|agv:ros:node:mission_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_follower_node--983183f9b80a|agv:ros:node:trajectory_follower_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/mission-trajectory-file--3e1456a7d19b|agv:ros:interface:mission-trajectory-file]]
