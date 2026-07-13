---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:safety-reset-fault"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:service:safety-reset-fault"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:safety-reset-fault"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/safety/reset_fault"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "7e9c4c9fafcaf660fc50ac6b27f60d32902112db16eae31df65e49df5eb4aac3"
relation_fingerprint: "8e2fa0bd02c887dd14149c06a79e880dfd9cac9e1f9e6182b3fc2504f7a60c13"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /safety/reset_fault

- 逻辑实体：`agv:ros:service:safety-reset-fault`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:safety-reset-fault`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_safety/src/safety_supervisor_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | service |
| `message_type` | unknown |
| `ros_name` | /safety/reset_fault |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_safety/src/safety_supervisor_node.cpp` | 31 | `provides_services` | `6fc04009a55824b6cbbf37ed22b770e68164645af33b7f4b84a8fd6908c74b8a` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_safety--2cb0a140ec4e|agv:ros:package:agv_safety]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/safety_supervisor_node--c235eb005bf0|agv:ros:node:safety_supervisor_node]] → `provides_services`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/safety-reset-fault--61450899e522|agv:ros:service:safety-reset-fault]]
