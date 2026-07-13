---
id: "agv:ros:node:ultrasonic_follower"
type: ros_node
ros_name: "/ultrasonic_follower"
executable: "ultrasonic_follower"
status: active
review: verified
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/ultrasonic_controlled_motor]]"
parent: "[[../../01_Project_AGV/Layers/导航决策与安全层]]"
publishes: ["[[../Interfaces/motor-command]]", "[[../Interfaces/motor-speed]]"]
subscribes: ["[[../Interfaces/ultrasonic-distance]]"]
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, ultrasonic_controlled_motor]
---

# ultrasonic_follower

## 职责

根据左右超声距离产生循墙或避障控制建议。

## 身份

- ROS 默认名：`/ultrasonic_follower`
- 可执行入口：`ultrasonic_follower`
- 所属 Package：[[../Packages/ultrasonic_controlled_motor]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/motor-command]]
- 发布：[[../Interfaces/motor-speed]]
- 订阅：[[../Interfaces/ultrasonic-distance]]

## Launch

- `src/bringup/launch/all_nodes.launch`
- `src/ultrasonic_controlled_motor/launch/ultrasonic_nodes.launch`

## 源码证据

- 三号车 `src/ultrasonic_controlled_motor/src/ultrasonic_follower.cpp:54-60,160`

## 复核说明

直接发布旧控制 Topic，必须纳入模式/控制权管理。

## 关联

- [[../../01_Project_AGV/Layers/导航决策与安全层]]
- [[../ROS系统总览]]
