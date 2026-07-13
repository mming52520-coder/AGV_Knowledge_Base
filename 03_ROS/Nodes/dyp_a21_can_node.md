---
id: "agv:ros:node:dyp_a21_can_node"
type: ros_node
ros_name: "/dyp_a21_can_node"
executable: "dyp_a21_can_node"
status: active
review: verified
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

# dyp_a21_can_node

## 职责

读取多方向 DYP-A21 CAN 超声数据并发布距离与状态。

## 身份

- ROS 默认名：`/dyp_a21_can_node`
- 可执行入口：`dyp_a21_can_node`
- 所属 Package：[[../Packages/ultrasonic_controlled_motor]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/ultrasonic-distance]]
- 发布：[[../Interfaces/ultrasonic-status]]

## Launch

- `src/bringup/launch/all_nodes.launch`
- `src/ultrasonic_controlled_motor/launch/ultrasonic_nodes.launch`

## 源码证据

- 三号车 `src/ultrasonic_controlled_motor/src/dyp_a21_can.cpp:299-345,395`

## 复核说明

具体方向与 Topic 由 sensor_side 和参数决定。

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
