---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:dyp_ultrasonic_legacy_adapter"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:dyp_ultrasonic_legacy_adapter"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:dyp_ultrasonic_legacy_adapter"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "dyp_ultrasonic_legacy_adapter"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "f7763fc348f8f96c00c671cdfecbf555dcc751ea1b0e6beb0ebfb1d92d72078b"
relation_fingerprint: "8d5d3aa5373f80483351235df47a23cc82311d6a5bac0dc894477fb5602c82c0"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# dyp_ultrasonic_legacy_adapter

- 逻辑实体：`agv:ros:node:dyp_ultrasonic_legacy_adapter`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:dyp_ultrasonic_legacy_adapter`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/ultrasonic_controlled_motor/src/dyp_ultrasonic_legacy_adapter.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | dyp_ultrasonic_legacy_adapter |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /dyp_ultrasonic_legacy_adapter |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/ultrasonic_controlled_motor/src/dyp_ultrasonic_legacy_adapter.cpp` | 1 | `node_source` | `a507058ba8b4df070ab58507bee19f02ea54df4a1a19d43ba398bac04d3286b7` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/ultrasonic_controlled_motor--2e98007ce616|agv:ros:package:ultrasonic_controlled_motor]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-front_distance--f2df0d6f13fc|agv:ros:interface:ultrasonic-front-distance]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-front_status--9cf5e5dd81ab|agv:ros:interface:ultrasonic-front-status]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_distance--1240d1cca41f|agv:ros:interface:ultrasonic-left-distance]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_status--076d80f3e514|agv:ros:interface:ultrasonic-left-status]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-rear_distance--875cdec8b4fb|agv:ros:interface:ultrasonic-rear-distance]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-rear_status--4db4f184e714|agv:ros:interface:ultrasonic-rear-status]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-right_distance--ce2626276c17|agv:ros:interface:ultrasonic-right-distance]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-right_status--1b88b10d7f8c|agv:ros:interface:ultrasonic-right-status]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-distances--95d581d0b6c4|agv:ros:interface:ultrasonic-distances]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/dyp_ultrasonic_legacy_adapter--b2f54bdcab46|agv:ros:node:dyp_ultrasonic_legacy_adapter]]
