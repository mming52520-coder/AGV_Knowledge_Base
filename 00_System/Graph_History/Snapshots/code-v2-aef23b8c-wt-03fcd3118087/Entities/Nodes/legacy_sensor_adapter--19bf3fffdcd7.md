---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:legacy_sensor_adapter"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:legacy_sensor_adapter"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:legacy_sensor_adapter"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "legacy_sensor_adapter"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "13bb376c94a2b6db0c74aa3a7e9fa24ac7128eacc4dc165aa1236bfd9f2a79d4"
relation_fingerprint: "20cc7061b4d2b5c67c469d0a0a7b9c07db4b4607d3d4588d9971c6fc0abc2a70"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# legacy_sensor_adapter

- 逻辑实体：`agv:ros:node:legacy_sensor_adapter`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:legacy_sensor_adapter`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_legacy/src/legacy_sensor_adapter.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | legacy_sensor_adapter |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /legacy_sensor_adapter |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_legacy/src/legacy_sensor_adapter.cpp` | 1 | `node_source` | `5f79e6f350f2296d63e20a6a315495ca50c9df9afabaac13718eb41917c24c3f` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_legacy--db70b74c409e|agv:ros:package:agv_legacy]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/legacy-odom--115195c0f833|agv:ros:interface:legacy-odom]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/vehicle-state--f1837ba03534|agv:ros:interface:vehicle-state]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/legacy_sensor_adapter--19bf3fffdcd7|agv:ros:node:legacy_sensor_adapter]]
