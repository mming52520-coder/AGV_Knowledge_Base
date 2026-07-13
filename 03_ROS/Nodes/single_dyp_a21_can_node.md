---
id: "agv:ros:node:single_dyp_a21_can_node"
type: ros_node
ros_name: "/single_dyp_a21_can_node"
executable: "single_dyp_a21_can_node"
status: available
review: generated
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/ultrasonic_controlled_motor]]"
parent: "[[../../01_Project_AGV/Layers/传感器与设备驱动层]]"
publishes: ["[[../Interfaces/ultrasonic-distance]]", "[[../Interfaces/ultrasonic-status]]"]
subscribes: []
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, ultrasonic_controlled_motor]
---

# single_dyp_a21_can_node

## 职责

单路 DYP-A21 CAN 超声读取工具。

## 身份

- ROS 默认名：`/single_dyp_a21_can_node`
- 可执行入口：`single_dyp_a21_can_node`
- 所属 Package：[[../Packages/ultrasonic_controlled_motor]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/ultrasonic-distance]]
- 发布：[[../Interfaces/ultrasonic-status]]

## Launch

- 当前默认 Launch 中未发现直接启动项。

## 源码证据

- 三号车 `src/ultrasonic_controlled_motor/src/single_dyp_a21_can.cpp:325`

## 复核说明

CMake 中存在可执行目标，但当前三号车默认 Launch 未启动。

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
