---
id: "agv:match:031"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:huakong-digital-io-protocol"
right_entity: "agv:ros:node:hk_dio_controller"
target_snapshot: "code-v1"
relation: "specifies_protocol_for"
match_score: 100
match_probability: 1.0
match_status: "accepted"
match_reasons: ["38400、功能码 01/02/05 和基址静态吻合。"]
match_keys: ["1-48路", "38400", "01", "02", "05", "线圈0", "离散输入0"]
conflicts: []
assertion_state: "specified"
authority: "A"
implementation_evidence: "verified-static"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "accepted"]
---

# 华控数字 IO 功能码与默认串口参数 → hk_dio_controller

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/华控数字 IO 功能码与默认串口参数|华控数字 IO 功能码与默认串口参数]]
- 右侧代码实体：[[03_ROS/Nodes/hk_dio_controller|hk_dio_controller]]
- 关系：`specifies_protocol_for`
- 匹配概率：**100%**
- 匹配状态：`accepted`
- 实现证据：`verified-static`

## 评分依据

- 38400、功能码 01/02/05 和基址静态吻合。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 无身份冲突。

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`accepted`
