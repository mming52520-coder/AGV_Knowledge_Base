---
id: "agv:ros:interface:odom"
type: ros_interface
interface_kind: topic
ros_name: "/odom"
message_type: "nav_msgs/Odometry"
status: active
review: needs-review
project: AGV
related_packages: ["[[../Packages/wheeltec_base]]", "[[../Packages/encoder]]", "[[../Packages/odometer]]", "[[../Packages/trajectory_recorder]]", "[[../Packages/magnetic_controlled_motor]]", "[[../Packages/agv_mqtt_bridge]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /odom

## 作用

车辆里程与位姿状态。

## 通信关系

- 生产者/服务端：`wheeltec_robot`、`rb100_encoder`、`ackermann_odometry_node`、`trajectory_recorder`、`trajectory_tracker`
- 消费者/客户端：`mag_sensor_reader`、`agv_mqtt_bridge 等`
- 消息或服务类型：`nav_msgs/Odometry`

## 证据

- 三号车 `src/wheeltec_base/src/wheeltec_robot.cpp:300`
- 三号车 `src/encoder/src/rb100_encoder.cpp`
- 三号车 `src/trajectory_recorder/src/trajectory_recorder.cpp:1183`

## 复核说明

静态源码存在多个发布者；实际部署必须确认唯一权威 /odom 或明确融合/重映射。

## 关联 Package

- [[../Packages/wheeltec_base]]
- [[../Packages/encoder]]
- [[../Packages/odometer]]
- [[../Packages/trajectory_recorder]]
- [[../Packages/magnetic_controlled_motor]]
- [[../Packages/agv_mqtt_bridge]]

- [[../ROS接口目录|返回接口目录]]
