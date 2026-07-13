---
id: "agv:hardware:stm32-chassis"
type: hardware
status: active
review: generated
project: AGV
source_scope: 三号车当前工作区与工作记忆
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, 硬件]
---

# STM32底盘控制器

## 作用

通过串口协议接收 Twist 并反馈里程、IMU 与电压。

## 软件映射

- Package：[[../03_ROS/Packages/wheeltec_base]]
- 节点：[[../03_ROS/Nodes/wheeltec_robot_node]]
- 节点：[[../03_ROS/Nodes/cmd_vel_adapter]]
- 接口：[[../03_ROS/Interfaces/cmd-vel]]
- 接口：[[../03_ROS/Interfaces/odom]]
- 接口：[[../03_ROS/Interfaces/imu]]

## 证据

- `D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码\src\wheeltec_base\src\wheeltec_robot.cpp:299-302`
- `D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码\src\wheeltec_base\src\cmd_vel_adapter.cpp:46-50`

## 复核说明

主要对应一号车兼容链；三号车默认采用新底盘桥接。

## 关联

- [[../05_Control/控制架构总览]]
- [[硬件系统总览]]
