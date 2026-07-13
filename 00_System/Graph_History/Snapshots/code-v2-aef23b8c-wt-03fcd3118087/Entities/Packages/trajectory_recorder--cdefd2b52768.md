---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:trajectory_recorder"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:trajectory_recorder"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:trajectory_recorder"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "trajectory_recorder"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "d4a5883a14f78f22099e70771e903ed48f97318c262e3c38a125c82dc74de146"
relation_fingerprint: "9c624efa41e4a6a720c812996c6fcb3d9c8dc9bf5b039fad39f527094fd3d8e7"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# trajectory_recorder

- 逻辑实体：`agv:ros:package:trajectory_recorder`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:trajectory_recorder`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/trajectory_recorder/package.xml`

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
| `src/trajectory_recorder/package.xml` | 1 | `package_manifest` | `174515b2dd2c1ae112aef01eba4c559f996d2170719359549daac3cf31d536e2` |

## 出向关系

- `depends_on` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/chassis_controller--57f0aa46929c|agv:ros:package:chassis_controller]]
- `depends_on` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/dyp_ultrasonic_driver--32fa83ff01e7|agv:ros:package:dyp_ultrasonic_driver]]
- `depends_on` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/magnetic_controlled_motor--8bee0b922a0e|agv:ros:package:magnetic_controlled_motor]]
- `depends_on` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/ultrasonic_controlled_motor--2e98007ce616|agv:ros:package:ultrasonic_controlled_motor]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/imu_probe--fa26d8e3a19c|agv:ros:node:imu_probe]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/steering_remote--9fadaeb1fc6d|agv:ros:node:steering_remote]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_recorder--4850a1d9f230|agv:ros:node:trajectory_recorder]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/trajectory_tracker--3031ab8e89fc|agv:ros:node:trajectory_tracker]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/agv-task_state--5dfdad5e839f|agv:ros:interface:agv-task-state]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-soc--fb01514bedd7|agv:ros:interface:battery-h56br-soc]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/chassis-cmd--f60fe5d4d5a2|agv:ros:interface:chassis-cmd]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/encoder_angle--bca3ba1cc686|agv:ros:interface:encoder-angle]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/fused_odom--e73c04c78ed4|agv:ros:interface:fused-odom]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu-probe_data--dd6a95a4889e|agv:ros:interface:imu-probe-data]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu-probe_rpy_deg--fb8aa34c79ce|agv:ros:interface:imu-probe-rpy-deg]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_sensor-frame--dec47a778ef7|agv:ros:interface:mag-sensor-frame]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/mag_sensor-nail_event--f74eeb1e095f|agv:ros:interface:mag-sensor-nail-event]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_command--6f8461f1fd20|agv:ros:interface:motor-command]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_speed--4e4656e48e31|agv:ros:interface:motor-speed]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/odom--1e74762c157b|agv:ros:interface:odom]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory_status--d64b6a185c5c|agv:ros:interface:trajectory-status]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-ultrasonic_state--c42cfd559c46|agv:ros:interface:trajectory-ultrasonic-state]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-distances--95d581d0b6c4|agv:ros:interface:ultrasonic-distances]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-front_distance--f2df0d6f13fc|agv:ros:interface:ultrasonic-front-distance]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-front_status--9cf5e5dd81ab|agv:ros:interface:ultrasonic-front-status]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_avg_distance--6dc5944f4576|agv:ros:interface:ultrasonic-left-avg-distance]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_distance--1240d1cca41f|agv:ros:interface:ultrasonic-left-distance]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_dual_steering_ratio--2f93c484368e|agv:ros:interface:ultrasonic-left-dual-steering-ratio]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_front_filtered--4cd49d5c7471|agv:ros:interface:ultrasonic-left-front-filtered]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_parallel_error--36f2e0f7e269|agv:ros:interface:ultrasonic-left-parallel-error]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_rear_filtered--28cb9a63c3d7|agv:ros:interface:ultrasonic-left-rear-filtered]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-left_status--076d80f3e514|agv:ros:interface:ultrasonic-left-status]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-rear_distance--875cdec8b4fb|agv:ros:interface:ultrasonic-rear-distance]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/ultrasonic-right_distance--ce2626276c17|agv:ros:interface:ultrasonic-right-distance]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu-reset_calibration--92101a8c204c|agv:ros:service:imu-reset-calibration]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu-set_forward--a8b86ae4edbd|agv:ros:service:imu-set-forward]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/imu-set_zero--cafbe217e891|agv:ros:service:imu-set-zero]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_enable--b1448e6b3664|agv:ros:service:motor-enable]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/motor_init--080a587cd9d9|agv:ros:service:motor-init]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/steering-save_params--9cb80ef2e02d|agv:ros:service:steering-save-params]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/steering-set_origin--cb8c38d86987|agv:ros:service:steering-set-origin]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-pause--1d26c34d770a|agv:ros:service:trajectory-pause]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-play--bb449507544e|agv:ros:service:trajectory-play]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-save--b7dbb55b5e17|agv:ros:service:trajectory-save]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-start_record--d1ef1c28d4da|agv:ros:service:trajectory-start-record]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-stop--477f96acba29|agv:ros:service:trajectory-stop]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/trajectory-stop_record--2819b569b2db|agv:ros:service:trajectory-stop-record]] → `related_packages`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/trajectory_recorder--cdefd2b52768|agv:ros:package:trajectory_recorder]]
