---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:odometer"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:odometer"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:odometer"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "odometer"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "5a3c4d0ef8135508604d371d1e31aaba151c0bcdb08ae8d93bd8dffe30f504d2"
relation_fingerprint: "698c36a3ca64307b44d2004eb4bad1ffaccae4213ddae2f54ae18b22769c9c11"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# odometer

- 逻辑实体：`agv:ros:package:odometer`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:odometer`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/odometer/package.xml`

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
| `src/odometer/package.xml` | 1 | `package_manifest` | `609b17ef48f6d7fe185d38a87a59e96920eab305efb6c3172258dfee4277e945` |

## 出向关系

- 无

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/odometer--4d91289aece7|agv:ros:node:odometer]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ackermann_cmd--a9657963ea4a|agv:ros:interface:ackermann-cmd]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/encoder_twist--e5de60543d8b|agv:ros:interface:encoder-twist]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/odom--1e74762c157b|agv:ros:interface:odom]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/wheel_encoder_data--3690ed9ff087|agv:ros:interface:wheel-encoder-data]] → `related_packages`

## 相对 V1 的变化

- `unchanged`：语义指纹与 V1 一致。
