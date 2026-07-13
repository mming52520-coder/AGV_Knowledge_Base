---
id: "agv:ros:interface:chassis-cmd"
type: ros_interface
interface_kind: topic
ros_name: "/chassis/cmd"
message_type: "chassis_controller/ChassisCommand"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/trajectory_recorder]]", "[[../Packages/remote_ctrl]]", "[[../Packages/chassis_controller]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /chassis/cmd

## 作用

三号车结构化底盘控制意图。

## 通信关系

- 生产者/服务端：`trajectory_tracker`、`remote_controller`
- 消费者/客户端：`chassis_bridge`
- 消息或服务类型：`chassis_controller/ChassisCommand`

## 证据

- 三号车 `src/trajectory_recorder/src/trajectory_tracker.cpp:3354,3873-3895`
- 三号车 `src/remote_ctrl/src/remote_controller.cpp:53,83,194`
- 三号车 `src/chassis_controller/config/chassis_controller.yaml:8`

## 复核说明

默认名由参数配置，三处源码默认值一致。

## 关联 Package

- [[../Packages/trajectory_recorder]]
- [[../Packages/remote_ctrl]]
- [[../Packages/chassis_controller]]

- [[../ROS接口目录|返回接口目录]]
