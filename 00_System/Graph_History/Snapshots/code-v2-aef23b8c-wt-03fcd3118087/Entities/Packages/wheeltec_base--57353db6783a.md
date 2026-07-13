---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:wheeltec_base"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:wheeltec_base"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:wheeltec_base"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "wheeltec_base"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "d4a5883a14f78f22099e70771e903ed48f97318c262e3c38a125c82dc74de146"
relation_fingerprint: "3bb8b9859218d809067501c37dfdf0e54d7d9571f8e821446511b155807e7c15"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# wheeltec_base

- 逻辑实体：`agv:ros:package:wheeltec_base`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:wheeltec_base`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/wheeltec_base/package.xml`

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
| `version` | 1.0.0 |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/wheeltec_base/package.xml` | 1 | `package_manifest` | `35b18a8e769b45347c6de72dec5fb31912ae09977e8ec90cae78adc42e374667` |

## 出向关系

- 无

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/cmd_vel_adapter--fcd537fae350|agv:ros:node:cmd_vel_adapter]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/wheeltec_robot_node--790717f1d34c|agv:ros:node:wheeltec_robot_node]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/cmd_vel--64adee285a61|agv:ros:interface:cmd-vel]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu--4caf2e58d1e5|agv:ros:interface:imu]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_brake--1d9a50d19a77|agv:ros:interface:motor-brake]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/odom--1e74762c157b|agv:ros:interface:odom]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/PowerVoltage--a406ef04e1cc|agv:ros:interface:powervoltage]] → `related_packages`

## 相对 V1 的变化

- `unchanged`：语义指纹与 V1 一致。
