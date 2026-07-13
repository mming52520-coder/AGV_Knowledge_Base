---
id: "agv:ros:interface:drive-feedback"
type: ros_interface
interface_kind: topic_group
ros_name: "/drive_feedback_odom + /drive_feedback_speed + /drive_feedback_twist"
message_type: "nav_msgs/Odometry; std_msgs/Float32; geometry_msgs/TwistStamped"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/chassis_controller]]", "[[../Packages/trajectory_recorder]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /drive_feedback_odom + /drive_feedback_speed + /drive_feedback_twist

## 作用

三号车从底盘状态派生的驱动反馈里程与速度。

## 通信关系

- 生产者/服务端：`drive_feedback_odom`
- 消费者/客户端：`trajectory_recorder`、`trajectory_tracker`
- 消息或服务类型：`nav_msgs/Odometry; std_msgs/Float32; geometry_msgs/TwistStamped`

## 证据

- 三号车 `src/chassis_controller/src/drive_feedback_odom.cpp:18-21,57-60`
- 三号车 `src/trajectory_recorder/src/trajectory_tracker.cpp:3412,3936`

## 复核说明

三号车新增；可用于替代或融合其他里程来源。

## 关联 Package

- [[../Packages/chassis_controller]]
- [[../Packages/trajectory_recorder]]

- [[../ROS接口目录|返回接口目录]]
