---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:relay"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:relay"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:relay"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "relay"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "5a3c4d0ef8135508604d371d1e31aaba151c0bcdb08ae8d93bd8dffe30f504d2"
relation_fingerprint: "b0c1837cbfc28357a34a3dd26d1cf9a41895edd68c699e96c65995d12a6743f6"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# relay

- 逻辑实体：`agv:ros:package:relay`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:relay`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/relay/package.xml`

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
| `src/relay/package.xml` | 1 | `package_manifest` | `41f21bc8e62ed6a1af89c359f031349af5a4a323101a3d716265fd5114c93539` |

## 出向关系

- 无

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/hk_dio--0a63059567a9|agv:ros:node:hk_dio_controller]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/hk_dio_remote--d5b6ebdf80e7|agv:ros:node:hk_dio_remote]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/hk_dio-channel_--e24647308374|agv:ros:interface:hk-dio-channel]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/hk_dio-input_status--72ab874ae88a|agv:ros:interface:hk-dio-input-status]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/hk_dio-relay_status--d0b9d229a1b0|agv:ros:interface:hk-dio-relay-status]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_brake--1d9a50d19a77|agv:ros:interface:motor-brake]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/hk_dio-get_all_status--1b4aaecd3d0d|agv:ros:service:hk-dio-get-all-status]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/hk_dio-test_connection--c5f31ec270da|agv:ros:service:hk-dio-test-connection]] → `related_packages`

## 相对 V1 的变化

- `unchanged`：语义指纹与 V1 一致。
