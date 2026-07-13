---
id: "agv:ros:node:imu_probe"
type: ros_node
ros_name: "/imu_probe"
executable: "imu_probe"
status: diagnostic
review: verified
project: AGV
vehicles: [一号车, 二号车, 三号车]
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

# imu_probe

## 职责

独立读取 IMU 并发布诊断数据与欧拉角。

## 身份

- ROS 默认名：`/imu_probe`
- 可执行入口：`imu_probe`
- 所属 Package：[[../Packages/trajectory_recorder]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/hardware-probe-topics]]

## Launch

- `src/trajectory_recorder/launch/imu_probe.launch`

## 源码证据

- 三号车 `src/trajectory_recorder/src/imu_probe_node.cpp:52-108`

## 复核说明

诊断节点，不代表生产链的 /imu 权威来源。

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
