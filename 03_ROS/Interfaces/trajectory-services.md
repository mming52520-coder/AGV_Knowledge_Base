---
id: "agv:ros:interface:trajectory-services"
type: ros_interface
interface_kind: service_group
ros_name: "/trajectory/* + /imu/* + /steering/*"
message_type: "std_srvs/Trigger"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/trajectory_recorder]]", "[[../Packages/agv_mqtt_bridge]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /trajectory/* + /imu/* + /steering/*

## 作用

轨迹记录/播放/停止/暂停、IMU 标定和转向参数操作。

## 通信关系

- 生产者/服务端：`trajectory_recorder`、`trajectory_tracker`
- 消费者/客户端：`后端命令或运维工具`
- 消息或服务类型：`std_srvs/Trigger`

## 证据

- 三号车 `src/trajectory_recorder/src/trajectory_recorder.cpp:1193-1202,1349-1438`
- 三号车 `src/trajectory_recorder/src/trajectory_tracker.cpp:3942-3959,4228-4497`

## 复核说明

三号车额外提供 /trajectory/realtime_mag_start。

## 关联 Package

- [[../Packages/trajectory_recorder]]
- [[../Packages/agv_mqtt_bridge]]

- [[../ROS接口目录|返回接口目录]]
