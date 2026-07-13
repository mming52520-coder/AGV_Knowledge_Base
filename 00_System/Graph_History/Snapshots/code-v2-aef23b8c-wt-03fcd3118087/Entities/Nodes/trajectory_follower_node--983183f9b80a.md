---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:trajectory_follower_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:trajectory_follower_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:trajectory_follower_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "trajectory_follower_node"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "62e07e1d9fc42281f57d72e8414938a91168bdf8b285a48aee99567163b431d5"
relation_fingerprint: "ef21a8db7aadcfb91c55cb5aaa645b1d449e985bee4ecd347bf7bc513a6b5faf"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# trajectory_follower_node

- 逻辑实体：`agv:ros:node:trajectory_follower_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:trajectory_follower_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_decision/src/trajectory_follower_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | trajectory_follower_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /decision/trajectory_follower_node |
| `status` | active |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_decision/src/trajectory_follower_node.cpp` | 1 | `node_source` | `911174c1a90ddde2bf29311d6d29b86f2dd47591c4f01c2b82c387523874a3c3` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-trajectory_intent--1a822f17b0b7|agv:ros:interface:decision-trajectory-intent]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-state--1bf376c688d5|agv:ros:interface:mission-state]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-trajectory_file--3e1456a7d19b|agv:ros:interface:mission-trajectory-file]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/perception-state--9e4cc739ed14|agv:ros:interface:perception-state]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/vehicle-state--f1837ba03534|agv:ros:interface:vehicle-state]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/trajectory_follower_node--983183f9b80a|agv:ros:node:trajectory_follower_node]]
