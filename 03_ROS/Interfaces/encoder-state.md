---
id: "agv:ros:interface:encoder-state"
type: ros_interface
interface_kind: topic_group
ros_name: "/encoder_angle + encoder_twist"
message_type: "std_msgs/Float32; geometry_msgs/TwistStamped/相关类型"
status: active
review: needs-review
project: AGV
related_packages: ["[[../Packages/encoder]]", "[[../Packages/odometer]]", "[[../Packages/trajectory_recorder]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /encoder_angle + encoder_twist

## 作用

编码器角度与运动状态。

## 通信关系

- 生产者/服务端：`rb100_encoder`、`ackermann_odometry_node`、`trajectory_recorder`
- 消费者/客户端：`轨迹与状态消费者`
- 消息或服务类型：`std_msgs/Float32; geometry_msgs/TwistStamped/相关类型`

## 证据

- 三号车 `src/encoder/src/rb100_encoder.cpp`
- 三号车 `src/odometer/src/odometer.cpp`
- 三号车 `src/trajectory_recorder/src/trajectory_recorder.cpp:1191`

## 复核说明

不同实现的消息类型和命名空间需运行时复核。

## 关联 Package

- [[../Packages/encoder]]
- [[../Packages/odometer]]
- [[../Packages/trajectory_recorder]]

- [[../ROS接口目录|返回接口目录]]
