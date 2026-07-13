---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:analog_controlled_motor"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:analog_controlled_motor"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:analog_controlled_motor"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "analog_controlled_motor"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "5a3c4d0ef8135508604d371d1e31aaba151c0bcdb08ae8d93bd8dffe30f504d2"
relation_fingerprint: "72d3e67a9b51506dd17ef1a40ea55ce636e016d4a6b95f586d68120b2997d2a8"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# analog_controlled_motor

- 逻辑实体：`agv:ros:package:analog_controlled_motor`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:analog_controlled_motor`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/analog_controlled_motor/package.xml`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` |  |
| `status` | compatibility |
| `type` | ros_package |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` | 0.0.0 |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/analog_controlled_motor/package.xml` | 1 | `package_manifest` | `0110a8b771193311468a98eae1122ffda75c3e68f55b158933e860407de90f05` |

## 出向关系

- 无

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/hk_ao--b087e142fee2|agv:ros:node:hk_ao]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/hk_ao_remote--ad5e24d09dba|agv:ros:node:hk_ao_remote]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]] → `related_packages`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/analog_controlled_motor--7f945fabfb29|agv:ros:package:analog_controlled_motor]]
