---
id: "agv:ros:node:h56br_node"
type: ros_node
ros_name: "/h56br_node"
executable: "h56br_node"
status: active
review: verified
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/h56br_driver]]"
parent: "[[../../01_Project_AGV/Layers/传感器与设备驱动层]]"
publishes: ["[[../Interfaces/battery-h56br-status]]", "[[../Interfaces/battery-h56br-soc]]"]
subscribes: []
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, h56br_driver]
---

# h56br_node

## 职责

读取 H56BR 电池表，发布状态并提供配置/标定服务。

## 身份

- ROS 默认名：`/h56br_node`
- 可执行入口：`h56br_node`
- 所属 Package：[[../Packages/h56br_driver]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/battery-h56br-status]]
- 发布：[[../Interfaces/battery-h56br-soc]]

## Launch

- `src/h56br_driver/launch/h56br.launch`

## 源码证据

- 三号车 `src/h56br_driver/src/h56br_node.cpp:57-77,298`

## 复核说明

其他电压和电流 Topic 记录在 Package 页面与源码中。

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
