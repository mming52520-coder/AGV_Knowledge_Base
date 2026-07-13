---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:single_dyp_a21_can_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:single_dyp_a21_can_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:single_dyp_a21_can_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "single_dyp_a21_can_node"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "259a9227aff2ad95ae7c49c998d1145a20e9a76e8559446a7c993720a445d4f8"
relation_fingerprint: "19c5233d23df0cad259581c4f84dedd10b02368fb036290e291cd82ce7383ece"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# single_dyp_a21_can_node

- 逻辑实体：`agv:ros:node:single_dyp_a21_can_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:single_dyp_a21_can_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/ultrasonic_controlled_motor/src/single_dyp_a21_can.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | single_dyp_a21_can_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /single_dyp_a21_can_node |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/ultrasonic_controlled_motor/src/single_dyp_a21_can.cpp` | 1 | `node_source` | `d4f89dd67631256b9c9a086ab290a0bcdca3ddb7ed24f625cc7847529eb25663` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/ultrasonic_controlled_motor--2e98007ce616|agv:ros:package:ultrasonic_controlled_motor]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-distance--cd82ec58bc6b|agv:ros:interface:ultrasonic-distance-atomic]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-status--2bc6c4777842|agv:ros:interface:ultrasonic-status-atomic]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/single_dyp_a21_can_node--3f41f9a6049a|agv:ros:node:single_dyp_a21_can_node]]
