---
id: "agv:ros:package:magnetic_controlled_motor"
type: ros_package
status: active
review: generated
project: AGV
version: "0.0.0"
vehicles: [一号车, 二号车, 三号车]
parent: "[[../../01_Project_AGV/Layers/导航决策与安全层]]"
source_scope: 三号车当前工作区与三车差异扫描
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Package, magnetic_controlled_motor]
---

# magnetic_controlled_motor

## 职责

读取 MS16A 磁信号、生成磁帧与磁钉事件，并提供磁循线控制建议。

## 车辆分布

- 一号车、二号车、三号车
- 三号车移除了本包 motor_control 可执行目标，执行链转向 steering_remote/chassis_controller。

## 构建与运行

- 版本：`0.0.0`
- 可执行目标：`mag_sensor_reader`、`magnetic_follower`、`motor_control（一/二号车）`
- 主要依赖：`roscpp`、`rospy`、`std_msgs`、`nav_msgs`、`message_generation`、`message_runtime`

## 源码证据

- 三号车 `src/magnetic_controlled_motor/package.xml`
- 三号车 `src/magnetic_controlled_motor/src/mag_sensor_reader.cpp`
- 三号车 `src/magnetic_controlled_motor/src/magnetic_follower.cpp`

## 关联

- [[../../01_Project_AGV/Layers/导航决策与安全层]]
- [[../ROS系统总览]]
