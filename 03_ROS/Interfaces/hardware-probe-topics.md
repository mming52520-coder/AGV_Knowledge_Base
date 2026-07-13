---
id: "agv:ros:interface:hardware-probe-topics"
type: ros_interface
interface_kind: topic_group
ros_name: "/imu/probe_* + /encoder_probe/* + ~yz_aim_probe/*"
message_type: "多种诊断消息"
status: diagnostic
review: verified
project: AGV
related_packages: ["[[../Packages/trajectory_recorder]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /imu/probe_* + /encoder_probe/* + ~yz_aim_probe/*

## 作用

三号车 IMU、编码器和转向伺服的独立诊断 Topic。

## 通信关系

- 生产者/服务端：`imu_probe`、`encoder_probe`、`yz_aim_probe`
- 消费者/客户端：`调试工具`
- 消息或服务类型：`多种诊断消息`

## 证据

- 三号车 `src/trajectory_recorder/src/imu_probe_node.cpp:107-108`
- 三号车 `src/trajectory_recorder/src/encoder_probe_node.cpp:109-110`
- 三号车 `src/trajectory_recorder/src/yz_aim_probe_node.cpp:41-49`

## 复核说明

仅用于诊断和标定，不应被误认为默认生产控制链。

## 关联 Package

- [[../Packages/trajectory_recorder]]

- [[../ROS接口目录|返回接口目录]]
