---
id: "agv:hardware:dyp-a21-ultrasonic"
type: hardware
status: active
review: generated
project: AGV
source_scope: 三号车当前工作区与工作记忆
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, 硬件]
---

# DYP-A21超声传感器

## 作用

提供前、后、左、右距离与障碍状态。

## 软件映射

- Package：[[../03_ROS/Packages/ultrasonic_controlled_motor]]
- 节点：[[../03_ROS/Nodes/dyp_a21_can_node]]
- 节点：[[../03_ROS/Nodes/single_dyp_a21_can_node]]
- 节点：[[../03_ROS/Nodes/ultrasonic_follower]]
- 接口：[[../03_ROS/Interfaces/ultrasonic-distance]]
- 接口：[[../03_ROS/Interfaces/ultrasonic-status]]

## 证据

- `D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码\src\ultrasonic_controlled_motor\src\dyp_a21_can.cpp:299-345`
- `D:\推料车项目\2.工作记忆/3.硬件调试/超声波调试记忆.md`

## 复核说明

方向、CAN 接口和 Topic 由参数配置，知识库不固化现场端口值。

## 关联

- [[../04_Navigation/超声安全与循墙]]
- [[硬件系统总览]]
