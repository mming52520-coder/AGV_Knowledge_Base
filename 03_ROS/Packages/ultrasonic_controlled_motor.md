---
id: "agv:ros:package:ultrasonic_controlled_motor"
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
tags: [AGV, ROS, Package, ultrasonic_controlled_motor]
---

# ultrasonic_controlled_motor

## 职责

读取 DYP-A21 超声传感器，发布距离/状态，并产生限速、停车或循墙控制建议。

## 车辆分布

- 一号车、二号车、三号车
- 三号车移除了本包 motor_control_node 可执行目标，控制输出交由新底盘链路处理。

## 构建与运行

- 版本：`0.0.0`
- 可执行目标：`dyp_a21_can_node`、`single_dyp_a21_can_node`、`ultrasonic_follower`、`motor_control_node（一/二号车）`
- 主要依赖：`roscpp`、`rospy`、`std_msgs`、`message_generation`、`message_runtime`

## 源码证据

- 三号车 `src/ultrasonic_controlled_motor/package.xml`
- 三号车 `src/ultrasonic_controlled_motor/src/dyp_a21_can.cpp`
- 三号车 `src/ultrasonic_controlled_motor/src/ultrasonic_follower.cpp`

## 关联

- [[../../01_Project_AGV/Layers/导航决策与安全层]]
- [[../ROS系统总览]]
