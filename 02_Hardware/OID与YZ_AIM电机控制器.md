---
id: "agv:hardware:oid-yz-aim-motor-controller"
type: hardware
status: active
review: generated
project: AGV
source_scope: 三号车当前工作区与工作记忆
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, 硬件]
---

# OID与YZ_AIM电机控制器

## 作用

承担驱动或转向电机的闭环控制与反馈。

## 软件映射

- Package：[[../03_ROS/Packages/chassis_controller]]
- Package：[[../03_ROS/Packages/trajectory_recorder]]
- 节点：[[../03_ROS/Nodes/chassis_bridge]]
- 节点：[[../03_ROS/Nodes/steering_remote]]
- 节点：[[../03_ROS/Nodes/yz_aim_probe]]
- 接口：[[../03_ROS/Interfaces/chassis-cmd]]
- 接口：[[../03_ROS/Interfaces/chassis-state]]
- 接口：[[../03_ROS/Interfaces/motor-command]]
- 接口：[[../03_ROS/Interfaces/motor-services]]
- 接口：[[../03_ROS/Interfaces/hardware-probe-topics]]

## 证据

- `D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码\src\chassis_controller\src\chassis_bridge.cpp:882-944`
- `D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码\src\trajectory_recorder\src\steering_remote.cpp:38-62`
- `D:\推料车项目\2.工作记忆/3.硬件调试/OID电机控制器/2026-05-19_电机控制器闭环反馈接入工作记忆.md`

## 复核说明

协议、站号和串口值不写入知识图谱；现场配置仍以部署文件为准。

## 关联

- [[../05_Control/控制架构总览]]
- [[硬件系统总览]]
