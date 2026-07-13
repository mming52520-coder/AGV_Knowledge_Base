---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:telemetry-cancel-request"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:telemetry-cancel-request"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:telemetry-cancel-request"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/telemetry/cancel_request"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "7668c3f91eeae44f7c6dd5594077e5853daaa5abd560a1dcddac516aadec0ffb"
relation_fingerprint: "93c1281ae96e23d9b26d26cbb11208fd46e23c61cc1881c8c7f60e091bdce651"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /telemetry/cancel_request

- 逻辑实体：`agv:ros:interface:telemetry-cancel-request`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:telemetry-cancel-request`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_telemetry/src/telemetry_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | unknown |
| `ros_name` | /telemetry/cancel_request |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_telemetry/src/telemetry_node.cpp` | 32 | `subscribes` | `54f7e54df3144dcd25b9fafd5e316ba1b17b5bb1eb92f9b79beae2ecfa7fb2b6` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_telemetry--948609af5cdf|agv:ros:package:agv_telemetry]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/telemetry_node--8a7add193f0d|agv:ros:node:telemetry_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/telemetry-cancel-request--c2b3e4a1e4a0|agv:ros:interface:telemetry-cancel-request]]
