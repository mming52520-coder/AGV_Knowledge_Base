---
id: "agv:ros:interface:gps-fix-json"
type: ros_interface
interface_kind: topic
ros_name: "/gps/fix_json"
message_type: "std_msgs/String (JSON)"
status: active
review: verified
project: AGV
related_packages: ["[[../Packages/agv_mqtt_bridge]]"]
source_scope: 三号车当前工作区与车辆差异
source_snapshot: "448336f86dd9debc9362e3262da712fa95c04a986863211d9b865d7bbba09d96"
updated: 2026-07-14
tags: [AGV, ROS, Interface]
---

# /gps/fix_json

## 作用

三号车将 NMEA 定位转换成 JSON 字符串。

## 通信关系

- 生产者/服务端：`gps_nmea_to_fix_json`
- 消费者/客户端：`MQTT/定位消费者`
- 消息或服务类型：`std_msgs/String (JSON)`

## 证据

- 三号车 `src/agv_mqtt_bridge/scripts/gps_nmea_to_fix_json.py:79,86,275`

## 复核说明

默认 Topic 可由私有参数覆盖。

## 关联 Package

- [[../Packages/agv_mqtt_bridge]]

- [[../ROS接口目录|返回接口目录]]
