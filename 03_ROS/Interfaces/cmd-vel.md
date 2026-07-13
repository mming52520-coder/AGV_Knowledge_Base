---
id: "agv:ros:interface:cmd-vel"
type: ros_interface
interface_kind: topic
ros_name: "/cmd_vel"
message_type: "geometry_msgs/Twist"
status: compatibility
review: verified
project: AGV
related_packages: ["[[../Packages/wheeltec_base]]", "[[../Packages/remote_ctrl]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /cmd_vel

## 作用

ROS 标准底盘速度接口。

## 通信关系

- 生产者/服务端：`cmd_vel_adapter`、`示例手柄脚本`
- 消费者/客户端：`wheeltec_robot`
- 消息或服务类型：`geometry_msgs/Twist`

## 证据

- 三号车 `src/wheeltec_base/src/cmd_vel_adapter.cpp:46`
- 三号车 `src/wheeltec_base/src/wheeltec_robot.cpp:302`

## 复核说明

一号车默认链路使用；三号车主要使用 /chassis/cmd。

## 关联 Package

- [[../Packages/wheeltec_base]]
- [[../Packages/remote_ctrl]]

- [[../ROS接口目录|返回接口目录]]
