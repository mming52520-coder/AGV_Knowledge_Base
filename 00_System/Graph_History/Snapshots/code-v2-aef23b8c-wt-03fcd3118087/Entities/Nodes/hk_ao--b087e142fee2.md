---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:hk_ao"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:hk_ao"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:hk_ao"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "hk_ao"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "8b76d132be30503effad211fa1ac86e9766198d4b2f81899183db1905c265d3a"
relation_fingerprint: "4546ccb1f3283bb116c22077cfa029edf2a7974749186f6828447b89ce547dc6"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# hk_ao

- 逻辑实体：`agv:ros:node:hk_ao`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:hk_ao`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/analog_controlled_motor/src/hk_ao.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | hk_ao |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /hua_kong_ao_node |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/analog_controlled_motor/src/hk_ao.cpp` | 1 | `node_source` | `4abb47a3ae0bfc52fc897c4a764b2e3e493b543be17841b8eba35fce8857ef2b` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/analog_controlled_motor--7f945fabfb29|agv:ros:package:analog_controlled_motor]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/hk_ao--b087e142fee2|agv:ros:node:hk_ao]]
