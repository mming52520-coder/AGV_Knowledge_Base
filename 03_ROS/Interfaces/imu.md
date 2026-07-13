---
id: "agv:ros:interface:imu"
type: ros_interface
interface_kind: topic
ros_name: "/imu"
message_type: "sensor_msgs/Imu"
status: active
review: generated
project: AGV
related_packages: ["[[../Packages/wheeltec_base]]", "[[../Packages/trajectory_recorder]]", "[[../Packages/agv_mqtt_bridge]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /imu

## 作用

底盘或 IMU 驱动发布的姿态状态。

## 通信关系

- 生产者/服务端：`wheeltec_robot`
- 消费者/客户端：`trajectory_recorder`、`trajectory_tracker`、`agv_mqtt_bridge`
- 消息或服务类型：`sensor_msgs/Imu`

## 证据

- 三号车 `src/wheeltec_base/src/wheeltec_robot.cpp:301`
- 三号车 `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py:571`

## 复核说明

轨迹系统还可直接读取串口 IMU；运行时来源需结合配置。

## 关联 Package

- [[../Packages/wheeltec_base]]
- [[../Packages/trajectory_recorder]]
- [[../Packages/agv_mqtt_bridge]]

- [[../ROS接口目录|返回接口目录]]
