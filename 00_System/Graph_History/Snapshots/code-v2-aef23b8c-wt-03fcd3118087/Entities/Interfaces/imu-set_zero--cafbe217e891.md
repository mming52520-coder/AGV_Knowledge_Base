---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:imu-set-zero"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:service:imu-set-zero"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:imu-set-zero"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/imu/set_zero"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "12e990109d0517b07c9b90ee90e42d85a907b6f4511775d4c918ab55306d5bf1"
relation_fingerprint: "b13caa1e5f7d2d9454be53c8c7c0a7e0b1617b9b3f3f839b487d7a61899e3fc9"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /imu/set_zero

- 逻辑实体：`agv:ros:service:imu-set-zero`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:imu-set-zero`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/trajectory_recorder/src/trajectory_recorder.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | service |
| `message_type` | unknown |
| `ros_name` | /imu/set_zero |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/trajectory_recorder/src/trajectory_recorder.cpp` | 917 | `provides_services` | `c971b301b5907f52e00034491d77dcf5c8beb9cd04b67ef4ab2c5d5b97afa8c6` |
| `src/trajectory_recorder/src/trajectory_tracker.cpp` | 3881 | `provides_services` | `b13ba9a028ec7abd7b3956173e7cc20bc3a123038872ec4ea9c3a159ccf795c7` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_recorder--4850a1d9f230|agv:ros:node:trajectory_recorder]] → `provides_services`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_tracker--3031ab8e89fc|agv:ros:node:trajectory_tracker]] → `provides_services`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/imu-set-zero--cafbe217e891|agv:ros:service:imu-set-zero]]
