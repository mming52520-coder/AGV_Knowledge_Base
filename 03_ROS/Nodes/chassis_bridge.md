---
id: "agv:ros:node:chassis_bridge"
type: ros_node
ros_name: "/chassis_bridge"
executable: "chassis_bridge"
status: active
review: verified
project: AGV
vehicles: [二号车, 三号车]
package: "[[../Packages/chassis_controller]]"
parent: "[[../../01_Project_AGV/Layers/底盘与执行抽象层]]"
publishes: ["[[../Interfaces/chassis-state]]"]
subscribes: ["[[../Interfaces/chassis-cmd]]"]
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, chassis_controller]
---

# chassis_bridge

## 职责

把统一底盘命令适配到实际硬件后端，并发布底盘状态。

## 身份

- ROS 默认名：`/chassis_bridge`
- 可执行入口：`chassis_bridge`
- 所属 Package：[[../Packages/chassis_controller]]
- 车辆：二号车、三号车

## 通信接口

- 发布：[[../Interfaces/chassis-state]]
- 订阅：[[../Interfaces/chassis-cmd]]

## Launch

- `src/chassis_controller/launch/chassis_bridge.launch`

## 源码证据

- 三号车 `src/chassis_controller/src/chassis_bridge.cpp:882-944,1265`

## 复核说明

命令和状态 Topic 均可参数化，三号车默认值已由配置和源码交叉确认。

## 关联

- [[../../01_Project_AGV/Layers/底盘与执行抽象层]]
- [[../ROS系统总览]]
