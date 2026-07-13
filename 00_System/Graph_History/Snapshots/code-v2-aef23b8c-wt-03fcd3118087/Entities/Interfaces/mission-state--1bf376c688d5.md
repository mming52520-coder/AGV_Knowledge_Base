---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mission-state"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:mission-state"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mission-state"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/mission/state"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "40c020473d2ad38479635e452741ba935ac2306b31037dca94f962fda0758397"
relation_fingerprint: "c2858afed9b105145bd781b035666f08af54b19884f025081091e9a47b95395a"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /mission/state

- 逻辑实体：`agv:ros:interface:mission-state`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:mission-state`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_mission/src/mission_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | agv_interfaces/MissionState |
| `ros_name` | /mission/state |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_decision/src/tight_turn_node.cpp` | 20 | `subscribes` | `91e65662a315958e30e5896c0fb267ae5a005eb59c77198075854eb97152189c` |
| `src/agv_decision/src/trajectory_follower_node.cpp` | 28 | `subscribes` | `911174c1a90ddde2bf29311d6d29b86f2dd47591c4f01c2b82c387523874a3c3` |
| `src/agv_mission/src/mission_node.cpp` | 23 | `publishes` | `1ce6e64406c5c9c21829ee60cdc5c1394e054a1841944589f1cb52c644bb1927` |
| `src/agv_telemetry/src/telemetry_node.cpp` | 25 | `subscribes` | `54f7e54df3144dcd25b9fafd5e316ba1b17b5bb1eb92f9b79beae2ecfa7fb2b6` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mission--2b7d8642ed63|agv:ros:package:agv_mission]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_telemetry--948609af5cdf|agv:ros:package:agv_telemetry]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/mission_node--3f300b35dfe3|agv:ros:node:mission_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/telemetry_node--8a7add193f0d|agv:ros:node:telemetry_node]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/tight_turn_node--fafce7d62191|agv:ros:node:tight_turn_node]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_follower_node--983183f9b80a|agv:ros:node:trajectory_follower_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/mission-state--1bf376c688d5|agv:ros:interface:mission-state]]
