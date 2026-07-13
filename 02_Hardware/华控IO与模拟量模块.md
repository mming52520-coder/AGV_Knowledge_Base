---
id: "agv:hardware:huakong-io-analog"
type: hardware
status: active
review: generated
project: AGV
source_scope: 三号车当前工作区与工作记忆
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, 硬件]
---

# 华控IO与模拟量模块

## 作用

提供模拟量驱动、数字 IO 与继电器控制。

## 软件映射

- Package：[[../03_ROS/Packages/chassis_controller]]
- Package：[[../03_ROS/Packages/analog_controlled_motor]]
- Package：[[../03_ROS/Packages/relay]]
- 节点：[[../03_ROS/Nodes/chassis_bridge]]
- 节点：[[../03_ROS/Nodes/hk_dio_controller]]
- 节点：[[../03_ROS/Nodes/hk_dio_remote]]
- 接口：[[../03_ROS/Interfaces/chassis-cmd]]
- 接口：[[../03_ROS/Interfaces/chassis-state]]
- 接口：[[../03_ROS/Interfaces/relay-io-status]]
- 接口：[[../03_ROS/Interfaces/motor-brake]]

## 证据

- `D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码\src\chassis_controller\src\chassis_bridge.cpp`
- `D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码\src\relay\src\hk_dio.cpp`
- `D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码\src\analog_controlled_motor\package.xml`

## 复核说明

三号车 analog_controlled_motor 当前只剩包壳；华控模拟量是否由 chassis_controller 后端使用需按配置确认。

## 关联

- [[../05_Control/控制架构总览]]
- [[硬件系统总览]]
