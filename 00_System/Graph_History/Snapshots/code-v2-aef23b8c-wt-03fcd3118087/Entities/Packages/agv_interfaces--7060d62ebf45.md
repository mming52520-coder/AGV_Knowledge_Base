---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_interfaces"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:agv_interfaces"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_interfaces"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "agv_interfaces"
status: "active"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "337668df6728636b5bc3ee462212c1ad5f18a388606726596b922537d8fd874f"
relation_fingerprint: "e36fcf330ee641d6efc1c520222f09ec2918cc4ec883d56616a4f775789b6245"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# agv_interfaces

- 逻辑实体：`agv:ros:package:agv_interfaces`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:agv_interfaces`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/agv_interfaces/package.xml`

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
| `src/agv_interfaces/package.xml` | 1 | `package_manifest` | `2fe4e170be8c2cb0143449382738c316b3210d00d569bd2c4279315ea22d6b1c` |

## 出向关系

- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv_interfaces-ExecutionState--d3b2d1e1d9f5|agv:ros:message:agv-interfaces-executionstate]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv_interfaces-MissionState--e29e3c0a75b5|agv:ros:message:agv-interfaces-missionstate]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv_interfaces-MotionCommand--2cf90aaf9b87|agv:ros:message:agv-interfaces-motioncommand]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv_interfaces-MotionIntent--5dbaee900acc|agv:ros:message:agv-interfaces-motionintent]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv_interfaces-PerceptionState--d5fae088771e|agv:ros:message:agv-interfaces-perceptionstate]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv_interfaces-SafetyState--34f318d1d4e9|agv:ros:message:agv-interfaces-safetystate]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv_interfaces-VehicleState--1295faac9b2a|agv:ros:message:agv-interfaces-vehiclestate]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv_interfaces-CancelMission--e64fd2dd465a|agv:ros:service-type:agv-interfaces-cancelmission]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv_interfaces-PauseMission--8c81cc486490|agv:ros:service-type:agv-interfaces-pausemission]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv_interfaces-ResetSafetyFault--c86e0ea5b8c1|agv:ros:service-type:agv-interfaces-resetsafetyfault]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv_interfaces-ResumeMission--0054e6a2ea1c|agv:ros:service-type:agv-interfaces-resumemission]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv_interfaces-StartMission--941e52c5a6f8|agv:ros:service-type:agv-interfaces-startmission]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_decision--b986d1212fd1|agv:ros:package:agv_decision]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_execution--855e548bdcfd|agv:ros:package:agv_execution]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_legacy--db70b74c409e|agv:ros:package:agv_legacy]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mission--2b7d8642ed63|agv:ros:package:agv_mission]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_perception--b3844e0c0c3f|agv:ros:package:agv_perception]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_safety--2cb0a140ec4e|agv:ros:package:agv_safety]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_state_estimation--99b849143b75|agv:ros:package:agv_state_estimation]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_telemetry--948609af5cdf|agv:ros:package:agv_telemetry]] → `depends_on`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/agv_interfaces--7060d62ebf45|agv:ros:package:agv_interfaces]]
