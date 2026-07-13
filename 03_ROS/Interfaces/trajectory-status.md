---
id: "agv:ros:interface:trajectory-status"
type: ros_interface
interface_kind: topic
ros_name: "/trajectory_status"
message_type: "std_msgs/String"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/trajectory_recorder]]", "[[../Packages/agv_mqtt_bridge]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /trajectory_status

## 作用

轨迹跟踪状态反馈。

## 通信关系

- 生产者/服务端：`trajectory_tracker`
- 消费者/客户端：`agv_mqtt_bridge`、`状态展示`
- 消息或服务类型：`std_msgs/String`

## 证据

- 三号车 `src/trajectory_recorder/src/trajectory_tracker.cpp:3906`

## 复核说明

字符串值域需要和后端协议保持一致。

## 关联 Package

- [[../Packages/trajectory_recorder]]
- [[../Packages/agv_mqtt_bridge]]

- [[../ROS接口目录|返回接口目录]]
