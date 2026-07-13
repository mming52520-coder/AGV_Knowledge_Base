---
id: "agv:ros:interface:motor-services"
type: ros_interface
interface_kind: service_group
ros_name: "/motor_init + /motor_enable"
message_type: "std_srvs/Trigger; std_srvs/SetBool"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/trajectory_recorder]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /motor_init + /motor_enable

## 作用

转向电机初始化与使能。

## 通信关系

- 生产者/服务端：`steering_remote`
- 消费者/客户端：`运维工具或启动流程`
- 消息或服务类型：`std_srvs/Trigger; std_srvs/SetBool`

## 证据

- 三号车 `src/trajectory_recorder/src/steering_remote.cpp:39-40,227-234`

## 复核说明

一/二号车旧 motor_control 也曾提供同名 Service；部署时避免重复服务端。

## 关联 Package

- [[../Packages/trajectory_recorder]]

- [[../ROS接口目录|返回接口目录]]
