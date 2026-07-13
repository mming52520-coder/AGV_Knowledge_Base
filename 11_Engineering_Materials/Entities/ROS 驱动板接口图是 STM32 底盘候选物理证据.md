---
id: "agv:claim:ros-driver-board-physical-interface"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:ros-driver-board-physical-interface"
derived_from: "agv:source:ros:ros-driver-board-pinout"
source_locator: "接口定义图页"
authority: "B"
assertion_state: "reference"
applies_to_snapshot: "vendor-board-pinout"
technical_keys: ["Motor A-D", "JTAG", "OLED", "预留IO"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "reference"]
---

# ROS 驱动板接口图是 STM32 底盘候选物理证据

## 原子结论

接口图描述同系列驱动小板的连接器和预留接口。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/ROS驱动板接口定义|ROS驱动板接口定义]]
- 定位：接口定义图页
- 来源权威级别：`B`

## 适用范围

- 事实状态：`reference`
- 适用快照：`vendor-board-pinout`

## 证据与限制

缺少采购明细或铭牌确认，不能判定三号车实际采用该 PCB。

## 候选关系

- [[11_Engineering_Materials/Matches/M055-ROS 驱动板接口图是 STM32 底盘候选物理证据-STM32底盘控制器|documents_physical_interface_of → STM32底盘控制器]]
