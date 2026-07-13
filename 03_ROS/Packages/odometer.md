---
id: "agv:ros:package:odometer"
type: ros_package
status: compatibility
review: generated
project: AGV
version: "0.0.0"
vehicles: [一号车, 二号车, 三号车]
parent: "[[../../01_Project_AGV/Layers/传感器与设备驱动层]]"
source_scope: 三号车当前工作区与三车差异扫描
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Package, odometer]
---

# odometer

## 职责

基于转向命令和轮编码器数据计算 Ackermann 里程。

## 车辆分布

- 一号车、二号车、三号车
- 三车聚合快照一致；三号车新增 drive_feedback_odom，当前里程来源需按 Launch 选择。

## 构建与运行

- 版本：`0.0.0`
- 可执行目标：`odometer`
- 主要依赖：`roscpp`、`rospy`、`std_msgs`

## 源码证据

- 三号车 `src/odometer/package.xml`
- 三号车 `src/odometer/src/odometer.cpp`

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
