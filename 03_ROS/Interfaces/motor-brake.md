---
id: "agv:ros:interface:motor-brake"
type: ros_interface
interface_kind: topic
ros_name: "/motor_brake"
message_type: "std_msgs/UInt8"
status: compatibility
review: verified
project: AGV
related_packages: ["[[../Packages/remote_ctrl]]", "[[../Packages/wheeltec_base]]", "[[../Packages/relay]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /motor_brake

## 作用

旧控制链的制动指令，1 表示刹车、0 表示正常。

## 通信关系

- 生产者/服务端：`remote_controller（一/二号车）`
- 消费者/客户端：`cmd_vel_adapter`、`hk_dio_remote`
- 消息或服务类型：`std_msgs/UInt8`

## 证据

- 三号车 `src/remote_ctrl/src/remote_controller.cpp（一号车）:67`
- 三号车 `src/wheeltec_base/src/cmd_vel_adapter.cpp:15,50`
- 三号车 `src/relay/src/hk_dio_remote.cpp:131`

## 复核说明

三号车 remote_controller 当前不发布该 Topic。

## 关联 Package

- [[../Packages/remote_ctrl]]
- [[../Packages/wheeltec_base]]
- [[../Packages/relay]]

- [[../ROS接口目录|返回接口目录]]
