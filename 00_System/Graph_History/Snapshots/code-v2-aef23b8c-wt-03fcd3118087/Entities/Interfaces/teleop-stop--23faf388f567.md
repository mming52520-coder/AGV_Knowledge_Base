---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:teleop-stop"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:teleop-stop"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:teleop-stop"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/teleop/stop"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "3e8b4906f172cf1a8c21b97473c521e983af863512bf9070ce75e620e174e9aa"
relation_fingerprint: "2b377259dbe586fa0e93c94a754e0b548a749c866ffd120e9c0c6600109446dd"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /teleop/stop

- 逻辑实体：`agv:ros:interface:teleop-stop`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:teleop-stop`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_decision/src/teleop_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | unknown |
| `ros_name` | /teleop/stop |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_decision/src/teleop_node.cpp` | 19 | `subscribes` | `65c9f0dd0ffe21416bf2c999e3e75fd727066c7dc27a3cf1e00d483a766c038f` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/teleop_node--46ce150fbd13|agv:ros:node:teleop_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/teleop-stop--23faf388f567|agv:ros:interface:teleop-stop]]
