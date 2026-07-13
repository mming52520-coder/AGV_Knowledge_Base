---
id: "agv:ros:package:trajectory_recorder"
type: ros_package
status: active
review: generated
project: AGV
version: "1.0.0"
vehicles: [一号车, 二号车, 三号车]
parent: "[[../../01_Project_AGV/Layers/任务与应用编排层]]"
source_scope: 三号车当前工作区与三车差异扫描
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Package, trajectory_recorder]
---

# trajectory_recorder

## 职责

轨迹记录、保存、回放和跟踪，融合磁导航、超声、里程、IMU、电量及底盘反馈。

## 车辆分布

- 一号车、二号车、三号车
- 三号车是最新变体，增加实时磁标志、驱动反馈里程和多种硬件探针。

## 构建与运行

- 版本：`1.0.0`
- 可执行目标：`trajectory_recorder`、`trajectory_tracker`、`imu_probe`、`steering_remote`、`encoder_probe（三号车）`、`yz_aim_probe（三号车）`
- 主要依赖：`roscpp`、`std_msgs`、`std_srvs`、`geometry_msgs`、`nav_msgs`、`sensor_msgs`、`tf`、`magnetic_controlled_motor`、`ultrasonic_controlled_motor`、`chassis_controller`

## 源码证据

- 三号车 `src/trajectory_recorder/package.xml`
- 三号车 `src/trajectory_recorder/src/trajectory_recorder.cpp`
- 三号车 `src/trajectory_recorder/src/trajectory_tracker.cpp`
- 三号车 `src/trajectory_recorder/launch/tracker.launch`

## 关联

- [[../../01_Project_AGV/Layers/任务与应用编排层]]
- [[../ROS系统总览]]
