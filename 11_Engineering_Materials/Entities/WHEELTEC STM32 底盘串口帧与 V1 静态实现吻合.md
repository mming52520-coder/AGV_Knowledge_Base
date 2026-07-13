---
id: "agv:claim:stm32-chassis-serial-framing"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:stm32-chassis-serial-framing"
derived_from: "agv:source:ros:stm32-motion-chassis-manual"
source_locator: "PDF 第 7-8 页"
authority: "A"
assertion_state: "specified"
applies_to_snapshot: "vendor-stm32-chassis-manual"
technical_keys: ["115200", "24字节", "0x7B", "0x7D", "BCC XOR", "速度", "IMU", "电池"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "specified"]
---

# WHEELTEC STM32 底盘串口帧与 V1 静态实现吻合

## 原子结论

手册规定 ROS 与 STM32 串口 115200、24 字节接收帧、0x7B/0x7D 边界和 BCC 异或校验；V1 wheeltec_base 静态实现吻合。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/STM32运动底盘开发手册|STM32运动底盘开发手册]]
- 定位：PDF 第 7-8 页
- 来源权威级别：`A`

## 适用范围

- 事实状态：`specified`
- 适用快照：`vendor-stm32-chassis-manual`

## 证据与限制

静态协议吻合不证明三号车实装硬件或运行质量。

## 候选关系

- [[11_Engineering_Materials/Matches/M051-WHEELTEC STM32 底盘串口帧与 V1 静态实现吻合-STM32底盘控制器|specifies → STM32底盘控制器]]
- [[11_Engineering_Materials/Matches/M052-WHEELTEC STM32 底盘串口帧与 V1 静态实现吻合-wheeltec_robot_node|specifies_protocol_for → wheeltec_robot_node]]
- [[11_Engineering_Materials/Matches/M053-WHEELTEC STM32 底盘串口帧与 V1 静态实现吻合--cmd_vel|specifies_transport_for → /cmd_vel]]
- [[11_Engineering_Materials/Matches/M054-WHEELTEC STM32 底盘串口帧与 V1 静态实现吻合--odom|specifies_transport_for → /odom]]
