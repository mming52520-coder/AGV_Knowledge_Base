---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:chassis-state"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:chassis-state"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:chassis-state"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/chassis/state"
status: "available"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "1fa02246e732ef73fa4ccd7b142ae66fe0c4b132e639b2770da77bba9dccfc82"
relation_fingerprint: "5ae1a06d051e0395fb2b7276301f9a0be707f37ce50e1c9d83f30f2360a44234"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /chassis/state

- 逻辑实体：`agv:ros:interface:chassis-state`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:chassis-state`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/chassis_controller/src/chassis_bridge.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | ChassisState |
| `ros_name` | /chassis/state |
| `status` | available |
| `type` | ros_interface |
| `vehicles` | [] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/chassis_controller/src/chassis_bridge.cpp` | 534 | `publishes` | `3a0cb99a9e0a47cb51c96f6034ea566cac7c9cca3146fbc295076de2ed9622f2` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/chassis_controller--57f0aa46929c|agv:ros:package:chassis_controller]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/chassis_bridge--f2b72fa46041|agv:ros:node:chassis_bridge]] → `publishes`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`message_type`, `status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/chassis-state--1aa49c890804|agv:ros:interface:chassis-state]]
