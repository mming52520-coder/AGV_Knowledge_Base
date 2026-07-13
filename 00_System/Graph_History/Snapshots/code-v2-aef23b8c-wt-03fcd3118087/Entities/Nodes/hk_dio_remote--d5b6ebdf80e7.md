---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:hk_dio_remote"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:hk_dio_remote"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:hk_dio_remote"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "hk_dio_remote"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "e664e88465776cf19e63cb9ca613952221a33a29b1e511f1584b416de60fb363"
relation_fingerprint: "ed77e8f4898152c53af338845aa44ff41daab2a3dbf3a2b3a53234fa869cb71a"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# hk_dio_remote

- 逻辑实体：`agv:ros:node:hk_dio_remote`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:hk_dio_remote`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/relay/src/hk_dio_remote.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | hk_dio_remote |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /hk_dio_remote |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/relay/src/hk_dio_remote.cpp` | 1 | `node_source` | `1fd77d8d9fba04ed1d9fa044a699462373798f299e3c105179bb8c910e966857` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/relay--7e8f04764da5|agv:ros:package:relay]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_brake--1d9a50d19a77|agv:ros:interface:motor-brake]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]]

## 入向关系

- 无

## 相对 V1 的变化

- `unchanged`：语义指纹与 V1 一致。
