---
id: "agv:ros:package:h56br_driver"
type: ros_package
status: active
review: generated
project: AGV
version: "0.1.0"
vehicles: [一号车, 二号车, 三号车]
parent: "[[../../01_Project_AGV/Layers/传感器与设备驱动层]]"
source_scope: 三号车当前工作区与三车差异扫描
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Package, h56br_driver]
---

# h56br_driver

## 职责

H56BR 电池表的 ROS Noetic 驱动，提供状态 Topic 与标定/配置 Service。

## 车辆分布

- 一号车、二号车、三号车
- 三车聚合快照一致。

## 构建与运行

- 版本：`0.1.0`
- 可执行目标：`h56br_node`
- 主要依赖：`roscpp`、`std_msgs`、`message_generation`、`message_runtime`

## 源码证据

- 三号车 `src/h56br_driver/package.xml`
- 三号车 `src/h56br_driver/src/h56br_node.cpp`
- 三号车 `src/h56br_driver/launch/h56br.launch`

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
