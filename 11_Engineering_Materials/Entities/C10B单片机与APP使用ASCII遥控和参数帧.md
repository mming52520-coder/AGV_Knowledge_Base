---
id: "agv:claim:c10b-mcu-app-reference-protocol"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:c10b-mcu-app-reference-protocol"
derived_from: "agv:source:ros:c10b-mcu-app-protocol"
source_locator: "PDF 第 4-9 页"
authority: "A"
assertion_state: "reference"
applies_to_snapshot: "vendor-reference-c10b-app"
technical_keys: ["APP", "UART", "ASCII", "遥控字符", "参数帧", "状态帧"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "reference"]
---

# C10B单片机与APP使用ASCII遥控和参数帧

## 原子结论

协议定义 APP 经通信模块与 MCU 交换 ASCII 遥控字符、调参帧及状态/波形显示帧。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/C10B单片机与APP通信协议|C10B单片机与APP通信协议]]
- 定位：PDF 第 4-9 页
- 来源权威级别：`A`

## 适用范围

- 事实状态：`reference`
- 适用快照：`vendor-reference-c10b-app`

## 证据与限制

未发现三号车当前代码使用该 APP 协议；不得把同属遥控概念视为接口同一或已实现。

## 候选关系

- [[11_Engineering_Materials/Matches/M058-C10B单片机与APP使用ASCII遥控和参数帧-控制架构总览|reference → 控制架构总览]]
