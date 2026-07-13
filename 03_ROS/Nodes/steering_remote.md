---
id: "agv:ros:node:steering_remote"
type: ros_node
ros_name: "/steering_remote"
executable: "steering_remote"
status: active
review: verified
project: AGV
vehicles: [二号车, 三号车]
package: "[[../Packages/trajectory_recorder]]"
parent: "[[../../01_Project_AGV/Layers/底盘与执行抽象层]]"
publishes: []
subscribes: ["[[../Interfaces/motor-command]]"]
provides_services: ["[[../Interfaces/motor-services]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, trajectory_recorder]
---

# steering_remote

## 职责

把转向命令发送到 YZ_AIM 等转向后端，并提供初始化和使能服务。

## 身份

- ROS 默认名：`/steering_remote`
- 可执行入口：`steering_remote`
- 所属 Package：[[../Packages/trajectory_recorder]]
- 车辆：二号车、三号车

## 通信接口

- 订阅：[[../Interfaces/motor-command]]
- 提供服务：[[../Interfaces/motor-services]]

## Launch

- `src/bringup/launch/all_nodes.launch`（三号车）
- `src/remote_ctrl/launch/steering_motor_only.launch`
- `src/remote_ctrl/launch/steering_only.launch`

## 源码证据

- 三号车 `src/trajectory_recorder/src/steering_remote.cpp:38-62,227-275`

## 复核说明

三号车 Bringup 默认启动；一号车使用旧 motor_control。

## 关联

- [[../../01_Project_AGV/Layers/底盘与执行抽象层]]
- [[../ROS系统总览]]
