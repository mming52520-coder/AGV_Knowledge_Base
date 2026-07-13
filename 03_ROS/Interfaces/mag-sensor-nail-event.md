---
id: "agv:ros:interface:mag-sensor-nail-event"
type: ros_interface
interface_kind: topic
ros_name: "/mag_sensor/nail_event"
message_type: "magnetic_controlled_motor/MagNailEvent"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/magnetic_controlled_motor]]", "[[../Packages/trajectory_recorder]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /mag_sensor/nail_event

## 作用

磁钉检测事件。

## 通信关系

- 生产者/服务端：`mag_sensor_reader`
- 消费者/客户端：`trajectory_recorder`、`trajectory_tracker`
- 消息或服务类型：`magnetic_controlled_motor/MagNailEvent`

## 证据

- 三号车 `src/magnetic_controlled_motor/src/mag_sensor_reader.cpp:72`
- 三号车 `src/trajectory_recorder/src/trajectory_recorder.cpp:1159`

## 复核说明

磁钉识别阈值和事件确认需结合磁导航配置。

## 关联 Package

- [[../Packages/magnetic_controlled_motor]]
- [[../Packages/trajectory_recorder]]

- [[../ROS接口目录|返回接口目录]]
