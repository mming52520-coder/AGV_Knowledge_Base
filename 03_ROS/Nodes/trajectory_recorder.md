---
id: "agv:ros:node:trajectory_recorder"
type: ros_node
ros_name: "/trajectory_recorder"
executable: "trajectory_recorder"
status: active
review: verified
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/trajectory_recorder]]"
parent: "[[../../01_Project_AGV/Layers/任务与应用编排层]]"
publishes: ["[[../Interfaces/odom]]", "[[../Interfaces/encoder-state]]"]
subscribes: ["[[../Interfaces/motor-speed]]", "[[../Interfaces/motor-command]]", "[[../Interfaces/mag-sensor-frame]]", "[[../Interfaces/mag-sensor-nail-event]]", "[[../Interfaces/ultrasonic-distance]]", "[[../Interfaces/drive-feedback]]"]
provides_services: ["[[../Interfaces/trajectory-services]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, trajectory_recorder]
---

# trajectory_recorder

## 职责

记录速度、转向、磁钉、超声、里程和姿态等轨迹数据。

## 身份

- ROS 默认名：`/trajectory_recorder`
- 可执行入口：`trajectory_recorder`
- 所属 Package：[[../Packages/trajectory_recorder]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/odom]]
- 发布：[[../Interfaces/encoder-state]]
- 订阅：[[../Interfaces/motor-speed]]
- 订阅：[[../Interfaces/motor-command]]
- 订阅：[[../Interfaces/mag-sensor-frame]]
- 订阅：[[../Interfaces/mag-sensor-nail-event]]
- 订阅：[[../Interfaces/ultrasonic-distance]]
- 订阅：[[../Interfaces/drive-feedback]]
- 提供服务：[[../Interfaces/trajectory-services]]

## Launch

- `src/trajectory_recorder/launch/recorder.launch`

## 源码证据

- 三号车 `src/trajectory_recorder/src/trajectory_recorder.cpp:1153-1202,1602`

## 复核说明

三号车可使用 drive_feedback_odom；原始轨迹 YAML 不逐文件进入图谱。

## 关联

- [[../../01_Project_AGV/Layers/任务与应用编排层]]
- [[../ROS系统总览]]
