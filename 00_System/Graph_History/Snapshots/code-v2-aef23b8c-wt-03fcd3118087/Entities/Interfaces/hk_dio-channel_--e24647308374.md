---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:hk-dio-channel"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:hk-dio-channel"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:hk-dio-channel"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/hk_dio/channel_"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "9af1fa779747945924a4d696448cd54e36a504bbccd1d24f947b55fbcbf13be8"
relation_fingerprint: "e5540036a5182897f4f395555965772600b5e7e89402d02df058dd2b9552c208"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /hk_dio/channel_

- 逻辑实体：`agv:ros:interface:hk-dio-channel`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:hk-dio-channel`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/relay/src/hk_dio.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | std_msgs/Bool |
| `ros_name` | /hk_dio/channel_ |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/relay/src/hk_dio.cpp` | 723 | `subscribes` | `f58219ece14ea3da46899038faa2a19b2fe31aa128b7fe1de30f42a6af4ab70f` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/relay--7e8f04764da5|agv:ros:package:relay]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/hk_dio--0a63059567a9|agv:ros:node:hk_dio_controller]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/hk-dio-channel--e24647308374|agv:ros:interface:hk-dio-channel]]
