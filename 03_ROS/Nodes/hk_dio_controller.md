---
id: "agv:ros:node:hk_dio_controller"
type: ros_node
ros_name: "/hk_dio_controller"
executable: "hk_dio"
status: compatibility
review: needs-review
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/relay]]"
parent: "[[../../01_Project_AGV/Layers/底盘与执行抽象层]]"
publishes: ["[[../Interfaces/relay-io-status]]"]
subscribes: []
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, relay]
---

# hk_dio_controller

## 职责

控制华控数字 IO/继电器并发布状态。

## 身份

- ROS 默认名：`/hk_dio_controller`
- 可执行入口：`hk_dio`
- 所属 Package：[[../Packages/relay]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 发布：[[../Interfaces/relay-io-status]]

## Launch

- `src/relay/launch/hk_dio.launch`

## 源码证据

- 三号车 `src/relay/src/hk_dio.cpp:845`
- 三号车 `src/relay/launch/hk_dio.launch`

## 复核说明

Launch 声明 pkg=hk_dio_controller，与本地 package=relay 不一致。

## 关联

- [[../../01_Project_AGV/Layers/底盘与执行抽象层]]
- [[../ROS系统总览]]
