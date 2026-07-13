---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:hk_ao_remote"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:hk_ao_remote"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:hk_ao_remote"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "hk_ao_remote"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "8fbe935f088ce10effea366d5134f573835f72c25f0cc74bc86ede19af4e4bf6"
relation_fingerprint: "dbd5dc0e4bfe53a36c9372844eec61b45f52abea9e2684c13b5c51c67b4cb29f"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# hk_ao_remote

- 逻辑实体：`agv:ros:node:hk_ao_remote`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:hk_ao_remote`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/analog_controlled_motor/src/hk_ao_remote.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | hk_ao_remote |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /hua_kong_ao_simple |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/analog_controlled_motor/src/hk_ao_remote.cpp` | 1 | `node_source` | `bf76aaa1481cf51f10a7cf3b259a71e486c1f6f181de400d831b0c7fe129238f` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/analog_controlled_motor--7f945fabfb29|agv:ros:package:analog_controlled_motor]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/hk_ao_remote--ad5e24d09dba|agv:ros:node:hk_ao_remote]]
