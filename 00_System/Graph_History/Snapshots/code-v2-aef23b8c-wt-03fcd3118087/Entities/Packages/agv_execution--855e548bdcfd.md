---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_execution"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:agv_execution"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_execution"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "agv_execution"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "337668df6728636b5bc3ee462212c1ad5f18a388606726596b922537d8fd874f"
relation_fingerprint: "5dfa5dcfe33e8ca6fc1a9d1a0ccc4f62cbd45227982264a4c008fe2cb8669c4e"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# agv_execution

- 逻辑实体：`agv:ros:package:agv_execution`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_execution`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/agv_execution/package.xml`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` |  |
| `status` | active |
| `type` | ros_package |
| `vehicles` | ["三号车"] |
| `version` | 0.0.1 |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/agv_execution/package.xml` | 1 | `package_manifest` | `278c9a18076e291a8315a6f9a421307b1839f13a109fcb9311df422e4865c51e` |

## 出向关系

- `depends_on` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_interfaces--7060d62ebf45|agv:ros:package:agv_interfaces]]
- `depends_on` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/chassis_controller--57f0aa46929c|agv:ros:package:chassis_controller]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_bringup--4378167611a3|agv:ros:package:agv_bringup]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_legacy--db70b74c409e|agv:ros:package:agv_legacy]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/chassis_gateway_node--e753a2e58776|agv:ros:node:chassis_gateway_node]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/chassis-cmd--f60fe5d4d5a2|agv:ros:interface:chassis-cmd]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/cmd_vel--64adee285a61|agv:ros:interface:cmd-vel]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/execution-state--ec53c020b6c5|agv:ros:interface:execution-state]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/safety-final_command--366706b48c35|agv:ros:interface:safety-final-command]] → `related_packages`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/agv_execution--855e548bdcfd|agv:ros:package:agv_execution]]
