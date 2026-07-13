---
id: "agv:ros:interface:chassis-state"
type: ros_interface
interface_kind: topic
ros_name: "/chassis/state"
message_type: "chassis_controller/ChassisState"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/chassis_controller]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /chassis/state

## 作用

底盘桥接层发布的执行与反馈状态。

## 通信关系

- 生产者/服务端：`chassis_bridge`
- 消费者/客户端：`drive_feedback_odom`
- 消息或服务类型：`chassis_controller/ChassisState`

## 证据

- 三号车 `src/chassis_controller/src/chassis_bridge.cpp:883,932`
- 三号车 `src/chassis_controller/src/drive_feedback_odom.cpp:18,57`
- 三号车 `src/chassis_controller/config/chassis_controller.yaml:9`

## 复核说明

用于驱动反馈里程计和上层状态观测。

## 关联 Package

- [[../Packages/chassis_controller]]

- [[../ROS接口目录|返回接口目录]]
