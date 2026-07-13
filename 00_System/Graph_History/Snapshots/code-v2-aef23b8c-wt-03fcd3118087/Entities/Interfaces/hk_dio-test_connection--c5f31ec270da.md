---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:hk-dio-test-connection"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:service:hk-dio-test-connection"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:hk-dio-test-connection"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/hk_dio/test_connection"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "6347b5d457398bcfe491b62a1fae4843bb735ff383487aeaa18e2982f4568379"
relation_fingerprint: "91bb66aaab1421147f22951d6c6ee43a952a213dc9b58ebb7dbac40a5f22b330"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /hk_dio/test_connection

- 逻辑实体：`agv:ros:service:hk-dio-test-connection`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:hk-dio-test-connection`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/relay/src/hk_dio.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | service |
| `message_type` | unknown |
| `ros_name` | /hk_dio/test_connection |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/relay/src/hk_dio.cpp` | 744 | `provides_services` | `f58219ece14ea3da46899038faa2a19b2fe31aa128b7fe1de30f42a6af4ab70f` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/relay--7e8f04764da5|agv:ros:package:relay]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/hk_dio--0a63059567a9|agv:ros:node:hk_dio_controller]] → `provides_services`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/hk-dio-test-connection--c5f31ec270da|agv:ros:service:hk-dio-test-connection]]
