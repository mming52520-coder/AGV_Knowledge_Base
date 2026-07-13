---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:encoder"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:encoder"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:encoder"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "encoder"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "5a3c4d0ef8135508604d371d1e31aaba151c0bcdb08ae8d93bd8dffe30f504d2"
relation_fingerprint: "cee3542633deec7f8bca6a743ac0ec8765cb4c4fa8823de312265581d960074c"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# encoder

- 逻辑实体：`agv:ros:package:encoder`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:encoder`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/encoder/package.xml`

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
| `src/encoder/package.xml` | 1 | `package_manifest` | `44192d83b64294bfade2320994c4f0f80cf7d1a1d4313b06af9208f9c8c95dfb` |

## 出向关系

- 无

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/rb100_encoder--a141ed92ecec|agv:ros:node:rb100_encoder]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/encoder_angle--bca3ba1cc686|agv:ros:interface:encoder-angle]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/encoder_twist--e5de60543d8b|agv:ros:interface:encoder-twist]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/odom--1e74762c157b|agv:ros:interface:odom]] → `related_packages`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/encoder--0240516ec77b|agv:ros:package:encoder]]
