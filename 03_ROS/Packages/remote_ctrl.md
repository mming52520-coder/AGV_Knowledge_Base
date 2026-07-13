---
id: "agv:ros:package:remote_ctrl"
type: ros_package
status: active
review: generated
project: AGV
version: "0.0.0"
vehicles: [一号车, 二号车, 三号车]
parent: "[[../../01_Project_AGV/Layers/任务与应用编排层]]"
source_scope: 三号车当前工作区与三车差异扫描
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Package, remote_ctrl]
---

# remote_ctrl

## 职责

处理本地手柄与云端遥控，输出驱动、转向和制动意图，并接入超声安全状态。

## 车辆分布

- 一号车、二号车、三号车
- 三号车 remote_controller 可发布结构化 /chassis/cmd；一号车仍以旧控制 Topic 为主。

## 构建与运行

- 版本：`0.0.0`
- 可执行目标：`remote_controller`、`joy_turtlebot.py`、`joy_turtlesim.py`
- 主要依赖：`roscpp`、`rospy`、`std_msgs`、`sensor_msgs`、`ultrasonic_controlled_motor`

## 源码证据

- 三号车 `src/remote_ctrl/package.xml`
- 三号车 `src/remote_ctrl/src/remote_controller.cpp`
- 三号车 `src/remote_ctrl/launch/remote_ctrl.launch`

## 关联

- [[../../01_Project_AGV/Layers/任务与应用编排层]]
- [[../ROS系统总览]]
