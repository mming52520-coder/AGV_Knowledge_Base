---
id: "agv:hardware:ms16a-magnetic-sensor"
type: hardware
status: active
review: generated
project: AGV
source_scope: 三号车当前工作区与工作记忆
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, 硬件]
---

# MS16A磁传感器

## 作用

检测磁条位置并支持磁钉事件识别。

## 软件映射

- Package：[[../03_ROS/Packages/magnetic_controlled_motor]]
- 节点：[[../03_ROS/Nodes/mag_sensor_reader]]
- 节点：[[../03_ROS/Nodes/magnetic_follower]]
- 接口：[[../03_ROS/Interfaces/mag-sensor-raw-data]]
- 接口：[[../03_ROS/Interfaces/mag-sensor-frame]]
- 接口：[[../03_ROS/Interfaces/mag-sensor-nail-event]]
- 接口：[[../03_ROS/Interfaces/mag-line-position]]

## 证据

- `D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码\src\magnetic_controlled_motor\src\mag_sensor_reader.cpp:70-73,564`
- `D:\推料车项目\2.工作记忆/3.硬件调试/磁导航调试记忆.md`

## 复核说明

型号与协议细节应以已确认的 MS16A/MGS-16FP 手册和现场接线为准。

## 关联

- [[../04_Navigation/磁导航与磁钉]]
- [[硬件系统总览]]
