---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:dyp_ultrasonic_driver"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:dyp_ultrasonic_driver"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:dyp_ultrasonic_driver"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "dyp_ultrasonic_driver"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "c3c713f5a6dc9bfe1cfb95a444d744f81b252f9207ef9f477467759d5962f55d"
relation_fingerprint: "881d6fa8253e5a2209ed51df1e4b7c3ea34fd11f401323b1d897767fbdd5ab14"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# dyp_ultrasonic_driver

- 逻辑实体：`agv:ros:package:dyp_ultrasonic_driver`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:dyp_ultrasonic_driver`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/dyp_ultrasonic_driver/package.xml`

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
| `version` | 0.1.0 |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/dyp_ultrasonic_driver/package.xml` | 1 | `package_manifest` | `abf17e5120a1c7f9334bb4ec784822e6c3d66439fe20d45355edf3aa7d298a1e` |

## 出向关系

- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/dyp_ultrasonic_driver-UltrasonicDistances--3852caede19a|agv:ros:message:dyp-ultrasonic-driver-ultrasonicdistances]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_perception--b3844e0c0c3f|agv:ros:package:agv_perception]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/ultrasonic_controlled_motor--2e98007ce616|agv:ros:package:ultrasonic_controlled_motor]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/dyp_ultrasonic_node--d11241c3f128|agv:ros:node:dyp_ultrasonic_node]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-distances--95d581d0b6c4|agv:ros:interface:ultrasonic-distances]] → `related_packages`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/dyp_ultrasonic_driver--32fa83ff01e7|agv:ros:package:dyp_ultrasonic_driver]]
