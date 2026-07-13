---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:ultrasonic-distance-atomic"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:ultrasonic-distance-atomic"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:ultrasonic-distance-atomic"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/ultrasonic/distance"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "5229d8c92f781f6baefe4aa0ae87b7c44ec66e9db7b69331f0ea9c7df5f14a8a"
relation_fingerprint: "5ea84d8f930fff5db55be77ae44d2afaaa87534df0177262008992ead2652f8c"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /ultrasonic/distance

- 逻辑实体：`agv:ros:interface:ultrasonic-distance-atomic`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:ultrasonic-distance-atomic`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/ultrasonic_controlled_motor/src/single_dyp_a21_can.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | std_msgs/Float32 |
| `ros_name` | /ultrasonic/distance |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/ultrasonic_controlled_motor/src/single_dyp_a21_can.cpp` | 285 | `publishes` | `d4f89dd67631256b9c9a086ab290a0bcdca3ddb7ed24f625cc7847529eb25663` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/ultrasonic_controlled_motor--2e98007ce616|agv:ros:package:ultrasonic_controlled_motor]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/single_dyp_a21_can_node--3f41f9a6049a|agv:ros:node:single_dyp_a21_can_node]] → `publishes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/ultrasonic-distance-atomic--cd82ec58bc6b|agv:ros:interface:ultrasonic-distance-atomic]]
