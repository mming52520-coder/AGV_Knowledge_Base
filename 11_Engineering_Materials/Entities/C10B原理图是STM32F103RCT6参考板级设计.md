---
id: "agv:claim:c10b-mainboard-reference-schematic"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:c10b-mainboard-reference-schematic"
derived_from: "agv:source:ros:c10b-mainboard-schematic-2025"
source_locator: "PDF 第 1-3 页"
authority: "A"
assertion_state: "reference"
applies_to_snapshot: "vendor-reference-c10b-schematic-2025"
technical_keys: ["STM32F103RCT6", "DCDC", "3.3V", "串口", "PWM", "ADC"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "reference"]
---

# C10B原理图是STM32F103RCT6参考板级设计

## 原子结论

原理图描述 C10B 的电源、STM32F103RCT6 主控与板级外设连接。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/C10B主板原理图2025-02-24|C10B主板原理图2025-02-24]]
- 定位：PDF 第 1-3 页
- 来源权威级别：`A`

## 适用范围

- 事实状态：`reference`
- 适用快照：`vendor-reference-c10b-schematic-2025`

## 证据与限制

未由采购、铭牌或三号车线束确认该 PCB；只能建立 reference 关系。

## 候选关系

- [[11_Engineering_Materials/Matches/M064-C10B原理图是STM32F103RCT6参考板级设计-STM32底盘控制器|reference → STM32底盘控制器]]
