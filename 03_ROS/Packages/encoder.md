---
id: "agv:ros:package:encoder"
type: ros_package
status: active
review: generated
project: AGV
version: "0.0.0"
vehicles: [一号车, 二号车, 三号车]
parent: "[[../../01_Project_AGV/Layers/传感器与设备驱动层]]"
source_scope: 三号车当前工作区与三车差异扫描
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Package, encoder]
---

# encoder

## 职责

读取编码器并发布角度、速度和里程状态。

## 车辆分布

- 一号车、二号车、三号车
- 三车聚合快照一致；是否由默认 Bringup 启动仍需按车辆部署确认。

## 构建与运行

- 版本：`0.0.0`
- 可执行目标：`rb100_encoder`
- 主要依赖：`roscpp`、`rospy`、`std_msgs`

## 源码证据

- 三号车 `src/encoder/package.xml`
- 三号车 `src/encoder/src/rb100_encoder.cpp`

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
