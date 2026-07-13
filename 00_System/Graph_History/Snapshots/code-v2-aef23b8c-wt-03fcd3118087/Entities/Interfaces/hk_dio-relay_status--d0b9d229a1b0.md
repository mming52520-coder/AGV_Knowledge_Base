---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:hk-dio-relay-status"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:hk-dio-relay-status"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:hk-dio-relay-status"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/hk_dio/relay_status"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "e487676a51a1f65739594bc6c9c29482a1b397c57ef09745f63454006923038b"
relation_fingerprint: "23d497f92c4edaf01c0baa6c962239db2c0cbf6af8bc5ff2aad6ad00eceb51f4"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /hk_dio/relay_status

- 逻辑实体：`agv:ros:interface:hk-dio-relay-status`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:hk-dio-relay-status`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/relay/src/hk_dio.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | std_msgs/UInt8MultiArray |
| `ros_name` | /hk_dio/relay_status |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/relay/src/hk_dio.cpp` | 714 | `publishes` | `f58219ece14ea3da46899038faa2a19b2fe31aa128b7fe1de30f42a6af4ab70f` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/relay--7e8f04764da5|agv:ros:package:relay]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/hk_dio--0a63059567a9|agv:ros:node:hk_dio_controller]] → `publishes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/hk-dio-relay-status--d0b9d229a1b0|agv:ros:interface:hk-dio-relay-status]]
