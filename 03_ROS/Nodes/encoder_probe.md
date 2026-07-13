---
id: "agv:ros:node:encoder_probe"
type: ros_node
ros_name: "/encoder_probe"
executable: "encoder_probe"
status: diagnostic
review: verified
project: AGV
vehicles: [三号车]
package: "[[../Packages/trajectory_recorder]]"
parent: "[[../../01_Project_AGV/Layers/传感器与设备驱动层]]"
publishes: ["[[../Interfaces/hardware-probe-topics]]"]
subscribes: []
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, trajectory_recorder]
---

# encoder_probe

## 职责

独立读取编码器原始值和角度。

## 身份

- ROS 默认名：`/encoder_probe`
- 可执行入口：`encoder_probe`
- 所属 Package：[[../Packages/trajectory_recorder]]
- 车辆：三号车

## 通信接口

- 发布：[[../Interfaces/hardware-probe-topics]]

## Launch

- `src/trajectory_recorder/launch/encoder_probe.launch`

## 源码证据

- 三号车 `src/trajectory_recorder/src/encoder_probe_node.cpp:74-110`

## 复核说明

三号车新增诊断节点。

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
