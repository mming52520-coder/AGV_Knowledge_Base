---
id: "agv:ros:node:agv_mqtt_bridge"
type: ros_node
ros_name: "/agv_mqtt_bridge"
executable: "agv_mqtt_bridge.py"
status: active
review: needs-review
project: AGV
vehicles: [一号车, 二号车, 三号车]
package: "[[../Packages/agv_mqtt_bridge]]"
parent: "[[../../01_Project_AGV/Layers/启动与外部通信层]]"
publishes: []
subscribes: ["[[../Interfaces/odom]]", "[[../Interfaces/imu]]", "[[../Interfaces/battery-h56br-status]]", "[[../Interfaces/battery-h56br-soc]]", "[[../Interfaces/mag-sensor-frame]]", "[[../Interfaces/mag-sensor-nail-event]]", "[[../Interfaces/ultrasonic-distance]]", "[[../Interfaces/ultrasonic-status]]", "[[../Interfaces/trajectory-status]]", "[[../Interfaces/agv-task-state]]", "[[../Interfaces/motor-command]]", "[[../Interfaces/motor-speed]]", "[[../Interfaces/motor-brake]]"]
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, agv_mqtt_bridge]
---

# agv_mqtt_bridge

## 职责

把 ROS 遥测转换为 MQTT 消息，并把后端控制转换为 ROS 命令。

## 身份

- ROS 默认名：`/agv_mqtt_bridge`
- 可执行入口：`agv_mqtt_bridge.py`
- 所属 Package：[[../Packages/agv_mqtt_bridge]]
- 车辆：一号车、二号车、三号车

## 通信接口

- 订阅：[[../Interfaces/odom]]
- 订阅：[[../Interfaces/imu]]
- 订阅：[[../Interfaces/battery-h56br-status]]
- 订阅：[[../Interfaces/battery-h56br-soc]]
- 订阅：[[../Interfaces/mag-sensor-frame]]
- 订阅：[[../Interfaces/mag-sensor-nail-event]]
- 订阅：[[../Interfaces/ultrasonic-distance]]
- 订阅：[[../Interfaces/ultrasonic-status]]
- 订阅：[[../Interfaces/trajectory-status]]
- 订阅：[[../Interfaces/agv-task-state]]
- 订阅：[[../Interfaces/motor-command]]
- 订阅：[[../Interfaces/motor-speed]]
- 订阅：[[../Interfaces/motor-brake]]

## Launch

- `src/agv_mqtt_bridge/launch/agv_mqtt_bridge.launch`

## 源码证据

- 三号车 `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py:474-667,1688`

## 复核说明

订阅 Topic 大量由参数动态生成；当前页面记录架构中明确的关键接口，不包含任何 MQTT 凭据或服务器地址。

## 关联

- [[../../01_Project_AGV/Layers/启动与外部通信层]]
- [[../ROS系统总览]]
