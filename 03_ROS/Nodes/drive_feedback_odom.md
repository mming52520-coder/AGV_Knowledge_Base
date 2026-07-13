---
id: "agv:ros:node:drive_feedback_odom"
type: ros_node
ros_name: "/drive_feedback_odom"
executable: "drive_feedback_odom"
status: active
review: verified
project: AGV
vehicles: [三号车]
package: "[[../Packages/chassis_controller]]"
parent: "[[../../01_Project_AGV/Layers/传感器与设备驱动层]]"
publishes: ["[[../Interfaces/drive-feedback]]"]
subscribes: ["[[../Interfaces/chassis-state]]"]
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, chassis_controller]
---

# drive_feedback_odom

## 职责

根据底盘反馈派生里程、速度与 Twist 状态。

## 身份

- ROS 默认名：`/drive_feedback_odom`
- 可执行入口：`drive_feedback_odom`
- 所属 Package：[[../Packages/chassis_controller]]
- 车辆：三号车

## 通信接口

- 发布：[[../Interfaces/drive-feedback]]
- 订阅：[[../Interfaces/chassis-state]]

## Launch

- `src/chassis_controller/launch/drive_feedback_odom.launch`

## 源码证据

- 三号车 `src/chassis_controller/src/drive_feedback_odom.cpp:18-24,57-60,186`

## 复核说明

三号车新增，可作为轨迹记录与跟踪的里程来源。

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
