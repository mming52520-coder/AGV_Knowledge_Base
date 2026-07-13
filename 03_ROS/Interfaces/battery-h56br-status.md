---
id: "agv:ros:interface:battery-h56br-status"
type: ros_interface
interface_kind: topic
ros_name: "/battery/h56br/status"
message_type: "h56br_driver/H56BRStatus"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/h56br_driver]]", "[[../Packages/agv_mqtt_bridge]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /battery/h56br/status

## 作用

H56BR 聚合电池状态。

## 通信关系

- 生产者/服务端：`h56br_node`
- 消费者/客户端：`agv_mqtt_bridge`
- 消息或服务类型：`h56br_driver/H56BRStatus`

## 证据

- 三号车 `src/h56br_driver/src/h56br_node.cpp:57`
- 三号车 `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py`

## 复核说明

包含的字段以 H56BRStatus.msg 为准。

## 关联 Package

- [[../Packages/h56br_driver]]
- [[../Packages/agv_mqtt_bridge]]

- [[../ROS接口目录|返回接口目录]]
