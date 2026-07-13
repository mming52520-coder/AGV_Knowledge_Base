---
id: "agv:ros:node:odometer"
type: ros_node
ros_name: "/ackermann_odometry_node"
executable: "odometer"
status: compatibility
review: generated
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/odometer]]"
parent: "[[../../01_Project_AGV/Layers/传感器与设备驱动层]]"
publishes: ["[[../Interfaces/odom]]", "[[../Interfaces/encoder-state]]"]
subscribes: []
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, odometer]
---

# odometer

## 职责

根据转向命令和轮编码器数据计算 Ackermann 里程。

## 身份

- ROS 默认名：`/ackermann_odometry_node`
- 可执行入口：`odometer`
- 所属 Package：[[../Packages/odometer]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/odom]]
- 发布：[[../Interfaces/encoder-state]]

## Launch

- 当前默认 Launch 中未发现直接启动项。

## 源码证据

- 三号车 `src/odometer/src/odometer.cpp:167`

## 复核说明

三号车可改用 drive_feedback_odom；当前权威里程源需运行时确认。

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
