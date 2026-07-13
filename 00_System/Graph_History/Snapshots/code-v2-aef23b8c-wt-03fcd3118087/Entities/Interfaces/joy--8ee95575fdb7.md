---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:joy"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:joy"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:joy"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/joy"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "4b68aa45cd7100a10664f31041d52fcbee822d80e34fb57345a3928dc3449bf3"
relation_fingerprint: "0c5233ffe8650a7449efa3988ee15521e9258fdcc03e2ce7b9a94b1a21dd8a2b"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /joy

- 逻辑实体：`agv:ros:interface:joy`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:joy`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/remote_ctrl/src/remote_controller.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | unknown |
| `ros_name` | /joy |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/remote_ctrl/src/remote_controller.cpp` | 75 | `subscribes` | `6487d9d6f0dbdbb257a4a21816c73c5f056dd26a987b8d1eba132452d1c9b98d` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/remote_ctrl--081aafab18b5|agv:ros:package:remote_ctrl]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/remote_controller--64f1746fd3dc|agv:ros:node:remote_controller]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/joy--8ee95575fdb7|agv:ros:interface:joy]]
