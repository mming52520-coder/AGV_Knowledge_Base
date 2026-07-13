---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:mission-start"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:service:mission-start"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:mission-start"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/mission/start"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "796cac47417b7758ff196b76347afa0b2f4f2d5792f662d985fd4078af2a899d"
relation_fingerprint: "264ae7d8f1cd09f2880088b56f313473954cf15987bfc7ae59c112338ee9b39c"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /mission/start

- 逻辑实体：`agv:ros:service:mission-start`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:mission-start`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_mission/src/mission_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | service |
| `message_type` | agv_interfaces/StartMission |
| `ros_name` | /mission/start |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_mission/src/mission_node.cpp` | 26 | `provides_services` | `1ce6e64406c5c9c21829ee60cdc5c1394e054a1841944589f1cb52c644bb1927` |
| `src/agv_telemetry/src/telemetry_node.cpp` | 35 | `uses_services` | `54f7e54df3144dcd25b9fafd5e316ba1b17b5bb1eb92f9b79beae2ecfa7fb2b6` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mission--2b7d8642ed63|agv:ros:package:agv_mission]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_telemetry--948609af5cdf|agv:ros:package:agv_telemetry]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/mission_node--3f300b35dfe3|agv:ros:node:mission_node]] → `provides_services`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/telemetry_node--8a7add193f0d|agv:ros:node:telemetry_node]] → `uses_services`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/mission-start--d482eb3f7b4d|agv:ros:service:mission-start]]
