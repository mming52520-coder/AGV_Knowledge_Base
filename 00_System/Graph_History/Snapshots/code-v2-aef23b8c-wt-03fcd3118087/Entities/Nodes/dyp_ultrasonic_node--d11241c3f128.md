---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:dyp_ultrasonic_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:dyp_ultrasonic_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:dyp_ultrasonic_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "dyp_ultrasonic_node"
status: "available"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "d6b3c7a5011092799fa145099155a31dbf7e0ed0da894c785dcbb8c824f9ee5b"
relation_fingerprint: "1fb7dcad2cc0826c2690a1c21ddffae8e6e73d6444879cfe0b805613809b9003"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# dyp_ultrasonic_node

- 逻辑实体：`agv:ros:node:dyp_ultrasonic_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:dyp_ultrasonic_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/dyp_ultrasonic_driver/src/dyp_ultrasonic_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | dyp_ultrasonic_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /dyp_ultrasonic_node |
| `status` | available |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/dyp_ultrasonic_driver/src/dyp_ultrasonic_node.cpp` | 1 | `node_source` | `bbf411065db498f72f8269f05690c77c522637dc05107522940ca6e5034065d0` |
| `src/dyp_ultrasonic_driver/src/modbus_rtu.cpp` | 1 | `node_source` | `dc7e13772b650cd8d633de532f7002364e22696e750f9c2e7a278a398c5a3eb3` |
| `src/dyp_ultrasonic_driver/src/serial_port.cpp` | 1 | `node_source` | `038a8016e90cf47853aeb0bef853f087fe30fec8f331177b57288f6a58648f22` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/dyp_ultrasonic_driver--32fa83ff01e7|agv:ros:package:dyp_ultrasonic_driver]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-distances--95d581d0b6c4|agv:ros:interface:ultrasonic-distances]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/dyp_ultrasonic_node--d11241c3f128|agv:ros:node:dyp_ultrasonic_node]]
