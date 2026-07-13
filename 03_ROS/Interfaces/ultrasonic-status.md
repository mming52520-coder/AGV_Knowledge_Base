---
id: "agv:ros:interface:ultrasonic-status"
type: ros_interface
interface_kind: topic_group
ros_name: "/ultrasonic/*_status"
message_type: "ultrasonic_controlled_motor/UltrasonicStatus"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/ultrasonic_controlled_motor]]", "[[../Packages/remote_ctrl]]", "[[../Packages/trajectory_recorder]]", "[[../Packages/agv_mqtt_bridge]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /ultrasonic/*_status

## 作用

多方向超声状态与安全等级 Topic 组。

## 通信关系

- 生产者/服务端：`dyp_a21_can_node`
- 消费者/客户端：`remote_controller`、`trajectory_tracker`、`agv_mqtt_bridge`
- 消息或服务类型：`ultrasonic_controlled_motor/UltrasonicStatus`

## 证据

- 三号车 `src/ultrasonic_controlled_motor/src/dyp_a21_can.cpp:300,331-345`
- 三号车 `src/remote_ctrl/src/remote_controller.cpp:91-96`

## 复核说明

状态用于限速、停车和避障约束。

## 关联 Package

- [[../Packages/ultrasonic_controlled_motor]]
- [[../Packages/remote_ctrl]]
- [[../Packages/trajectory_recorder]]
- [[../Packages/agv_mqtt_bridge]]

- [[../ROS接口目录|返回接口目录]]
