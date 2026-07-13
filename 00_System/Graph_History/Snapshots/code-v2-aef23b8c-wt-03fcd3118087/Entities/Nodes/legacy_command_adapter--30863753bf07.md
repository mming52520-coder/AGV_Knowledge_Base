---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:legacy_command_adapter"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:legacy_command_adapter"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:legacy_command_adapter"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "legacy_command_adapter"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "dfceb72cec21d8d97dfb80bf108ef0af560e2619023968815d436b56e5919797"
relation_fingerprint: "8ae27db017739ccfd1c942101d6accd4647fb12f5d09c8283af8254e73cf5118"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# legacy_command_adapter

- 逻辑实体：`agv:ros:node:legacy_command_adapter`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:legacy_command_adapter`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_legacy/src/legacy_command_adapter.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | legacy_command_adapter |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /legacy_command_adapter |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_legacy/src/legacy_command_adapter.cpp` | 1 | `node_source` | `fa4aef04bb56c36e83a3ca8f01ef53b7482c8583a11473a4a6a74259e2fa3901` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_legacy--db70b74c409e|agv:ros:package:agv_legacy]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/safety-final_command--366706b48c35|agv:ros:interface:safety-final-command]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/legacy_command_adapter--30863753bf07|agv:ros:node:legacy_command_adapter]]
