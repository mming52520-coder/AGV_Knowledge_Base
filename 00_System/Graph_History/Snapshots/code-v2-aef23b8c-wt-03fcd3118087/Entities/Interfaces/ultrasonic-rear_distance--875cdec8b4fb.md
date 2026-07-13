---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:ultrasonic-rear-distance"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:ultrasonic-rear-distance"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:ultrasonic-rear-distance"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/ultrasonic/rear_distance"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "dbef391656ce8210d61add5d5ec3700a9fbb0292cbccde3d31634980043e6f3a"
relation_fingerprint: "88941c1749fe06a8397698a6f863de07709c94d4c5e14ba1ac4fd4c04090325c"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /ultrasonic/rear_distance

- 逻辑实体：`agv:ros:interface:ultrasonic-rear-distance`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:ultrasonic-rear-distance`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/ultrasonic_controlled_motor/src/dyp_ultrasonic_legacy_adapter.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | std_msgs/Float32 |
| `ros_name` | /ultrasonic/rear_distance |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/trajectory_recorder/src/trajectory_recorder.cpp` | 888 | `subscribes` | `c971b301b5907f52e00034491d77dcf5c8beb9cd04b67ef4ab2c5d5b97afa8c6` |
| `src/trajectory_recorder/src/trajectory_tracker.cpp` | 3856 | `subscribes` | `b13ba9a028ec7abd7b3956173e7cc20bc3a123038872ec4ea9c3a159ccf795c7` |
| `src/ultrasonic_controlled_motor/src/dyp_ultrasonic_legacy_adapter.cpp` | 58 | `publishes` | `a507058ba8b4df070ab58507bee19f02ea54df4a1a19d43ba398bac04d3286b7` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/ultrasonic_controlled_motor--2e98007ce616|agv:ros:package:ultrasonic_controlled_motor]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/dyp_ultrasonic_legacy_adapter--b2f54bdcab46|agv:ros:node:dyp_ultrasonic_legacy_adapter]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_recorder--4850a1d9f230|agv:ros:node:trajectory_recorder]] → `subscribes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_tracker--3031ab8e89fc|agv:ros:node:trajectory_tracker]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/ultrasonic-rear-distance--875cdec8b4fb|agv:ros:interface:ultrasonic-rear-distance]]
