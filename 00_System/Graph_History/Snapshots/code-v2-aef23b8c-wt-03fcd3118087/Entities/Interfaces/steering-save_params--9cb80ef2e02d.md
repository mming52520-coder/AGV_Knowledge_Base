---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:steering-save-params"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:service:steering-save-params"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:steering-save-params"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/steering/save_params"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "09a24f61b448435a1b0c1c78d9c19debe5b468efcb0e8d2012de534a09f264ed"
relation_fingerprint: "45dec020f23ab87db7e2644d50a011d9ab44c66afb0359c457265960b4b82e64"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /steering/save_params

- 逻辑实体：`agv:ros:service:steering-save-params`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:service:steering-save-params`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/trajectory_recorder/src/trajectory_tracker.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | service |
| `message_type` | unknown |
| `ros_name` | /steering/save_params |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/trajectory_recorder/src/trajectory_tracker.cpp` | 3889 | `provides_services` | `b13ba9a028ec7abd7b3956173e7cc20bc3a123038872ec4ea9c3a159ccf795c7` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_tracker--3031ab8e89fc|agv:ros:node:trajectory_tracker]] → `provides_services`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/steering-save-params--9cb80ef2e02d|agv:ros:service:steering-save-params]]
