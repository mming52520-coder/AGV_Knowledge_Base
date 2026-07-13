---
id: "agv:ros:node:trajectory_tracker"
type: ros_node
ros_name: "/trajectory_tracker"
executable: "trajectory_tracker"
status: active
review: needs-review
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/trajectory_recorder]]"
parent: "[[../../01_Project_AGV/Layers/任务与应用编排层]]"
publishes: ["[[../Interfaces/chassis-cmd]]", "[[../Interfaces/motor-command]]", "[[../Interfaces/motor-speed]]", "[[../Interfaces/odom]]", "[[../Interfaces/trajectory-status]]", "[[../Interfaces/agv-task-state]]"]
subscribes: ["[[../Interfaces/battery-h56br-soc]]", "[[../Interfaces/ultrasonic-distance]]", "[[../Interfaces/ultrasonic-status]]", "[[../Interfaces/drive-feedback]]"]
provides_services: ["[[../Interfaces/trajectory-services]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, trajectory_recorder]
---

# trajectory_tracker

## 职责

读取轨迹并执行跟踪，融合超声、磁导航、电量、里程和底盘反馈。

## 身份

- ROS 默认名：`/trajectory_tracker`
- 可执行入口：`trajectory_tracker`
- 所属 Package：[[../Packages/trajectory_recorder]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/chassis-cmd]]
- 发布：[[../Interfaces/motor-command]]
- 发布：[[../Interfaces/motor-speed]]
- 发布：[[../Interfaces/odom]]
- 发布：[[../Interfaces/trajectory-status]]
- 发布：[[../Interfaces/agv-task-state]]
- 订阅：[[../Interfaces/battery-h56br-soc]]
- 订阅：[[../Interfaces/ultrasonic-distance]]
- 订阅：[[../Interfaces/ultrasonic-status]]
- 订阅：[[../Interfaces/drive-feedback]]
- 提供服务：[[../Interfaces/trajectory-services]]

## Launch

- `src/trajectory_recorder/launch/tracker.launch`
- `src/trajectory_recorder/launch/robot_full.launch`

## 源码证据

- 三号车 `src/trajectory_recorder/src/trajectory_tracker.cpp:3836-3959,4569`

## 复核说明

该节点同时支持旧控制 Topic 和新 /chassis/cmd；运行输出模式与 /odom 发布策略必须结合配置复核。

## 关联

- [[../../01_Project_AGV/Layers/任务与应用编排层]]
- [[../ROS系统总览]]
