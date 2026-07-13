---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:teleop-cmd"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:teleop-cmd"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:teleop-cmd"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/teleop/cmd"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "beeddd69e25fe1d9fc205d33594485619dd6ef7441442bd7926e388d3e300b95"
relation_fingerprint: "c5af5518f0bebb830ab33e68a8ab5ac79f7d4091f947b69e2b509ff5e9ff2597"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /teleop/cmd

- 逻辑实体：`agv:ros:interface:teleop-cmd`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:teleop-cmd`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_decision/src/teleop_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | unknown |
| `ros_name` | /teleop/cmd |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_decision/src/teleop_node.cpp` | 18 | `subscribes` | `65c9f0dd0ffe21416bf2c999e3e75fd727066c7dc27a3cf1e00d483a766c038f` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/teleop_node--46ce150fbd13|agv:ros:node:teleop_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/teleop-cmd--cbd3a6af2f03|agv:ros:interface:teleop-cmd]]
