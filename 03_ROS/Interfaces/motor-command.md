---
id: "agv:ros:interface:motor-command"
type: ros_interface
interface_kind: topic
ros_name: "/motor_command"
message_type: "std_msgs/String"
status: compatibility
review: verified
project: AGV
related_packages: ["[[../Packages/magnetic_controlled_motor]]", "[[../Packages/ultrasonic_controlled_motor]]", "[[../Packages/trajectory_recorder]]", "[[../Packages/remote_ctrl]]", "[[../Packages/wheeltec_base]]", "[[../Packages/agv_mqtt_bridge]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /motor_command

## 作用

旧控制链的转向/动作命令。

## 通信关系

- 生产者/服务端：`magnetic_follower`、`ultrasonic_follower`、`trajectory_tracker`、`remote_controller`
- 消费者/客户端：`steering_remote`、`cmd_vel_adapter`、`trajectory_recorder`、`旧 motor_control`、`agv_mqtt_bridge`
- 消息或服务类型：`std_msgs/String`

## 证据

- 三号车 `src/magnetic_controlled_motor/src/magnetic_follower.cpp:56`
- 三号车 `src/trajectory_recorder/src/steering_remote.cpp:38`
- 三号车 `src/wheeltec_base/src/cmd_vel_adapter.cpp:48`
- 三号车 `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py:588-590`

## 复核说明

字符串协议需要结合当前命令约定文档复核。

## 关联 Package

- [[../Packages/magnetic_controlled_motor]]
- [[../Packages/ultrasonic_controlled_motor]]
- [[../Packages/trajectory_recorder]]
- [[../Packages/remote_ctrl]]
- [[../Packages/wheeltec_base]]
- [[../Packages/agv_mqtt_bridge]]

- [[../ROS接口目录|返回接口目录]]
