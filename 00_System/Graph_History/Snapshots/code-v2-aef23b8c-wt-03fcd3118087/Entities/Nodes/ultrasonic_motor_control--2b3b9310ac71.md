---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:ultrasonic_motor_control"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:ultrasonic_motor_control"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:ultrasonic_motor_control"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "ultrasonic_motor_control"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "8b397add46c80889cfbdb5c31d9cd3bf58427978cfe4be6742f527b48670dc7a"
relation_fingerprint: "0b567fc931891735f28d2dd04fdceb02b4659478e3273fb8bc981c9b7165e677"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# ultrasonic_motor_control

- 逻辑实体：`agv:ros:node:ultrasonic_motor_control`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:ultrasonic_motor_control`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/ultrasonic_controlled_motor/src/motor_control.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | motor_control_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /ultrasonic_motor_control |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/ultrasonic_controlled_motor/src/motor_control.cpp` | 1 | `node_source` | `ebf562123626197cefe449061c90c82f3f91198da65ef1e7ddc88f703b112269` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/ultrasonic_controlled_motor--2e98007ce616|agv:ros:package:ultrasonic_controlled_motor]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_enable--b1448e6b3664|agv:ros:service:motor-enable]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_init--080a587cd9d9|agv:ros:service:motor-init]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/ultrasonic_motor_control--2b3b9310ac71|agv:ros:node:ultrasonic_motor_control]]
