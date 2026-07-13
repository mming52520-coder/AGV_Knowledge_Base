---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:cmd_vel_adapter"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:cmd_vel_adapter"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:cmd_vel_adapter"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "cmd_vel_adapter"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "81c392e980a132e1588036e62a0066eada25903fcf5f897e3742443d4ceaa0a9"
relation_fingerprint: "8add8e2c01658b226f34fac8485f1b412154db3bc5c85f06a7c01cc006491115"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# cmd_vel_adapter

- 逻辑实体：`agv:ros:node:cmd_vel_adapter`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:cmd_vel_adapter`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/wheeltec_base/src/cmd_vel_adapter.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | cmd_vel_adapter |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /cmd_vel_adapter |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/wheeltec_base/src/cmd_vel_adapter.cpp` | 1 | `node_source` | `68c1dcce28d60b85c990697c7cbe394a3fc4d99035eb4f6a13440fc69665359c` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/wheeltec_base--57353db6783a|agv:ros:package:wheeltec_base]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/cmd_vel--64adee285a61|agv:ros:interface:cmd-vel]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_brake--1d9a50d19a77|agv:ros:interface:motor-brake]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]]

## 入向关系

- 无

## 相对 V1 的变化

- `unchanged`：语义指纹与 V1 一致。
