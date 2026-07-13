---
id: "agv:claim:wheeltec-pid-control-reference"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:wheeltec-pid-control-reference"
derived_from: "agv:source:ros:wheeltec-pid-guide"
source_locator: "PDF 第 16-25 页"
authority: "B"
assertion_state: "reference"
applies_to_snapshot: "vendor-reference-pid-tutorial"
technical_keys: ["位置式PID", "增量式PI", "编码器反馈", "位置环", "速度环", "限幅"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "reference"]
---

# 位置式PID与增量式PI可构成位置速度串级参考

## 原子结论

手册给出编码器反馈下的位置式 PID、增量式速度 PI 和位置外环-速度内环的串级结构。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/WHEELTEC PID基础入门开发手册|WHEELTEC PID基础入门开发手册]]
- 定位：PDF 第 16-25 页
- 来源权威级别：`B`

## 适用范围

- 事实状态：`reference`
- 适用快照：`vendor-reference-pid-tutorial`

## 证据与限制

教程公式和示例代码不证明三号车采用相同控制律、采样周期、限幅或增益。

## 候选关系

- [[11_Engineering_Materials/Matches/M060-位置式PID与增量式PI可构成位置速度串级参考-控制架构总览|related_theory → 控制架构总览]]
