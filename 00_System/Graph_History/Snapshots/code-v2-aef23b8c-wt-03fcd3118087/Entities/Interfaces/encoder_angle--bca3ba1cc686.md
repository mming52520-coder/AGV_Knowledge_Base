---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:encoder-angle"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:encoder-angle"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:encoder-angle"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/encoder_angle"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "a8c5ff0b3b1d5a3be5eceebdbe76ab4dc8b5d798b42498c2eb3186dfef2b4068"
relation_fingerprint: "a1cddcbe00186644bc1f0573f99bc1de4bff357142163e8a328f812981af2c3c"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /encoder_angle

- 逻辑实体：`agv:ros:interface:encoder-angle`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:encoder-angle`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/encoder/src/rb100_encoder.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | std_msgs/Float32 |
| `ros_name` | /encoder_angle |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/encoder/src/rb100_encoder.cpp` | 412 | `publishes` | `7606db8a8175b2049da2c09f11abbf03ca27b57029c298c14fd25c0a42513000` |
| `src/trajectory_recorder/src/trajectory_recorder.cpp` | 908 | `publishes` | `c971b301b5907f52e00034491d77dcf5c8beb9cd04b67ef4ab2c5d5b97afa8c6` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/encoder--0240516ec77b|agv:ros:package:encoder]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/rb100_encoder--a141ed92ecec|agv:ros:node:rb100_encoder]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_recorder--4850a1d9f230|agv:ros:node:trajectory_recorder]] → `publishes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/encoder-angle--bca3ba1cc686|agv:ros:interface:encoder-angle]]
