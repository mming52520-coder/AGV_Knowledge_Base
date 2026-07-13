---
id: "agv:ros:interface:mag-line-position"
type: ros_interface
interface_kind: topic
ros_name: "/mag_line_position"
message_type: "std_msgs/Float32"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/magnetic_controlled_motor]]", "[[../Packages/trajectory_recorder]]", "[[../Packages/agv_mqtt_bridge]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /mag_line_position

## 作用

磁线横向位置或偏差估计。

## 通信关系

- 生产者/服务端：`magnetic_follower`
- 消费者/客户端：`导航/状态消费者`
- 消息或服务类型：`std_msgs/Float32`

## 证据

- 三号车 `src/magnetic_controlled_motor/src/magnetic_follower.cpp:58`

## 复核说明

具体单位和正负方向需要从算法实现及现场标定确认。

## 关联 Package

- [[../Packages/magnetic_controlled_motor]]
- [[../Packages/trajectory_recorder]]
- [[../Packages/agv_mqtt_bridge]]

- [[../ROS接口目录|返回接口目录]]
