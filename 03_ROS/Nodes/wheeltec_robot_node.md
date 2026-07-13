---
id: "agv:ros:node:wheeltec_robot_node"
type: ros_node
ros_name: "/wheeltec_robot"
executable: "wheeltec_robot_node"
status: compatibility
review: verified
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/wheeltec_base]]"
parent: "[[../../01_Project_AGV/Layers/底盘与执行抽象层]]"
publishes: ["[[../Interfaces/odom]]", "[[../Interfaces/imu]]"]
subscribes: ["[[../Interfaces/cmd-vel]]"]
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, wheeltec_base]
---

# wheeltec_robot_node

## 职责

通过串口与 STM32 底盘通信，接收 Twist 并发布里程、IMU 和电压。

## 身份

- ROS 默认名：`/wheeltec_robot`
- 可执行入口：`wheeltec_robot_node`
- 所属 Package：[[../Packages/wheeltec_base]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/odom]]
- 发布：[[../Interfaces/imu]]
- 订阅：[[../Interfaces/cmd-vel]]

## Launch

- `src/wheeltec_base/launch/wheeltec_base.launch`

## 源码证据

- 三号车 `src/wheeltec_base/src/wheeltec_robot.cpp:8,299-302`

## 复核说明

三号车保留兼容实现，但当前主 Bringup 使用新底盘桥。

## 关联

- [[../../01_Project_AGV/Layers/底盘与执行抽象层]]
- [[../ROS系统总览]]
