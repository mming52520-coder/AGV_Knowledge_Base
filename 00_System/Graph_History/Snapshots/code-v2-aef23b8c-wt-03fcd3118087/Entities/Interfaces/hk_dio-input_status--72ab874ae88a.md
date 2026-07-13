---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:hk-dio-input-status"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:hk-dio-input-status"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:hk-dio-input-status"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/hk_dio/input_status"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "b3dc7b8c25c6bdc2e9e0572d743678dc3c7d54b4fa713ae72d99fb077fde7757"
relation_fingerprint: "9349d4764587e9398361b463714af2e1a887c23e2b9fa520a5db4bf1e8438487"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /hk_dio/input_status

- 逻辑实体：`agv:ros:interface:hk-dio-input-status`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:hk-dio-input-status`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/relay/src/hk_dio.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | std_msgs/UInt8MultiArray |
| `ros_name` | /hk_dio/input_status |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/relay/src/hk_dio.cpp` | 715 | `publishes` | `f58219ece14ea3da46899038faa2a19b2fe31aa128b7fe1de30f42a6af4ab70f` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/relay--7e8f04764da5|agv:ros:package:relay]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/hk_dio--0a63059567a9|agv:ros:node:hk_dio_controller]] → `publishes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/hk-dio-input-status--72ab874ae88a|agv:ros:interface:hk-dio-input-status]]
