---
id: "agv:ros:package:relay"
type: ros_package
status: compatibility
review: needs-review
project: AGV
version: "0.0.0"
vehicles: [一号车, 二号车, 三号车]
parent: "[[../../01_Project_AGV/Layers/底盘与执行抽象层]]"
source_scope: 三号车当前工作区与三车差异扫描
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Package, relay]
---

# relay

## 职责

华控数字 IO、继电器和制动相关控制。

## 车辆分布

- 一号车、二号车、三号车
- Launch 中声明的 pkg 为 hk_dio_controller，与本地 package 名 relay 不一致，需要在运行环境复核来源。

## 构建与运行

- 版本：`0.0.0`
- 可执行目标：`hk_dio`、`hk_dio_remote`
- 主要依赖：`roscpp`、`rospy`、`std_msgs`

## 源码证据

- 三号车 `src/relay/package.xml`
- 三号车 `src/relay/src/hk_dio.cpp`
- 三号车 `src/relay/src/hk_dio_remote.cpp`
- 三号车 `src/relay/launch/hk_dio.launch`

## 关联

- [[../../01_Project_AGV/Layers/底盘与执行抽象层]]
- [[../ROS系统总览]]
