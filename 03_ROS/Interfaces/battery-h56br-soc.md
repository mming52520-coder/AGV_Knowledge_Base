---
id: "agv:ros:interface:battery-h56br-soc"
type: ros_interface
interface_kind: topic
ros_name: "/battery/h56br/soc"
message_type: "std_msgs/Float32"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/h56br_driver]]", "[[../Packages/trajectory_recorder]]", "[[../Packages/agv_mqtt_bridge]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /battery/h56br/soc

## 作用

电池剩余电量百分比。

## 通信关系

- 生产者/服务端：`h56br_node`
- 消费者/客户端：`trajectory_tracker`、`agv_mqtt_bridge`
- 消息或服务类型：`std_msgs/Float32`

## 证据

- 三号车 `src/h56br_driver/src/h56br_node.cpp:60`
- 三号车 `src/trajectory_recorder/src/trajectory_tracker.cpp:3836-3838`

## 复核说明

低电量策略由轨迹配置和任务逻辑决定。

## 关联 Package

- [[../Packages/h56br_driver]]
- [[../Packages/trajectory_recorder]]
- [[../Packages/agv_mqtt_bridge]]

- [[../ROS接口目录|返回接口目录]]
