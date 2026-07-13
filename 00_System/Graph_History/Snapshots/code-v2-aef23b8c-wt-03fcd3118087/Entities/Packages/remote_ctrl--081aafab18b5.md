---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:remote_ctrl"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:remote_ctrl"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:remote_ctrl"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "remote_ctrl"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "5a3c4d0ef8135508604d371d1e31aaba151c0bcdb08ae8d93bd8dffe30f504d2"
relation_fingerprint: "54a2dc285684ac189353c97325c640a21b76dbcdfa0310f169260192bbf19a91"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# remote_ctrl

- 逻辑实体：`agv:ros:package:remote_ctrl`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:remote_ctrl`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/remote_ctrl/package.xml`

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
| `src/remote_ctrl/package.xml` | 1 | `package_manifest` | `fab03b31daec8f98916214b6bcb52329b316725375ca92221ff84f1cb14ddb17` |

## 出向关系

- `depends_on` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/ultrasonic_controlled_motor--2e98007ce616|agv:ros:package:ultrasonic_controlled_motor]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/remote_controller--64f1746fd3dc|agv:ros:node:remote_controller]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/joy--8ee95575fdb7|agv:ros:interface:joy]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_brake--1d9a50d19a77|agv:ros:interface:motor-brake]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-front_status--9cf5e5dd81ab|agv:ros:interface:ultrasonic-front-status]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-rear_status--4db4f184e714|agv:ros:interface:ultrasonic-rear-status]] → `related_packages`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/remote_ctrl--081aafab18b5|agv:ros:package:remote_ctrl]]
