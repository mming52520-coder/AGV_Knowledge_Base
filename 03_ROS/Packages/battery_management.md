---
id: "agv:ros:package:battery_management"
type: ros_package
status: archived
review: verified
project: AGV
version: "0.0.0"
vehicles: [一号车, 二号车, 三号车]
parent: "[[../../01_Project_AGV/Layers/传感器与设备驱动层]]"
source_scope: 三号车当前工作区与三车差异扫描
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Package, battery_management]
---

# battery_management

## 职责

旧库仑计电量管理实现。

## 车辆分布

- 一号车、二号车、三号车
- 目录名带 _archived，当前电量实现应以 h56br_driver 为准。

## 构建与运行

- 版本：`0.0.0`
- 可执行目标：`coulomb_meter`
- 主要依赖：`roscpp`、`rospy`、`std_msgs`

## 源码证据

- 三号车 `src/_archived_battery_management/package.xml`
- 三号车 `src/_archived_battery_management/src/coulomb_meter.cpp`

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
