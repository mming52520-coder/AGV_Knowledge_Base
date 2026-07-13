---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:perception-health"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:perception-health"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:perception-health"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/perception/health"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "cb81015fdb9775aee1e162d9fd44249c8a1735c3e3eb895973d0610da511fa07"
relation_fingerprint: "3844ae968d66d20981c5ebdb73b374436ba3e591e990f2a3cf9602e1da492a06"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /perception/health

- 逻辑实体：`agv:ros:interface:perception-health`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:perception-health`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_perception/src/perception_aggregator_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | diagnostic_msgs/DiagnosticArray |
| `ros_name` | /perception/health |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_perception/src/perception_aggregator_node.cpp` | 62 | `publishes` | `5b988700b3ea59236ab37c28ca7d0b4bd1dc66b69bf3328b71245d703f16d089` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_perception--b3844e0c0c3f|agv:ros:package:agv_perception]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/perception_aggregator_node--38fa4d21e1c4|agv:ros:node:perception_aggregator_node]] → `publishes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/perception-health--8c7afd3dc0e7|agv:ros:interface:perception-health]]
