---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:legacy-odom"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:legacy-odom"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:legacy-odom"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/legacy/odom"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "e6aa44f933992202f0287c5519bd655844f03282331e826d8874cbc6f993d9ce"
relation_fingerprint: "7a32a77cfde02839761ecbc8b3df5131afb63f8211b7c9299995b16344bc8c03"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /legacy/odom

- 逻辑实体：`agv:ros:interface:legacy-odom`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:legacy-odom`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_legacy/src/legacy_sensor_adapter.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | nav_msgs/Odometry |
| `ros_name` | /legacy/odom |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_legacy/src/legacy_sensor_adapter.cpp` | 19 | `publishes` | `5f79e6f350f2296d63e20a6a315495ca50c9df9afabaac13718eb41917c24c3f` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_legacy--db70b74c409e|agv:ros:package:agv_legacy]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/legacy_sensor_adapter--19bf3fffdcd7|agv:ros:node:legacy_sensor_adapter]] → `publishes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/legacy-odom--115195c0f833|agv:ros:interface:legacy-odom]]
