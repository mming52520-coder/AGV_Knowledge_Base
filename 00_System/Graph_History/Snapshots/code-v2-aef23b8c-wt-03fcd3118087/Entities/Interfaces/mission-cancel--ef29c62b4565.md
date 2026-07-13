---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:mission-cancel"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:service:mission-cancel"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:mission-cancel"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/mission/cancel"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "127f7d9a173fe686bc86def675cce568b29ca7cda41fda3513f5420990f463ca"
relation_fingerprint: "4e9bfff1e66b70e0187e6651747d20bcadf130d5c0a0820bc538d6e7112fb3bc"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /mission/cancel

- 逻辑实体：`agv:ros:service:mission-cancel`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:mission-cancel`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_mission/src/mission_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | service |
| `message_type` | agv_interfaces/CancelMission |
| `ros_name` | /mission/cancel |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_mission/src/mission_node.cpp` | 29 | `provides_services` | `1ce6e64406c5c9c21829ee60cdc5c1394e054a1841944589f1cb52c644bb1927` |
| `src/agv_telemetry/src/telemetry_node.cpp` | 36 | `uses_services` | `54f7e54df3144dcd25b9fafd5e316ba1b17b5bb1eb92f9b79beae2ecfa7fb2b6` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mission--2b7d8642ed63|agv:ros:package:agv_mission]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_telemetry--948609af5cdf|agv:ros:package:agv_telemetry]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/mission_node--3f300b35dfe3|agv:ros:node:mission_node]] → `provides_services`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/telemetry_node--8a7add193f0d|agv:ros:node:telemetry_node]] → `uses_services`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/mission-cancel--ef29c62b4565|agv:ros:service:mission-cancel]]
