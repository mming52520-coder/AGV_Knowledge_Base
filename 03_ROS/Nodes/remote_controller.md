---
id: "agv:ros:node:remote_controller"
type: ros_node
ros_name: "/remote_controller"
executable: "remote_controller"
status: active
review: verified
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/remote_ctrl]]"
parent: "[[../../01_Project_AGV/Layers/任务与应用编排层]]"
publishes: ["[[../Interfaces/chassis-cmd]]", "[[../Interfaces/motor-command]]", "[[../Interfaces/motor-speed]]", "[[../Interfaces/motor-brake]]"]
subscribes: ["[[../Interfaces/ultrasonic-status]]"]
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, remote_ctrl]
---

# remote_controller

## 职责

处理本地手柄与云端摇杆，输出遥控意图并接入超声安全状态。

## 身份

- ROS 默认名：`/remote_controller`
- 可执行入口：`remote_controller`
- 所属 Package：[[../Packages/remote_ctrl]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/chassis-cmd]]
- 发布：[[../Interfaces/motor-command]]
- 发布：[[../Interfaces/motor-speed]]
- 发布：[[../Interfaces/motor-brake]]
- 订阅：[[../Interfaces/ultrasonic-status]]

## Launch

- `src/remote_ctrl/launch/remote_ctrl.launch`
- `src/remote_ctrl/launch/steering_only.launch`

## 源码证据

- 三号车 `src/remote_ctrl/src/remote_controller.cpp:53,79-107,194,811`

## 复核说明

三号车可发布 /chassis/cmd；旧 Topic 的实际发布能力随车辆版本和输出模式变化。

## 关联

- [[../../01_Project_AGV/Layers/任务与应用编排层]]
- [[../ROS系统总览]]
