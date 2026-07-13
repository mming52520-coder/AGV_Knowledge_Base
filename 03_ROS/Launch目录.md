---
id: "agv:ros:launch-catalog"
type: index
status: active
review: generated
project: AGV
updated: 2026-07-14
source_scope: 三号车当前工作区
tags: [AGV, ROS, Launch]
---

# Launch 目录

## 三号车主要入口

| Launch | 用途 | 关键节点/包含 |
|---|---|---|
| `bringup/launch/all_nodes.launch` | 当前整车基础启动 | [[Nodes/chassis_bridge]]、[[Nodes/drive_feedback_odom]]、[[Nodes/steering_remote]]、磁导航、超声、H56BR |
| `trajectory_recorder/launch/integrated.launch` | record/track 模式组合 | 遥控、磁传感、超声、记录或跟踪 |
| `trajectory_recorder/launch/robot_full.launch` | 新底盘完整跟踪入口 | [[Nodes/trajectory_tracker]]、底盘桥、反馈里程，可选记录 |
| `trajectory_recorder/launch/tracker.launch` | 轨迹跟踪 | [[Nodes/trajectory_tracker]] 与多方向超声 |
| `trajectory_recorder/launch/recorder.launch` | 轨迹记录 | [[Nodes/trajectory_recorder]] 与磁传感 |
| `remote_ctrl/launch/remote_ctrl.launch` | 手柄/云端遥控 | [[Nodes/remote_controller]]、[[Nodes/steering_remote]]、可选底盘桥 |
| `chassis_controller/launch/chassis_bridge.launch` | 新底盘桥 | [[Nodes/chassis_bridge]] |
| `chassis_controller/launch/drive_feedback_odom.launch` | 底盘反馈里程 | [[Nodes/drive_feedback_odom]] |
| `magnetic_controlled_motor/launch/magnetic_nodes.launch` | 磁传感与可选循线 | [[Nodes/mag_sensor_reader]]、可选 [[Nodes/magnetic_follower]] |
| `ultrasonic_controlled_motor/launch/ultrasonic_nodes.launch` | 超声驱动与循墙 | [[Nodes/dyp_a21_can_node]]、[[Nodes/ultrasonic_follower]] |
| `h56br_driver/launch/h56br.launch` | 电池表 | [[Nodes/h56br_node]] |
| `agv_mqtt_bridge/launch/agv_mqtt_bridge.launch` | ROS/MQTT 桥接 | [[Nodes/agv_mqtt_bridge]] |
| `agv_mqtt_bridge/launch/gps_nmea.launch` | GPS NMEA 转换 | [[Nodes/gps_nmea_to_fix_json]] |

## 诊断入口

- `trajectory_recorder/launch/imu_probe.launch` → [[Nodes/imu_probe]]
- `trajectory_recorder/launch/encoder_probe.launch` → [[Nodes/encoder_probe]]
- `trajectory_recorder/launch/yz_aim_probe.launch` → [[Nodes/yz_aim_probe]]
- `chassis_controller/launch/motor_controller_test.launch` → 独立底盘控制器测试

## 兼容与待复核

- `wheeltec_base/launch/wheeltec_base.launch` 属于旧 STM32 底盘链；不在三号车当前 Bringup 主链中。
- `relay/launch/hk_dio.launch` 的 package 声明与本地目录不一致，见 [[Nodes/hk_dio_controller]]。
- 条件组、参数和 Include 会改变实际运行节点；本目录不替代 `roslaunch --nodes` 与运行时检查。

## 关联

- [[ROS系统总览]]
- [[ROS节点与通信图]]
- [[../05_Control/控制权仲裁]]
