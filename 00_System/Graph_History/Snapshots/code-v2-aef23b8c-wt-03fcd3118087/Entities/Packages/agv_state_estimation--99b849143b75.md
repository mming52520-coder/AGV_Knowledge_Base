---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_state_estimation"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:agv_state_estimation"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_state_estimation"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "agv_state_estimation"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "337668df6728636b5bc3ee462212c1ad5f18a388606726596b922537d8fd874f"
relation_fingerprint: "f27482a875a2a4fadd6c6ac8188349b9ff780abb973c88ca108ea9d00e2308a0"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# agv_state_estimation

- 逻辑实体：`agv:ros:package:agv_state_estimation`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_state_estimation`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/agv_state_estimation/package.xml`

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
| `src/agv_state_estimation/package.xml` | 1 | `package_manifest` | `9ba89556174b3a08926bbd8d63ad1d99bacaf8ee47629b9501f314a8b68fa12f` |

## 出向关系

- `depends_on` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_interfaces--7060d62ebf45|agv:ros:package:agv_interfaces]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_bringup--4378167611a3|agv:ros:package:agv_bringup]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/vehicle_state_estimator_node--f5bf32466a46|agv:ros:node:vehicle_state_estimator_node]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/execution-state--ec53c020b6c5|agv:ros:interface:execution-state]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/odom--1e74762c157b|agv:ros:interface:odom]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/perception-state--9e4cc739ed14|agv:ros:interface:perception-state]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/vehicle-state--f1837ba03534|agv:ros:interface:vehicle-state]] → `related_packages`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/agv_state_estimation--99b849143b75|agv:ros:package:agv_state_estimation]]
