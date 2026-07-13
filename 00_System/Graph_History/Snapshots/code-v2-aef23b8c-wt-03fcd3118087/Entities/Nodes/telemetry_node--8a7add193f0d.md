---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:telemetry_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:telemetry_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:telemetry_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "telemetry_node"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "cacf4c039ede65eb1d03efa0cd0e48ac7f3713d2de37e8047410173f6bfdeae0"
relation_fingerprint: "ad845c2e194914c35ad72706c4e68e7bd8769a79bc105ed892ca2bbec5d26f20"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# telemetry_node

- 逻辑实体：`agv:ros:node:telemetry_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:telemetry_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_telemetry/src/telemetry_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | telemetry_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /telemetry_node |
| `status` | active |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_telemetry/src/telemetry_node.cpp` | 1 | `node_source` | `54f7e54df3144dcd25b9fafd5e316ba1b17b5bb1eb92f9b79beae2ecfa7fb2b6` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_telemetry--948609af5cdf|agv:ros:package:agv_telemetry]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/telemetry-status--079590b53a21|agv:ros:interface:telemetry-status]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/execution-state--ec53c020b6c5|agv:ros:interface:execution-state]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-state--1bf376c688d5|agv:ros:interface:mission-state]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/safety-state--b5957c7c06d9|agv:ros:interface:safety-state]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/telemetry-cancel_request--c2b3e4a1e4a0|agv:ros:interface:telemetry-cancel-request]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/telemetry-start_request--73157ff8f7a5|agv:ros:interface:telemetry-start-request]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/vehicle-state--f1837ba03534|agv:ros:interface:vehicle-state]]
- `uses_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-cancel--ef29c62b4565|agv:ros:service:mission-cancel]]
- `uses_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-start--d482eb3f7b4d|agv:ros:service:mission-start]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/telemetry_node--8a7add193f0d|agv:ros:node:telemetry_node]]
