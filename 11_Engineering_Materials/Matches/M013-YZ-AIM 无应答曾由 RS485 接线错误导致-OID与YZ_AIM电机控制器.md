---
id: "agv:match:013"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:yz-aim-rs485-wiring-debug"
right_entity: "agv:hardware:oid-yz-aim-motor-controller"
target_snapshot: "code-v1"
relation: "tests"
match_score: 92
match_probability: 0.92
match_status: "accepted"
match_reasons: ["YZ-AIM 型号和 RS485 调试上下文命中组合硬件实体。"]
match_keys: ["YZ-AIM", "RS485", "A/B", "Modbus"]
conflicts: []
assertion_state: "observed"
authority: "B"
implementation_evidence: "field-observation"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "accepted"]
---

# YZ-AIM 无应答曾由 RS485 接线错误导致 → OID与YZ_AIM电机控制器

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/YZ-AIM 无应答曾由 RS485 接线错误导致|YZ-AIM 无应答曾由 RS485 接线错误导致]]
- 右侧代码实体：[[02_Hardware/OID与YZ_AIM电机控制器|OID与YZ_AIM电机控制器]]
- 关系：`tests`
- 匹配概率：**92%**
- 匹配状态：`accepted`
- 实现证据：`field-observation`

## 评分依据

- YZ-AIM 型号和 RS485 调试上下文命中组合硬件实体。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 无身份冲突。

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`accepted`
