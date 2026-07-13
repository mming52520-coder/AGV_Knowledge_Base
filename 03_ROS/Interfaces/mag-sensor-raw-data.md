---
id: "agv:ros:interface:mag-sensor-raw-data"
type: ros_interface
interface_kind: topic
ros_name: "/mag_sensor/raw_data"
message_type: "std_msgs/UInt16"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/magnetic_controlled_motor]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /mag_sensor/raw_data

## 作用

MS16A 原始磁传感器位图。

## 通信关系

- 生产者/服务端：`mag_sensor_reader`
- 消费者/客户端：`magnetic_follower`
- 消息或服务类型：`std_msgs/UInt16`

## 证据

- 三号车 `src/magnetic_controlled_motor/src/mag_sensor_reader.cpp:70`
- 三号车 `src/magnetic_controlled_motor/src/magnetic_follower.cpp:53`

## 复核说明

原始位图用于磁线位置估计。

## 关联 Package

- [[../Packages/magnetic_controlled_motor]]

- [[../ROS接口目录|返回接口目录]]
