---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_mission"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:agv_mission"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_mission"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "agv_mission"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "337668df6728636b5bc3ee462212c1ad5f18a388606726596b922537d8fd874f"
relation_fingerprint: "372cd81f7ee7c7059630f44a404ad19296362639ca8fd9e5bad3b94bcefd9849"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# agv_mission

- 逻辑实体：`agv:ros:package:agv_mission`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_mission`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/agv_mission/package.xml`

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
| `src/agv_mission/package.xml` | 1 | `package_manifest` | `4f85c15c749089eca5605c38744b92c474812eb020fec17032fe0ba4bea14765` |

## 出向关系

- `depends_on` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_interfaces--7060d62ebf45|agv:ros:package:agv_interfaces]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_bringup--4378167611a3|agv:ros:package:agv_bringup]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/mission_node--3f300b35dfe3|agv:ros:node:mission_node]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-state--1bf376c688d5|agv:ros:interface:mission-state]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-trajectory_file--3e1456a7d19b|agv:ros:interface:mission-trajectory-file]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-cancel--ef29c62b4565|agv:ros:service:mission-cancel]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-pause--ced3313a25c7|agv:ros:service:mission-pause]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-resume--63c8ad51735d|agv:ros:service:mission-resume]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mission-start--d482eb3f7b4d|agv:ros:service:mission-start]] → `related_packages`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/agv_mission--2b7d8642ed63|agv:ros:package:agv_mission]]
