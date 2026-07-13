---
id: "agv:ros:node:magnetic_follower"
type: ros_node
ros_name: "/mag_line_follower"
executable: "magnetic_follower"
status: active
review: verified
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/magnetic_controlled_motor]]"
parent: "[[../../01_Project_AGV/Layers/导航决策与安全层]]"
publishes: ["[[../Interfaces/motor-command]]", "[[../Interfaces/motor-speed]]", "[[../Interfaces/mag-line-position]]"]
subscribes: ["[[../Interfaces/mag-sensor-raw-data]]"]
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, magnetic_controlled_motor]
---

# magnetic_follower

## 职责

从原始磁位图估计磁线位置并产生旧链路控制建议。

## 身份

- ROS 默认名：`/mag_line_follower`
- 可执行入口：`magnetic_follower`
- 所属 Package：[[../Packages/magnetic_controlled_motor]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/motor-command]]
- 发布：[[../Interfaces/motor-speed]]
- 发布：[[../Interfaces/mag-line-position]]
- 订阅：[[../Interfaces/mag-sensor-raw-data]]

## Launch

- `src/bringup/launch/all_nodes.launch`
- `src/magnetic_controlled_motor/launch/magnetic_nodes.launch`

## 源码证据

- 三号车 `src/magnetic_controlled_motor/src/magnetic_follower.cpp:53-58,236`

## 复核说明

源码默认 ROS 名为 mag_line_follower；与轨迹跟踪同时运行时要明确控制权。

## 关联

- [[../../01_Project_AGV/Layers/导航决策与安全层]]
- [[../ROS系统总览]]
