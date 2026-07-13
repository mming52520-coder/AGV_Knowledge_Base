---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:trajectory_tracker"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:node:trajectory_tracker"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:trajectory_tracker"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_node"
title: "trajectory_tracker"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "d606fd97e4c9f1abec9fa27ee625bac6c7f0aaae92b3898689141d32776a4688"
relation_fingerprint: "8e4d8d6f03306e79560543bd4327d0e39056d0cb1331548b9d6fe0527397836e"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# trajectory_tracker

- 逻辑实体：`agv:ros:node:trajectory_tracker`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:node:trajectory_tracker`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/_index|Nodes]]
- 代码证据主路径：`src/trajectory_recorder/src/trajectory_tracker.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` | trajectory_tracker |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` | /trajectory_tracker |
| `status` | compatibility |
| `type` | ros_node |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/trajectory_recorder/src/trajectory_tracker.cpp` | 1 | `node_source` | `b13ba9a028ec7abd7b3956173e7cc20bc3a123038872ec4ea9c3a159ccf795c7` |

## 出向关系

- `package` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu-reset_calibration--92101a8c204c|agv:ros:service:imu-reset-calibration]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu-set_forward--a8b86ae4edbd|agv:ros:service:imu-set-forward]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu-set_zero--cafbe217e891|agv:ros:service:imu-set-zero]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/steering-save_params--9cb80ef2e02d|agv:ros:service:steering-save-params]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/steering-set_origin--cb8c38d86987|agv:ros:service:steering-set-origin]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-pause--1d26c34d770a|agv:ros:service:trajectory-pause]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-play--bb449507544e|agv:ros:service:trajectory-play]]
- `provides_services` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-stop--477f96acba29|agv:ros:service:trajectory-stop]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv-task_state--5dfdad5e839f|agv:ros:interface:agv-task-state]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/chassis-cmd--f60fe5d4d5a2|agv:ros:interface:chassis-cmd]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/fused_odom--e73c04c78ed4|agv:ros:interface:fused-odom]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/odom--1e74762c157b|agv:ros:interface:odom]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory_status--d64b6a185c5c|agv:ros:interface:trajectory-status]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-ultrasonic_state--c42cfd559c46|agv:ros:interface:trajectory-ultrasonic-state]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_avg_distance--6dc5944f4576|agv:ros:interface:ultrasonic-left-avg-distance]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_dual_steering_ratio--2f93c484368e|agv:ros:interface:ultrasonic-left-dual-steering-ratio]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_front_filtered--4cd49d5c7471|agv:ros:interface:ultrasonic-left-front-filtered]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_parallel_error--36f2e0f7e269|agv:ros:interface:ultrasonic-left-parallel-error]]
- `publishes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_rear_filtered--28cb9a63c3d7|agv:ros:interface:ultrasonic-left-rear-filtered]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-soc--fb01514bedd7|agv:ros:interface:battery-h56br-soc]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-distances--95d581d0b6c4|agv:ros:interface:ultrasonic-distances]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-front_distance--f2df0d6f13fc|agv:ros:interface:ultrasonic-front-distance]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-front_status--9cf5e5dd81ab|agv:ros:interface:ultrasonic-front-status]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_distance--1240d1cca41f|agv:ros:interface:ultrasonic-left-distance]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_status--076d80f3e514|agv:ros:interface:ultrasonic-left-status]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-rear_distance--875cdec8b4fb|agv:ros:interface:ultrasonic-rear-distance]]
- `subscribes` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-right_distance--ce2626276c17|agv:ros:interface:ultrasonic-right-distance]]

## 入向关系

- 无

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/trajectory_tracker--3031ab8e89fc|agv:ros:node:trajectory_tracker]]
