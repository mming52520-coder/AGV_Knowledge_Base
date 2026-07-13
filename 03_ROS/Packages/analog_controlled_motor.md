---
id: "agv:ros:package:analog_controlled_motor"
type: ros_package
status: inactive
review: needs-review
project: AGV
version: "0.0.0"
vehicles: [一号车, 二号车, 三号车]
parent: "[[../../01_Project_AGV/Layers/底盘与执行抽象层]]"
source_scope: 三号车当前工作区与三车差异扫描
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Package, analog_controlled_motor]
---

# analog_controlled_motor

## 职责

通过华控模拟量模块输出驱动或转向控制量。

## 车辆分布

- 一号车、二号车、三号车
- 一号车和二号车保留实现；三号车当前只剩包壳且源码处于删除状态，不应视为三号车现行执行链。

## 构建与运行

- 版本：`0.0.0`
- 可执行目标：`hk_ao`、`hk_ao_remote`
- 主要依赖：`roscpp`、`rospy`、`std_msgs`

## 源码证据

- 三号车 `src/analog_controlled_motor/package.xml`

## 关联

- [[../../01_Project_AGV/Layers/底盘与执行抽象层]]
- [[../ROS系统总览]]
