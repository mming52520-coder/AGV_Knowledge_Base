---
id: "agv:ros:interface:mag-sensor-frame"
type: ros_interface
interface_kind: topic
ros_name: "/mag_sensor/frame"
message_type: "magnetic_controlled_motor/MagFrame"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/magnetic_controlled_motor]]", "[[../Packages/trajectory_recorder]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /mag_sensor/frame

## 作用

带时间和里程语义的磁传感帧。

## 通信关系

- 生产者/服务端：`mag_sensor_reader`
- 消费者/客户端：`trajectory_recorder`
- 消息或服务类型：`magnetic_controlled_motor/MagFrame`

## 证据

- 三号车 `src/magnetic_controlled_motor/src/mag_sensor_reader.cpp:71`
- 三号车 `src/trajectory_recorder/src/trajectory_recorder.cpp:1157`

## 复核说明

用于轨迹数据记录与后续导航分析。

## 关联 Package

- [[../Packages/magnetic_controlled_motor]]
- [[../Packages/trajectory_recorder]]

- [[../ROS接口目录|返回接口目录]]
