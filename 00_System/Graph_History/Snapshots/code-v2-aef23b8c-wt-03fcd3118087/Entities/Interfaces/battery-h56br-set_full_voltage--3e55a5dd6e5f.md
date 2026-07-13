---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:battery-h56br-set-full-voltage"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:service:battery-h56br-set-full-voltage"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:battery-h56br-set-full-voltage"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/battery/h56br/set_full_voltage"
status: "available"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "ca7bd6f18a0da4123a137c6ee91b4c506074d6c78f7e566d5b9a1020ef94f8f5"
relation_fingerprint: "668478551487ca3e2742382d9f8d7069e97e98d3728bee982e6194bab54daaa3"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /battery/h56br/set_full_voltage

- 逻辑实体：`agv:ros:service:battery-h56br-set-full-voltage`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:battery-h56br-set-full-voltage`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/h56br_driver/src/h56br_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | service |
| `message_type` | unknown |
| `ros_name` | /battery/h56br/set_full_voltage |
| `status` | available |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/h56br_driver/src/h56br_node.cpp` | 66 | `provides_services` | `06f7026c7a5db41028e34932d7965102ec7826445214637c7be0cf841c003b24` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/h56br_driver--8cf5e3bb73a1|agv:ros:package:h56br_driver]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/h56br_node--74030e2108af|agv:ros:node:h56br_node]] → `provides_services`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/battery-h56br-set-full-voltage--3e55a5dd6e5f|agv:ros:service:battery-h56br-set-full-voltage]]
