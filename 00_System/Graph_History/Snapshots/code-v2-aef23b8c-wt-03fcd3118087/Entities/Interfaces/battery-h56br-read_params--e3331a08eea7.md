---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:battery-h56br-read-params"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:service:battery-h56br-read-params"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:battery-h56br-read-params"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/battery/h56br/read_params"
status: "available"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "3412b0e336fd32e8c2720083fdc8ea451e26b579ff2dda90d8ba2430975a7d8c"
relation_fingerprint: "26ddfd2b9d2d753535748dfd6dbbf9458f9e4d71378992a763c0a7debe96b4ac"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /battery/h56br/read_params

- 逻辑实体：`agv:ros:service:battery-h56br-read-params`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:battery-h56br-read-params`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/h56br_driver/src/h56br_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | service |
| `message_type` | unknown |
| `ros_name` | /battery/h56br/read_params |
| `status` | available |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/h56br_driver/src/h56br_node.cpp` | 62 | `provides_services` | `06f7026c7a5db41028e34932d7965102ec7826445214637c7be0cf841c003b24` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/h56br_driver--8cf5e3bb73a1|agv:ros:package:h56br_driver]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/h56br_node--74030e2108af|agv:ros:node:h56br_node]] → `provides_services`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/battery-h56br-read-params--e3331a08eea7|agv:ros:service:battery-h56br-read-params]]
