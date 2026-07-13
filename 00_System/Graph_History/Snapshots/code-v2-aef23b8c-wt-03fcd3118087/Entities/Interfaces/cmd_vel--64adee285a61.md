---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:cmd-vel"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:cmd-vel"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:cmd-vel"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/cmd_vel"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "60da51357391a2afb8542cda0b78d55a79def9d4f2b357a71a74c5fc8413b34b"
relation_fingerprint: "78bbc7476bce335857844050612a02055ba0b3351ee02fb92aa054d7616999ee"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /cmd_vel

- 逻辑实体：`agv:ros:interface:cmd-vel`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:cmd-vel`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/agv_execution/src/chassis_gateway_node.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | geometry_msgs/Twist |
| `ros_name` | /cmd_vel |
| `status` | active |
| `type` | ros_interface |
| `vehicles` | [] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_execution/src/chassis_gateway_node.cpp` | 48 | `publishes` | `f30568932c8e70e73f4ee7677a7d3905faa2e11bc0864fa8547c64a92e3b60b7` |
| `src/wheeltec_base/src/cmd_vel_adapter.cpp` | 46 | `publishes` | `68c1dcce28d60b85c990697c7cbe394a3fc4d99035eb4f6a13440fc69665359c` |
| `src/wheeltec_base/src/wheeltec_robot.cpp` | 302 | `subscribes` | `48ac16949d4c430b1c20fd50685f08402e2dbd589ef9b8e353255d916dc77bdc` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_execution--855e548bdcfd|agv:ros:package:agv_execution]]
- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/wheeltec_base--57353db6783a|agv:ros:package:wheeltec_base]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/chassis_gateway_node--e753a2e58776|agv:ros:node:chassis_gateway_node]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/cmd_vel_adapter--fcd537fae350|agv:ros:node:cmd_vel_adapter]] → `publishes`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/wheeltec_robot_node--790717f1d34c|agv:ros:node:wheeltec_robot_node]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/cmd-vel--64adee285a61|agv:ros:interface:cmd-vel]]
