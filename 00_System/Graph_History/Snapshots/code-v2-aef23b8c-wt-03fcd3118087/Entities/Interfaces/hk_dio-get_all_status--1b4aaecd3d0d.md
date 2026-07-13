---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:hk-dio-get-all-status"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:service:hk-dio-get-all-status"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:hk-dio-get-all-status"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/hk_dio/get_all_status"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "54c8917e4f3b7372b7a4794e448a8fb733a22fe2dda4cc7d259e7f1a65f2a23d"
relation_fingerprint: "baeca367a8be5a0b6d5c48b8ca006cca5575a5a82ad749ba701885a513a20b5e"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /hk_dio/get_all_status

- 逻辑实体：`agv:ros:service:hk-dio-get-all-status`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:hk-dio-get-all-status`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/relay/src/hk_dio.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | service |
| `message_type` | unknown |
| `ros_name` | /hk_dio/get_all_status |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/relay/src/hk_dio.cpp` | 740 | `provides_services` | `f58219ece14ea3da46899038faa2a19b2fe31aa128b7fe1de30f42a6af4ab70f` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/relay--7e8f04764da5|agv:ros:package:relay]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/hk_dio--0a63059567a9|agv:ros:node:hk_dio_controller]] → `provides_services`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/hk-dio-get-all-status--1b4aaecd3d0d|agv:ros:service:hk-dio-get-all-status]]
