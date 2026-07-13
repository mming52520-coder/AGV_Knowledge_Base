---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:tight_turn_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:tight_turn_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:tight_turn_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "tight_turn_node"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "8ae5326ef71d69c9b44099508f9728ed7208ff8124437c96468bd28cb8ffa471"
relation_fingerprint: "354eba3b048f4ad95320dcd9808bb72f42205cde8e06c1ed56a905728595aabd"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# tight_turn_node

- 逻辑实体：`agv:ros:node:tight_turn_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:tight_turn_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_decision/src/tight_turn_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | tight_turn_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /decision/tight_turn_node |
| `status` | active |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_decision/src/tight_turn_node.cpp` | 1 | `node_source` | `91e65662a315958e30e5896c0fb267ae5a005eb59c77198075854eb97152189c` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/decision-tight_turn_intent--f3e83fac1cd0|agv:ros:interface:decision-tight-turn-intent]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-state--1bf376c688d5|agv:ros:interface:mission-state]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/perception-state--9e4cc739ed14|agv:ros:interface:perception-state]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/tight_turn_node--fafce7d62191|agv:ros:node:tight_turn_node]]
