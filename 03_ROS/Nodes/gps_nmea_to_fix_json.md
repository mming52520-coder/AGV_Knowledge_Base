---
id: "agv:ros:node:gps_nmea_to_fix_json"
type: ros_node
ros_name: "/gps_nmea_to_fix_json"
executable: "gps_nmea_to_fix_json.py"
status: active
review: verified
project: AGV
vehicles: [三号车]
package: "[[../Packages/agv_mqtt_bridge]]"
parent: "[[../../01_Project_AGV/Layers/传感器与设备驱动层]]"
publishes: ["[[../Interfaces/gps-fix-json]]"]
subscribes: []
provides_services: []
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Node, agv_mqtt_bridge]
---

# gps_nmea_to_fix_json

## 职责

读取 NMEA 定位输入并发布 JSON 格式定位状态。

## 身份

- ROS 默认名：`/gps_nmea_to_fix_json`
- 可执行入口：`gps_nmea_to_fix_json.py`
- 所属 Package：[[../Packages/agv_mqtt_bridge]]
- 车辆：三号车

## 通信接口

- 发布：[[../Interfaces/gps-fix-json]]

## Launch

- `src/agv_mqtt_bridge/launch/gps_nmea.launch`

## 源码证据

- 三号车 `src/agv_mqtt_bridge/scripts/gps_nmea_to_fix_json.py:79,86,275`

## 复核说明

三号车新增诊断/定位能力；输入设备参数不写入知识库。

## 关联

- [[../../01_Project_AGV/Layers/传感器与设备驱动层]]
- [[../ROS系统总览]]
