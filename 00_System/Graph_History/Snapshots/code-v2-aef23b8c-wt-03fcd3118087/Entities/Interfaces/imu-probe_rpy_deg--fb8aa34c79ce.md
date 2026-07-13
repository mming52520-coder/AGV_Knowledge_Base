---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:imu-probe-rpy-deg"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:imu-probe-rpy-deg"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:imu-probe-rpy-deg"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/imu/probe_rpy_deg"
status: "diagnostic"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "ffbcb80d35a2749107aafedfb118e2a3ed338a614d05ab8b414cb22ac7c1b09c"
relation_fingerprint: "de8948d5aaa4c825ef13c24e3ede6eac0ac995bf072dbad61cbfba48ddc8dcaf"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /imu/probe_rpy_deg

- 逻辑实体：`agv:ros:interface:imu-probe-rpy-deg`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:imu-probe-rpy-deg`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/trajectory_recorder/src/imu_probe_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | geometry_msgs/Vector3Stamped |
| `ros_name` | /imu/probe_rpy_deg |
| `status` | diagnostic |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/trajectory_recorder/src/imu_probe_node.cpp` | 108 | `publishes` | `d399fcd6ee93484284c6bda916e1112cf92cd5a3c8aed27faf58446e3c81bb0f` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/imu_probe--fa26d8e3a19c|agv:ros:node:imu_probe]] → `publishes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/imu-probe-rpy-deg--fb8aa34c79ce|agv:ros:interface:imu-probe-rpy-deg]]
