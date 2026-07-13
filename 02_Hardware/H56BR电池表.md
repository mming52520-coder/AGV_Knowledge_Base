---
id: "agv:hardware:h56br-battery-meter"
type: hardware
status: active
review: generated
project: AGV
source_scope: 三号车当前工作区与工作记忆
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, 硬件]
---

# H56BR电池表

## 作用

测量电压、电流、SOC 并支持电量参数标定。

## 软件映射

- Package：[[../03_ROS/Packages/h56br_driver]]
- 节点：[[../03_ROS/Nodes/h56br_node]]
- 接口：[[../03_ROS/Interfaces/battery-h56br-status]]
- 接口：[[../03_ROS/Interfaces/battery-h56br-soc]]

## 证据

- `D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码\src\h56br_driver\src\h56br_node.cpp:57-77,298`
- `D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码\src\h56br_driver\README.md`

## 复核说明

当前实现取代已归档的 battery_management。

## 关联

- [[../04_Navigation/轨迹记录与跟踪]]
- [[硬件系统总览]]
