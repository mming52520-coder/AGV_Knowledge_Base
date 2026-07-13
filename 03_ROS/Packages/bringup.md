---
id: "agv:ros:package:bringup"
type: ros_package
status: active
review: generated
project: AGV
version: "0.0.0"
vehicles: [一号车, 二号车, 三号车]
parent: "[[../../01_Project_AGV/Layers/启动与外部通信层]]"
source_scope: 三号车当前工作区与三车差异扫描
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Package, bringup]
---

# bringup

## 职责

整车基础节点的组合启动入口。

## 车辆分布

- 一号车、二号车、三号车
- 三号车 Bringup 引入 chassis_bridge、drive_feedback_odom 和 steering_remote，和一/二号车启动组合不同。

## 构建与运行

- 版本：`0.0.0`
- 可执行目标：`无独立可执行目标`
- 主要依赖：`roscpp`、`rospy`、`std_msgs`

## 源码证据

- 三号车 `src/bringup/package.xml`
- 三号车 `src/bringup/launch/all_nodes.launch`

## 关联

- [[../../01_Project_AGV/Layers/启动与外部通信层]]
- [[../ROS系统总览]]
