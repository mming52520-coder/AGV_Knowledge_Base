---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:decision-left-wall-intent"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:decision-left-wall-intent"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:decision-left-wall-intent"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/decision/left_wall_intent"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "c6307d4d5b251e26c4240c6cb8dd13a84e0555b1ab44b83685f94d08fd007c6b"
relation_fingerprint: "2a791cbd1d6c90258ce1bcbe8c91a947b09838f8f9f81e6ef4dc444e63dda8e8"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /decision/left_wall_intent

- 逻辑实体：`agv:ros:interface:decision-left-wall-intent`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:decision-left-wall-intent`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_decision/src/left_wall_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | agv_interfaces/MotionIntent |
| `ros_name` | /decision/left_wall_intent |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_decision/src/left_wall_node.cpp` | 18 | `publishes` | `c20f48e877a36e5a382864cd88b6b387483b57b78515b5381aa592200cb73735` |
| `src/agv_safety/src/motion_arbiter_node.cpp` | 18 | `subscribes` | `929268b1a6acc26bab31319976678a77281e24fa599e7a99cf787783b86a5c37` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_safety--2cb0a140ec4e|agv:ros:package:agv_safety]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/left_wall_node--fdb9bf57d711|agv:ros:node:left_wall_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/motion_arbiter_node--7dadfc6c36d0|agv:ros:node:motion_arbiter_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/decision-left-wall-intent--8c1624b405c7|agv:ros:interface:decision-left-wall-intent]]
