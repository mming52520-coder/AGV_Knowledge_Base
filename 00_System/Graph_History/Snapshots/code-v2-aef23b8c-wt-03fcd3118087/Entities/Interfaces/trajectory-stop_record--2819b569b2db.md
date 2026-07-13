---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:trajectory-stop-record"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:service:trajectory-stop-record"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:trajectory-stop-record"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/trajectory/stop_record"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "03acf9e105ad330c7fbb136863ff869d8726c3cee4d3f8b549243516adb73825"
relation_fingerprint: "483e10cc8dce00098d7077c4171736886cface82c4b1fe3a02a5b9fdfeecf013"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /trajectory/stop_record

- 逻辑实体：`agv:ros:service:trajectory-stop-record`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:trajectory-stop-record`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/trajectory_recorder/src/trajectory_recorder.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | service |
| `message_type` | unknown |
| `ros_name` | /trajectory/stop_record |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/trajectory_recorder/src/trajectory_recorder.cpp` | 911 | `provides_services` | `c971b301b5907f52e00034491d77dcf5c8beb9cd04b67ef4ab2c5d5b97afa8c6` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_recorder--4850a1d9f230|agv:ros:node:trajectory_recorder]] → `provides_services`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/trajectory-stop-record--2819b569b2db|agv:ros:service:trajectory-stop-record]]
