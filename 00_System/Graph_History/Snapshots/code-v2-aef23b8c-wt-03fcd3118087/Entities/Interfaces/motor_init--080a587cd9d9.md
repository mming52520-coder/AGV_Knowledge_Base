---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:motor-init"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:service:motor-init"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:motor-init"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/motor_init"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "8c1c9fb1e69e4ae03a62c59deb0da2596ed4f59c756324ce435354971c6867ee"
relation_fingerprint: "fbddc4052c54a30966d296331c216a4bcab94f2bb4ae5076bebcb41af5195683"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /motor_init

- 逻辑实体：`agv:ros:service:motor-init`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:motor-init`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/magnetic_controlled_motor/src/motor_control.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | service |
| `message_type` | unknown |
| `ros_name` | /motor_init |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/magnetic_controlled_motor/src/motor_control.cpp` | 366 | `provides_services` | `ab9568f051ef72710b082c9e9cec34b37bd25b5e92927022100140dce99cb235` |
| `src/trajectory_recorder/src/steering_remote.cpp` | 40 | `provides_services` | `6b7c2094990cf9c047b8febda758d18ff8d2d8e15d2f97eed2156169df2eab76` |
| `src/ultrasonic_controlled_motor/src/motor_control.cpp` | 366 | `provides_services` | `ebf562123626197cefe449061c90c82f3f91198da65ef1e7ddc88f703b112269` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/magnetic_controlled_motor--8bee0b922a0e|agv:ros:package:magnetic_controlled_motor]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/ultrasonic_controlled_motor--2e98007ce616|agv:ros:package:ultrasonic_controlled_motor]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/magnetic_motor_control--463962ff9429|agv:ros:node:magnetic_motor_control]] → `provides_services`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/steering_remote--9fadaeb1fc6d|agv:ros:node:steering_remote]] → `provides_services`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/ultrasonic_motor_control--2b3b9310ac71|agv:ros:node:ultrasonic_motor_control]] → `provides_services`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/motor-init--080a587cd9d9|agv:ros:service:motor-init]]
