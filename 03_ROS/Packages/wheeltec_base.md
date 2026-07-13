---
id: "agv:ros:package:wheeltec_base"
type: ros_package
status: compatibility
review: generated
project: AGV
version: "1.0.0"
vehicles: [一号车, 二号车, 三号车]
parent: "[[../../01_Project_AGV/Layers/底盘与执行抽象层]]"
source_scope: 三号车当前工作区与三车差异扫描
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Package, wheeltec_base]
---

# wheeltec_base

## 职责

STM32 底盘驱动，并把旧控制 Topic 适配为标准 /cmd_vel。

## 车辆分布

- 一号车、二号车、三号车
- 一号车默认 Bringup 使用该链路；三号车主要使用 chassis_controller，但保留本包用于兼容。

## 构建与运行

- 版本：`1.0.0`
- 可执行目标：`wheeltec_robot_node`、`cmd_vel_adapter`
- 主要依赖：`roscpp`、`std_msgs`、`geometry_msgs`、`nav_msgs`、`sensor_msgs`、`serial`、`tf`

## 源码证据

- 三号车 `src/wheeltec_base/package.xml`
- 三号车 `src/wheeltec_base/src/wheeltec_robot.cpp`
- 三号车 `src/wheeltec_base/src/cmd_vel_adapter.cpp`

## 关联

- [[../../01_Project_AGV/Layers/底盘与执行抽象层]]
- [[../ROS系统总览]]
