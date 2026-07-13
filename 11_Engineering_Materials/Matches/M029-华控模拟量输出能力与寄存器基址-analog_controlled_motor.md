---
id: "agv:match:029"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:huakong-analog-output-protocol"
right_entity: "agv:ros:package:analog_controlled_motor"
target_snapshot: "code-v1"
relation: "documents_intended_for"
match_score: 100
match_probability: 1.0
match_status: "accepted"
match_reasons: ["寄存器基址 0x000A 静态吻合；V1 包状态为 inactive。"]
match_keys: ["1-12路", "0-5V", "0-10V", "0-20mA", "4-20mA", "12位", "0x000A"]
conflicts: []
assertion_state: "specified"
authority: "A"
implementation_evidence: "verified-static-not-deployed"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "accepted"]
---

# 华控模拟量输出能力与寄存器基址 → analog_controlled_motor

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/华控模拟量输出能力与寄存器基址|华控模拟量输出能力与寄存器基址]]
- 右侧代码实体：[[03_ROS/Packages/analog_controlled_motor|analog_controlled_motor]]
- 关系：`documents_intended_for`
- 匹配概率：**100%**
- 匹配状态：`accepted`
- 实现证据：`verified-static-not-deployed`

## 评分依据

- 寄存器基址 0x000A 静态吻合；V1 包状态为 inactive。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 无身份冲突。

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`accepted`
