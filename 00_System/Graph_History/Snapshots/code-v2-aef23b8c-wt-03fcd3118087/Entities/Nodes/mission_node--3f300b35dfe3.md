---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:mission_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:mission_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:mission_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "mission_node"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "7d123ff40c404a3ae3649102350a99f623d2243699cbd8b989685c9739fde042"
relation_fingerprint: "46260f2654a26c4704fdd1854c5c3cb4de7642fffbe5840e8708d825a055126f"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# mission_node

- 逻辑实体：`agv:ros:node:mission_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:mission_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_mission/src/mission_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | mission_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /mission_node |
| `status` | active |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_mission/src/mission_node.cpp` | 1 | `node_source` | `1ce6e64406c5c9c21829ee60cdc5c1394e054a1841944589f1cb52c644bb1927` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mission--2b7d8642ed63|agv:ros:package:agv_mission]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-cancel--ef29c62b4565|agv:ros:service:mission-cancel]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-pause--ced3313a25c7|agv:ros:service:mission-pause]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-resume--63c8ad51735d|agv:ros:service:mission-resume]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-start--d482eb3f7b4d|agv:ros:service:mission-start]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-state--1bf376c688d5|agv:ros:interface:mission-state]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-trajectory_file--3e1456a7d19b|agv:ros:interface:mission-trajectory-file]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/mission_node--3f300b35dfe3|agv:ros:node:mission_node]]
