---
id: "agv:hardware:serial-can-rs485"
type: hardware
status: active
review: generated
project: AGV
source_scope: 三号车当前工作区与工作记忆
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, 硬件]
---

# 串口CAN与RS485总线

## 作用

连接底盘、磁传感器、超声、电池表、电机控制器和 IO 模块。

## 软件映射

- Package：[[../03_ROS/Packages/wheeltec_base]]
- Package：[[../03_ROS/Packages/magnetic_controlled_motor]]
- Package：[[../03_ROS/Packages/ultrasonic_controlled_motor]]
- Package：[[../03_ROS/Packages/h56br_driver]]
- Package：[[../03_ROS/Packages/chassis_controller]]
- Package：[[../03_ROS/Packages/relay]]
- 节点：[[../03_ROS/Nodes/wheeltec_robot_node]]
- 节点：[[../03_ROS/Nodes/mag_sensor_reader]]
- 节点：[[../03_ROS/Nodes/dyp_a21_can_node]]
- 节点：[[../03_ROS/Nodes/h56br_node]]
- 节点：[[../03_ROS/Nodes/chassis_bridge]]
- 节点：[[../03_ROS/Nodes/steering_remote]]

## 证据

- `D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码\src\wheeltec_base\src\wheeltec_robot.cpp`
- `D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码\src\ultrasonic_controlled_motor\src\dyp_a21_can.cpp`
- `D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码\src\h56br_driver\src\h56br_node.cpp`

## 复核说明

知识图谱只记录总线角色，不保存现场设备地址、密码或远程连接信息。

## 关联

- [[../01_Project_AGV/Layers/物理硬件层]]
- [[硬件系统总览]]
