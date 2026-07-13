---
id: "agv:ros:node:cmd_vel_adapter"
type: ros_node
ros_name: "/cmd_vel_adapter"
executable: "cmd_vel_adapter"
status: compatibility
review: verified
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/wheeltec_base]]"
parent: "[[../../01_Project_AGV/Layers/底盘与执行抽象层]]"
publishes: ["[[../Interfaces/cmd-vel]]"]
subscribes: ["[[../Interfaces/motor-command]]", "[[../Interfaces/motor-speed]]", "[[../Interfaces/motor-brake]]"]
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, wheeltec_base]
---

# cmd_vel_adapter

## 职责

把旧驱动、转向和制动 Topic 转换为 geometry_msgs/Twist。

## 身份

- ROS 默认名：`/cmd_vel_adapter`
- 可执行入口：`cmd_vel_adapter`
- 所属 Package：[[../Packages/wheeltec_base]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/cmd-vel]]
- 订阅：[[../Interfaces/motor-command]]
- 订阅：[[../Interfaces/motor-speed]]
- 订阅：[[../Interfaces/motor-brake]]

## Launch

- `src/wheeltec_base/launch/wheeltec_base.launch`

## 源码证据

- 三号车 `src/wheeltec_base/src/cmd_vel_adapter.cpp:46-62,115`

## 复核说明

一号车默认链路使用；三号车主要使用 chassis_controller。

## 关联

- [[../../01_Project_AGV/Layers/底盘与执行抽象层]]
- [[../ROS系统总览]]
