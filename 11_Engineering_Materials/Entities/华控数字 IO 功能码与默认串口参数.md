---
id: "agv:claim:huakong-digital-io-protocol"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:huakong-digital-io-protocol"
derived_from: "agv:source:ros:huakong-digital-io-rs485-manual"
source_locator: "PDF 第 4-5、9 页"
authority: "A"
assertion_state: "specified"
applies_to_snapshot: "vendor-huakong-dio-manual"
technical_keys: ["1-48路", "38400", "01", "02", "05", "线圈0", "离散输入0"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "specified"]
---

# 华控数字 IO 功能码与默认串口参数

## 原子结论

手册规定数字输入、继电器输出、默认 38400/8N1 以及功能码 01/02/05；V1 hk_dio 静态实现与主要协议字段吻合。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/华控数字量输入输出模块RS485手册|华控数字量输入输出模块RS485手册]]
- 定位：PDF 第 4-5、9 页
- 来源权威级别：`A`

## 适用范围

- 事实状态：`specified`
- 适用快照：`vendor-huakong-dio-manual`

## 证据与限制

V1 已知 launch 包名不一致仍需复核；不自动执行继电器写操作。

## 候选关系

- [[11_Engineering_Materials/Matches/M030-华控数字 IO 功能码与默认串口参数-华控IO与模拟量模块|specifies → 华控IO与模拟量模块]]
- [[11_Engineering_Materials/Matches/M031-华控数字 IO 功能码与默认串口参数-hk_dio_controller|specifies_protocol_for → hk_dio_controller]]
- [[11_Engineering_Materials/Matches/M032-华控数字 IO 功能码与默认串口参数-继电器与IO状态|specifies_payload_for → 继电器与IO状态]]
