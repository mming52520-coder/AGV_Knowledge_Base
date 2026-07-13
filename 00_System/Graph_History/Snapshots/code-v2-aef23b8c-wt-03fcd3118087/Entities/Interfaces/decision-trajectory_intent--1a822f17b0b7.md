---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:decision-trajectory-intent"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:decision-trajectory-intent"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:decision-trajectory-intent"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/decision/trajectory_intent"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "eda9418d99cdafb7e58a9dd84ed1f1d00a3fcc86f1593b8c680692ccd6cdede9"
relation_fingerprint: "9ff7ff3756355f1036cd638828cc8d4b2975805f10195e1bf236b06324de60d4"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /decision/trajectory_intent

- 逻辑实体：`agv:ros:interface:decision-trajectory-intent`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:decision-trajectory-intent`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_safety/src/motion_arbiter_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | agv_interfaces/MotionIntent |
| `ros_name` | /decision/trajectory_intent |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_decision/src/trajectory_follower_node.cpp` | 31 | `publishes` | `911174c1a90ddde2bf29311d6d29b86f2dd47591c4f01c2b82c387523874a3c3` |
| `src/agv_safety/src/motion_arbiter_node.cpp` | 16 | `subscribes` | `929268b1a6acc26bab31319976678a77281e24fa599e7a99cf787783b86a5c37` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_safety--2cb0a140ec4e|agv:ros:package:agv_safety]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_follower_node--983183f9b80a|agv:ros:node:trajectory_follower_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/motion_arbiter_node--7dadfc6c36d0|agv:ros:node:motion_arbiter_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/decision-trajectory-intent--1a822f17b0b7|agv:ros:interface:decision-trajectory-intent]]
