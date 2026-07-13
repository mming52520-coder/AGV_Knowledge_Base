---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:motion_arbiter_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:motion_arbiter_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:motion_arbiter_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "motion_arbiter_node"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "53b0bf2e041f733f2bd1319d7d45d61d38909e012fe82867a6783e9044281f93"
relation_fingerprint: "a319677cf3f16d9b9f179cea717ab6a9f04889ec9d6d2012a0f3538096df9624"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# motion_arbiter_node

- 逻辑实体：`agv:ros:node:motion_arbiter_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:motion_arbiter_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_safety/src/motion_arbiter_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | motion_arbiter_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /motion_arbiter_node |
| `status` | active |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_safety/src/motion_arbiter_node.cpp` | 1 | `node_source` | `929268b1a6acc26bab31319976678a77281e24fa599e7a99cf787783b86a5c37` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_safety--2cb0a140ec4e|agv:ros:package:agv_safety]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/safety-candidate_command--f5c7d63afd32|agv:ros:interface:safety-candidate-command]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-left_wall_intent--8c1624b405c7|agv:ros:interface:decision-left-wall-intent]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-magnetic_intent--b3456506e926|agv:ros:interface:decision-magnetic-intent]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-teleop_intent--f636270024da|agv:ros:interface:decision-teleop-intent]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-tight_turn_intent--f3e83fac1cd0|agv:ros:interface:decision-tight-turn-intent]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-trajectory_intent--1a822f17b0b7|agv:ros:interface:decision-trajectory-intent]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/motion_arbiter_node--7dadfc6c36d0|agv:ros:node:motion_arbiter_node]]
