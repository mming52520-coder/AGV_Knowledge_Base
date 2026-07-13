---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:vehicle_state_estimator_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:vehicle_state_estimator_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:vehicle_state_estimator_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "vehicle_state_estimator_node"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "0c9671fef86c649a48a0a23d4faa5ed14f84535ce5f4d0ef5481e39f27352038"
relation_fingerprint: "d90ee1e40a7b988b0e8517dd87ed51ad83fb07cebaba0cf76f9abc8c7f36937b"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# vehicle_state_estimator_node

- 逻辑实体：`agv:ros:node:vehicle_state_estimator_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:vehicle_state_estimator_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_state_estimation/src/vehicle_state_estimator_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | vehicle_state_estimator_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /vehicle_state_estimator_node |
| `status` | active |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_state_estimation/src/vehicle_state_estimator_node.cpp` | 1 | `node_source` | `a2fcf806695f2d7e23fbdc9ac6f12ae8255ee662dbd3e24eeeac9f43c983825f` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_state_estimation--99b849143b75|agv:ros:package:agv_state_estimation]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/odom--1e74762c157b|agv:ros:interface:odom]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/vehicle-state--f1837ba03534|agv:ros:interface:vehicle-state]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/execution-state--ec53c020b6c5|agv:ros:interface:execution-state]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/perception-state--9e4cc739ed14|agv:ros:interface:perception-state]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/vehicle_state_estimator_node--f5bf32466a46|agv:ros:node:vehicle_state_estimator_node]]
