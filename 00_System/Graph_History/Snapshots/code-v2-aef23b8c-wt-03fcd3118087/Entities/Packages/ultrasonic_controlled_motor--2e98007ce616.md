---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:ultrasonic_controlled_motor"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:ultrasonic_controlled_motor"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:ultrasonic_controlled_motor"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "ultrasonic_controlled_motor"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "5a3c4d0ef8135508604d371d1e31aaba151c0bcdb08ae8d93bd8dffe30f504d2"
relation_fingerprint: "584be7d2e0c6e67b97c2d803acf81a0873c68d40217e40445d5a85ea769a99a1"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# ultrasonic_controlled_motor

- 逻辑实体：`agv:ros:package:ultrasonic_controlled_motor`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:ultrasonic_controlled_motor`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/ultrasonic_controlled_motor/package.xml`

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
| `src/ultrasonic_controlled_motor/package.xml` | 1 | `package_manifest` | `df954087b21c2f8e0f1753be1e8a2d1a735b49851c2a2d0c0477141e4f654e3c` |

## 出向关系

- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic_controlled_motor-UltrasonicStatus--9516db868368|agv:ros:message:ultrasonic-controlled-motor-ultrasonicstatus]]
- `depends_on` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/dyp_ultrasonic_driver--32fa83ff01e7|agv:ros:package:dyp_ultrasonic_driver]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mqtt_bridge--001d465b2aae|agv:ros:package:agv_mqtt_bridge]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/remote_ctrl--081aafab18b5|agv:ros:package:remote_ctrl]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/dyp_a21_can_node--6d10dab251e7|agv:ros:node:dyp_a21_can_node]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/dyp_ultrasonic_legacy_adapter--b2f54bdcab46|agv:ros:node:dyp_ultrasonic_legacy_adapter]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/single_dyp_a21_can_node--3f41f9a6049a|agv:ros:node:single_dyp_a21_can_node]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/ultrasonic_follower--a7eeb0b895ef|agv:ros:node:ultrasonic_follower]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/ultrasonic_motor_control--2b3b9310ac71|agv:ros:node:ultrasonic_motor_control]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-distance--cd82ec58bc6b|agv:ros:interface:ultrasonic-distance-atomic]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-distances--95d581d0b6c4|agv:ros:interface:ultrasonic-distances]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-front_distance--f2df0d6f13fc|agv:ros:interface:ultrasonic-front-distance]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-front_status--9cf5e5dd81ab|agv:ros:interface:ultrasonic-front-status]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_distance--1240d1cca41f|agv:ros:interface:ultrasonic-left-distance]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_status--076d80f3e514|agv:ros:interface:ultrasonic-left-status]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-rear_distance--875cdec8b4fb|agv:ros:interface:ultrasonic-rear-distance]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-rear_status--4db4f184e714|agv:ros:interface:ultrasonic-rear-status]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-right_distance--ce2626276c17|agv:ros:interface:ultrasonic-right-distance]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-right_status--1b88b10d7f8c|agv:ros:interface:ultrasonic-right-status]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-status--2bc6c4777842|agv:ros:interface:ultrasonic-status-atomic]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_enable--b1448e6b3664|agv:ros:service:motor-enable]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_init--080a587cd9d9|agv:ros:service:motor-init]] → `related_packages`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/ultrasonic_controlled_motor--2e98007ce616|agv:ros:package:ultrasonic_controlled_motor]]
