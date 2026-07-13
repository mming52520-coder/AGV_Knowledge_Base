---
id: "agv:ros:interface:motor-speed"
type: ros_interface
interface_kind: topic
ros_name: "/motor_speed"
message_type: "std_msgs/Float32"
status: compatibility
review: verified
project: AGV
related_packages: ["[[../Packages/magnetic_controlled_motor]]", "[[../Packages/ultrasonic_controlled_motor]]", "[[../Packages/trajectory_recorder]]", "[[../Packages/remote_ctrl]]", "[[../Packages/wheeltec_base]]", "[[../Packages/analog_controlled_motor]]", "[[../Packages/relay]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /motor_speed

## 作用

旧控制链的驱动速度指令。

## 通信关系

- 生产者/服务端：`magnetic_follower`、`ultrasonic_follower`、`trajectory_tracker`、`remote_controller（一/二号车）`
- 消费者/客户端：`cmd_vel_adapter`、`analog_controlled_motor`、`relay`、`trajectory_recorder`
- 消息或服务类型：`std_msgs/Float32`

## 证据

- 三号车 `src/magnetic_controlled_motor/src/magnetic_follower.cpp:57`
- 三号车 `src/trajectory_recorder/src/trajectory_tracker.cpp:3887`
- 三号车 `src/wheeltec_base/src/cmd_vel_adapter.cpp:49`

## 复核说明

存在多个潜在发布者，运行时必须由模式或仲裁保证单一有效控制源。

## 关联 Package

- [[../Packages/magnetic_controlled_motor]]
- [[../Packages/ultrasonic_controlled_motor]]
- [[../Packages/trajectory_recorder]]
- [[../Packages/remote_ctrl]]
- [[../Packages/wheeltec_base]]
- [[../Packages/analog_controlled_motor]]
- [[../Packages/relay]]

- [[../ROS接口目录|返回接口目录]]
