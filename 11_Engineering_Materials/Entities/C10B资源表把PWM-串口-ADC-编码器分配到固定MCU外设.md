---
id: "agv:claim:c10b-resource-allocation-reference"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:c10b-resource-allocation-reference"
derived_from: "agv:source:ros:c10b-resource-map"
source_locator: "PDF 第 1 页"
authority: "A"
assertion_state: "reference"
applies_to_snapshot: "vendor-reference-c10b-resource-map"
technical_keys: ["TIM3", "UART1", "UART3", "UART4", "UART5", "ADC", "电磁巡线", "编码器"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "reference"]
---

# C10B资源表把PWM-串口-ADC-编码器分配到固定MCU外设

## 原子结论

资源表登记 C10B 的电机 PWM、蓝牙、雷达、OpenMV、CCD/电磁 ADC、编码器和超声接口分配。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/C10B主控资源分配详情表|C10B主控资源分配详情表]]
- 定位：PDF 第 1 页
- 来源权威级别：`A`

## 适用范围

- 事实状态：`reference`
- 适用快照：`vendor-reference-c10b-resource-map`

## 证据与限制

仅能说明 C10B 板级资源，不证明三号车接线、端口或设备所有权。

## 候选关系

- [[11_Engineering_Materials/Matches/M063-C10B资源表把PWM-串口-ADC-编码器分配到固定MCU外设-STM32底盘控制器|reference → STM32底盘控制器]]
