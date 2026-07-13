---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:chassis_controller"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:chassis_controller"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:chassis_controller"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "chassis_controller"
status: "available"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "5fef59743c5452da6dca9d1e5082691e29eac43433c32d43b28855a62bb46746"
relation_fingerprint: "a9c40ea746a777ae280b2293aa3ade6d8efc1e9d834fa3640bd7e536b2870af0"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# chassis_controller

- 逻辑实体：`agv:ros:package:chassis_controller`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:chassis_controller`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/chassis_controller/package.xml`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` |  |
| `status` | available |
| `type` | ros_package |
| `vehicles` | ["二号车","三号车"] |
| `version` | 0.1.0 |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/chassis_controller/package.xml` | 1 | `package_manifest` | `f44ab6cdc8fc7f615d6aacdae000b46e9825020587e627793e4efbfbb663482c` |

## 出向关系

- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/chassis_controller-ChassisCommand--47a572360aab|agv:ros:message:chassis-controller-chassiscommand]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/chassis_controller-ChassisState--f06839446eb9|agv:ros:message:chassis-controller-chassisstate]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_execution--855e548bdcfd|agv:ros:package:agv_execution]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/chassis_bridge--f2b72fa46041|agv:ros:node:chassis_bridge]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/chassis-cmd--f60fe5d4d5a2|agv:ros:interface:chassis-cmd]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/chassis-state--1aa49c890804|agv:ros:interface:chassis-state]] → `related_packages`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/chassis_controller--57f0aa46929c|agv:ros:package:chassis_controller]]
