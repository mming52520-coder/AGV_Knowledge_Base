---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:safety_supervisor_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:safety_supervisor_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:safety_supervisor_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "safety_supervisor_node"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "f74149c67df273aa94bb4aa65d61eeb7748d176c014a478a754d6f04cd41b343"
relation_fingerprint: "6b3cf02bca8b5648e6ba99ada584375a52fc5dbeb85517bb3b7768f2d3fd6e06"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# safety_supervisor_node

- 逻辑实体：`agv:ros:node:safety_supervisor_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:safety_supervisor_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_safety/src/safety_supervisor_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | safety_supervisor_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /safety_supervisor_node |
| `status` | active |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_safety/src/safety_supervisor_node.cpp` | 1 | `node_source` | `6fc04009a55824b6cbbf37ed22b770e68164645af33b7f4b84a8fd6908c74b8a` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_safety--2cb0a140ec4e|agv:ros:package:agv_safety]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/safety-reset_fault--61450899e522|agv:ros:service:safety-reset-fault]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/safety-final_command--366706b48c35|agv:ros:interface:safety-final-command]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/safety-state--b5957c7c06d9|agv:ros:interface:safety-state]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/execution-state--ec53c020b6c5|agv:ros:interface:execution-state]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/perception-state--9e4cc739ed14|agv:ros:interface:perception-state]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/safety-candidate_command--f5c7d63afd32|agv:ros:interface:safety-candidate-command]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/safety-estop_request--ac3e325e6d4c|agv:ros:interface:safety-estop-request]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/vehicle-state--f1837ba03534|agv:ros:interface:vehicle-state]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/safety_supervisor_node--c235eb005bf0|agv:ros:node:safety_supervisor_node]]
