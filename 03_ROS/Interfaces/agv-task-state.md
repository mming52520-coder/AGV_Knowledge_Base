---
id: "agv:ros:interface:agv-task-state"
type: ros_interface
interface_kind: topic
ros_name: "/agv/task_state"
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

# /agv/task_state

## 作用

整车任务状态。

## 通信关系

- 生产者/服务端：`trajectory_tracker`
- 消费者/客户端：`agv_mqtt_bridge`、`后端状态展示`
- 消息或服务类型：`std_msgs/String`

## 证据

- 三号车 `src/trajectory_recorder/src/trajectory_tracker.cpp:3907`

## 复核说明

属于 ROS 与后端任务语义的边界接口。

## 关联 Package

- [[../Packages/trajectory_recorder]]
- [[../Packages/agv_mqtt_bridge]]

- [[../ROS接口目录|返回接口目录]]
