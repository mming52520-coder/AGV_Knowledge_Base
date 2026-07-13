---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:chassis_bridge"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:chassis_bridge"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:chassis_bridge"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "chassis_bridge"
status: "available"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "16370a38858040bc2aa2c20a3723201ef0a98bcb15e320bae7d9fae63ac545eb"
relation_fingerprint: "58bc444d36c4e8677d4b4d962012ec48ab594375e1d28a56556cdc127ba6e054"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# chassis_bridge

- 逻辑实体：`agv:ros:node:chassis_bridge`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:chassis_bridge`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/chassis_controller/src/chassis_bridge.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | chassis_bridge |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /chassis_bridge |
| `status` | available |
| `type` | ros_node |
| `vehicles` | ["二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/chassis_controller/src/chassis_bridge.cpp` | 1 | `node_source` | `3a0cb99a9e0a47cb51c96f6034ea566cac7c9cca3146fbc295076de2ed9622f2` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/chassis_controller--57f0aa46929c|agv:ros:package:chassis_controller]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/chassis-state--1aa49c890804|agv:ros:interface:chassis-state]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/chassis-cmd--f60fe5d4d5a2|agv:ros:interface:chassis-cmd]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/chassis_bridge--f2b72fa46041|agv:ros:node:chassis_bridge]]
