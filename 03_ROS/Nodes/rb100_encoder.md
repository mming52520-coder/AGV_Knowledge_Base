---
id: "agv:ros:node:rb100_encoder"
type: ros_node
ros_name: "/rb100_odometry_node"
executable: "rb100_encoder"
status: available
review: generated
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/encoder]]"
parent: "[[../../01_Project_AGV/Layers/传感器与设备驱动层]]"
publishes: ["[[../Interfaces/odom]]", "[[../Interfaces/encoder-state]]"]
subscribes: []
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, encoder]
---

# rb100_encoder

## 职责

读取 RB100/相关编码器并发布角度、Twist 与里程。

## 身份

- ROS 默认名：`/rb100_odometry_node`
- 可执行入口：`rb100_encoder`
- 所属 Package：[[../Packages/encoder]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/odom]]
- 发布：[[../Interfaces/encoder-state]]

## Launch

- 当前默认 Launch 中未发现直接启动项。

## 源码证据

- 三号车 `src/encoder/src/rb100_encoder.cpp:470`

## 复核说明

三车代码一致；当前默认 Launch 中未发现直接启动项。

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
