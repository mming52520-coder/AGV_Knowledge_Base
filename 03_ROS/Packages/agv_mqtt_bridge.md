---
id: "agv:ros:package:agv_mqtt_bridge"
type: ros_package
status: active
review: generated
project: AGV
version: "0.1.0"
vehicles: [一号车, 二号车, 三号车]
parent: "[[../../01_Project_AGV/Layers/启动与外部通信层]]"
source_scope: 三号车当前工作区与三车差异扫描
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Package, agv_mqtt_bridge]
---

# agv_mqtt_bridge

## 职责

ROS 与 MQTT 的双向桥接：上报整车遥测，接收后端命令；三号车增加 GPS NMEA 转换。

## 车辆分布

- 一号车、二号车、三号车
- Topic 名称大量由参数读取；静态扫描只确认订阅结构，实际运行名称需结合配置复核。

## 构建与运行

- 版本：`0.1.0`
- 可执行目标：`agv_mqtt_bridge.py`、`gps_nmea_to_fix_json.py（三号车）`
- 主要依赖：`rospy`、`std_msgs`、`sensor_msgs`、`nav_msgs`、`h56br_driver`、`magnetic_controlled_motor`、`ultrasonic_controlled_motor`、`python3-paho-mqtt`

## 源码证据

- 三号车 `src/agv_mqtt_bridge/package.xml`
- 三号车 `src/agv_mqtt_bridge/scripts/agv_mqtt_bridge.py`
- 三号车 `src/agv_mqtt_bridge/launch/agv_mqtt_bridge.launch`

## 关联

- [[../../01_Project_AGV/Layers/启动与外部通信层]]
- [[../ROS系统总览]]
