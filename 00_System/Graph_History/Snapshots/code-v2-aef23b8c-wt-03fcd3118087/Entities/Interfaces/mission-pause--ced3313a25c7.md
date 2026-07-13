---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:mission-pause"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:service:mission-pause"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:mission-pause"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/mission/pause"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "99e5a555214c9de26c2a6ee3fe3167b390f1a45f02a3936970a0749aa3d2bf43"
relation_fingerprint: "4164f1e72e22d8956a4a59a6aa2c58cc3e95737b18f76c07521190941658468b"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /mission/pause

- 逻辑实体：`agv:ros:service:mission-pause`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:mission-pause`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_mission/src/mission_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | service |
| `message_type` | unknown |
| `ros_name` | /mission/pause |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_mission/src/mission_node.cpp` | 27 | `provides_services` | `1ce6e64406c5c9c21829ee60cdc5c1394e054a1841944589f1cb52c644bb1927` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mission--2b7d8642ed63|agv:ros:package:agv_mission]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/mission_node--3f300b35dfe3|agv:ros:node:mission_node]] → `provides_services`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/mission-pause--ced3313a25c7|agv:ros:service:mission-pause]]
