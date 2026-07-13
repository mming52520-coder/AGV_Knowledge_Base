---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:chassis_gateway_node"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:chassis_gateway_node"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:chassis_gateway_node"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "chassis_gateway_node"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "24a628b444fca402ccee4721d1a88f39f070d75575626a6cae0d59375f0b968f"
relation_fingerprint: "b6a5c1cd70575a37172122e57eb4de0df981396e126eb10e71318ad83d4ee707"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# chassis_gateway_node

- 逻辑实体：`agv:ros:node:chassis_gateway_node`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:chassis_gateway_node`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/agv_execution/src/chassis_gateway_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | chassis_gateway_node |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /chassis_gateway_node |
| `status` | active |
| `type` | ros_node |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_execution/src/chassis_gateway_node.cpp` | 1 | `node_source` | `f30568932c8e70e73f4ee7677a7d3905faa2e11bc0864fa8547c64a92e3b60b7` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_execution--855e548bdcfd|agv:ros:package:agv_execution]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/chassis-cmd--f60fe5d4d5a2|agv:ros:interface:chassis-cmd]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/cmd_vel--64adee285a61|agv:ros:interface:cmd-vel]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/execution-state--ec53c020b6c5|agv:ros:interface:execution-state]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/safety-final_command--366706b48c35|agv:ros:interface:safety-final-command]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/chassis_gateway_node--e753a2e58776|agv:ros:node:chassis_gateway_node]]
