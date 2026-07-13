---
id: "agv:ros:package:chassis_controller"
type: ros_package
status: active
review: generated
project: AGV
version: "0.1.0"
vehicles: [二号车, 三号车]
parent: "[[../../01_Project_AGV/Layers/底盘与执行抽象层]]"
source_scope: 三号车当前工作区与三车差异扫描
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Package, chassis_controller]
---

# chassis_controller

## 职责

统一底盘控制意图，隔离轨迹/遥控层与 Modbus、CAN、OID 等硬件协议。

## 车辆分布

- 二号车、三号车
- 一号车没有该包；三号车增加驱动反馈里程计节点。

## 构建与运行

- 版本：`0.1.0`
- 可执行目标：`chassis_bridge`、`drive_feedback_odom（三号车）`
- 主要依赖：`roscpp`、`std_msgs`、`message_generation`、`message_runtime`

## 源码证据

- 三号车 `src/chassis_controller/package.xml`
- 三号车 `src/chassis_controller/src/chassis_bridge.cpp`
- 三号车 `src/chassis_controller/launch/chassis_bridge.launch`

## 关联

- [[../../01_Project_AGV/Layers/底盘与执行抽象层]]
- [[../ROS系统总览]]
