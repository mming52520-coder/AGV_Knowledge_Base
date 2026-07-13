---
id: "agv:ros:node:hk_dio_remote"
type: ros_node
ros_name: "/hk_dio_remote"
executable: "hk_dio_remote"
status: compatibility
review: verified
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/relay]]"
parent: "[[../../01_Project_AGV/Layers/底盘与执行抽象层]]"
publishes: []
subscribes: ["[[../Interfaces/motor-brake]]", "[[../Interfaces/motor-speed]]"]
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, relay]
---

# hk_dio_remote

## 职责

根据旧控制 Topic 驱动制动或继电器输出。

## 身份

- ROS 默认名：`/hk_dio_remote`
- 可执行入口：`hk_dio_remote`
- 所属 Package：[[../Packages/relay]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 订阅：[[../Interfaces/motor-brake]]
- 订阅：[[../Interfaces/motor-speed]]

## Launch

- `src/remote_ctrl/launch/remote_ctrl.launch`（一/二号车）

## 源码证据

- 三号车 `src/relay/src/hk_dio_remote.cpp:119,131`

## 复核说明

三号车默认遥控 Launch 不启动该节点。

## 关联

- [[../../01_Project_AGV/Layers/底盘与执行抽象层]]
- [[../ROS系统总览]]
