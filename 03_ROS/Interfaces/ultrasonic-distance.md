---
id: "agv:ros:interface:ultrasonic-distance"
type: ros_interface
interface_kind: topic_group
ros_name: "/ultrasonic/*_distance"
message_type: "std_msgs/Float32"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/ultrasonic_controlled_motor]]", "[[../Packages/trajectory_recorder]]", "[[../Packages/agv_mqtt_bridge]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /ultrasonic/*_distance

## 作用

前、后、左、右超声距离 Topic 组。

## 通信关系

- 生产者/服务端：`dyp_a21_can_node`
- 消费者/客户端：`ultrasonic_follower`、`trajectory_recorder`、`trajectory_tracker`、`agv_mqtt_bridge`
- 消息或服务类型：`std_msgs/Float32`

## 证据

- 三号车 `src/ultrasonic_controlled_motor/src/dyp_a21_can.cpp:299,327-345`
- 三号车 `src/ultrasonic_controlled_motor/src/ultrasonic_follower.cpp:54-56`

## 复核说明

具体 Topic 由 sensor_side 和参数决定。

## 关联 Package

- [[../Packages/ultrasonic_controlled_motor]]
- [[../Packages/trajectory_recorder]]
- [[../Packages/agv_mqtt_bridge]]

- [[../ROS接口目录|返回接口目录]]
