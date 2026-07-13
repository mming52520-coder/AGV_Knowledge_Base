---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:steering_remote"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:steering_remote"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:steering_remote"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "steering_remote"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "ae04007fee7fbaa4b664aa53bbfbe64dc0866191cc0a171a70a3599f78b85ecb"
relation_fingerprint: "991f40f273ce387cf8a6fec73488a832d132c027392eb02a7cca0e6a9752774a"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# steering_remote

- 逻辑实体：`agv:ros:node:steering_remote`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:steering_remote`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/trajectory_recorder/src/steering_remote.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | steering_remote |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /steering_remote |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/trajectory_recorder/src/serial_port.cpp` | 1 | `node_source` | `7755904f6bf452fe9e6247621e14eef23031735825301b448ba6ac762096791f` |
| `src/trajectory_recorder/src/steering_motor.cpp` | 1 | `node_source` | `75c7133c5c5a5b7e9d977b2687382621e6183cb40548a66d9753f56c9bc7919c` |
| `src/trajectory_recorder/src/steering_remote.cpp` | 1 | `node_source` | `6b7c2094990cf9c047b8febda758d18ff8d2d8e15d2f97eed2156169df2eab76` |
| `src/trajectory_recorder/src/yz_aim_servo.cpp` | 1 | `node_source` | `62a2cc0aaf76ec2ea312473264ff3bc34bb937a91c8401531d9f4cc10278dbb7` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_enable--b1448e6b3664|agv:ros:service:motor-enable]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_init--080a587cd9d9|agv:ros:service:motor-init]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/steering_remote--9fadaeb1fc6d|agv:ros:node:steering_remote]]
