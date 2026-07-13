---
id: "agv:ros:interface:relay-io-status"
type: ros_interface
interface_kind: topic_group
ros_name: "hk_dio/input_status + hk_dio/relay_status"
message_type: "std_msgs/相关类型"
status: compatibility
review: needs-review
project: AGV
related_packages: ["[[../Packages/relay]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# hk_dio/input_status + hk_dio/relay_status

## 作用

华控数字 IO 与继电器状态。

## 通信关系

- 生产者/服务端：`hk_dio_controller`
- 消费者/客户端：`运维或状态消费者`
- 消息或服务类型：`std_msgs/相关类型`

## 证据

- 三号车 `src/relay/src/hk_dio.cpp`

## 复核说明

本地 package 名与 Launch 中声明的 hk_dio_controller 不一致，需运行时复核。

## 关联 Package

- [[../Packages/relay]]

- [[../ROS接口目录|返回接口目录]]
