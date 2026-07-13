---
id: "agv:claim:dyp-a21-can-protocol"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:dyp-a21-can-protocol"
derived_from: "agv:source:ros:dyp-a21-datasheet"
source_locator: "PDF 第 4、6、26-29 页"
authority: "A"
assertion_state: "specified"
applies_to_snapshot: "vendor-datasheet-dyp-a21-v1.0"
technical_keys: ["DYP-A21", "250Kbps", "0x0520+地址", "03/83", "0xFFFE", "0xFFFD", "0xFFFF"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "specified"]
---

# DYP-A21 CAN 帧与异常值协议

## 原子结论

手册规定标准 CAN 帧、默认 250 Kbps、CAN ID 0x0520 加地址，以及测量与异常值语义；V1 静态实现与核心字段吻合。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/DYP-A21产品规格书|DYP-A21产品规格书]]
- 定位：PDF 第 4、6、26-29 页
- 来源权威级别：`A`

## 适用范围

- 事实状态：`specified`
- 适用快照：`vendor-datasheet-dyp-a21-v1.0`

## 证据与限制

静态吻合不等于已在当前车辆运行验证。

## 候选关系

- [[11_Engineering_Materials/Matches/M018-DYP-A21 CAN 帧与异常值协议-DYP-A21超声传感器|specifies → DYP-A21超声传感器]]
- [[11_Engineering_Materials/Matches/M019-DYP-A21 CAN 帧与异常值协议-dyp_a21_can_node|specifies_protocol_for → dyp_a21_can_node]]
- [[11_Engineering_Materials/Matches/M020-DYP-A21 CAN 帧与异常值协议-超声距离话题|specifies_payload_for → 超声距离话题]]
- [[11_Engineering_Materials/Matches/M021-DYP-A21 CAN 帧与异常值协议-超声状态话题|specifies_payload_for → 超声状态话题]]
