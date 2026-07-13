---
id: "agv:ros:node:yz_aim_probe"
type: ros_node
ros_name: "/yz_aim_probe"
executable: "yz_aim_probe"
status: diagnostic
review: verified
project: AGV
vehicles: [三号车]
package: "[[../Packages/trajectory_recorder]]"
parent: "[[../../01_Project_AGV/Layers/传感器与设备驱动层]]"
publishes: ["[[../Interfaces/hardware-probe-topics]]"]
subscribes: ["[[../Interfaces/hardware-probe-topics]]"]
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, trajectory_recorder]
---

# yz_aim_probe

## 职责

独立调试 YZ_AIM 转向伺服，发布位置、速度与告警状态。

## 身份

- ROS 默认名：`/yz_aim_probe`
- 可执行入口：`yz_aim_probe`
- 所属 Package：[[../Packages/trajectory_recorder]]
- 车辆：三号车

## 通信接口

- 发布：[[../Interfaces/hardware-probe-topics]]
- 订阅：[[../Interfaces/hardware-probe-topics]]

## Launch

- `src/trajectory_recorder/launch/yz_aim_probe.launch`

## 源码证据

- 三号车 `src/trajectory_recorder/src/yz_aim_probe_node.cpp:41-49,77,231`

## 复核说明

私有命名空间 Topic 仅供调试。

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
