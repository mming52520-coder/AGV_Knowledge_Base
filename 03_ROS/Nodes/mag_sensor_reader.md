---
id: "agv:ros:node:mag_sensor_reader"
type: ros_node
ros_name: "/ms16a_mag_sensor_node"
executable: "mag_sensor_reader"
status: active
review: verified
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/magnetic_controlled_motor]]"
parent: "[[../../01_Project_AGV/Layers/传感器与设备驱动层]]"
publishes: ["[[../Interfaces/mag-sensor-raw-data]]", "[[../Interfaces/mag-sensor-frame]]", "[[../Interfaces/mag-sensor-nail-event]]"]
subscribes: ["[[../Interfaces/odom]]"]
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, magnetic_controlled_motor]
---

# mag_sensor_reader

## 职责

读取 MS16A 磁传感器，构造磁帧并识别磁钉事件。

## 身份

- ROS 默认名：`/ms16a_mag_sensor_node`
- 可执行入口：`mag_sensor_reader`
- 所属 Package：[[../Packages/magnetic_controlled_motor]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/mag-sensor-raw-data]]
- 发布：[[../Interfaces/mag-sensor-frame]]
- 发布：[[../Interfaces/mag-sensor-nail-event]]
- 订阅：[[../Interfaces/odom]]

## Launch

- `src/bringup/launch/all_nodes.launch`
- `src/magnetic_controlled_motor/launch/magnetic_nodes.launch`

## 源码证据

- 三号车 `src/magnetic_controlled_motor/src/mag_sensor_reader.cpp:70-73,564`

## 复核说明

Launch 名为 mag_sensor_reader，源码默认 ROS 名为 ms16a_mag_sensor_node。

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
