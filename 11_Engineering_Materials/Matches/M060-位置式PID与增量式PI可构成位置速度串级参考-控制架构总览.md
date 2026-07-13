---
id: "agv:match:060"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:wheeltec-pid-control-reference"
right_entity: "agv:control:overview"
target_snapshot: "code-v1"
relation: "related_theory"
match_score: 60
match_probability: 0.6
match_status: "weak-candidate"
match_reasons: ["位置、速度和串级反馈是控制架构的一般理论参考。"]
match_keys: ["位置式PID", "增量式PI", "编码器反馈", "位置环", "速度环", "限幅"]
conflicts: []
assertion_state: "reference"
authority: "B"
implementation_evidence: "theory-only"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "weak-candidate"]
---

# 位置式PID与增量式PI可构成位置速度串级参考 → 控制架构总览

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/位置式PID与增量式PI可构成位置速度串级参考|位置式PID与增量式PI可构成位置速度串级参考]]
- 右侧代码实体：[[05_Control/控制架构总览|控制架构总览]]
- 关系：`related_theory`
- 匹配概率：**60%**
- 匹配状态：`weak-candidate`
- 实现证据：`theory-only`

## 评分依据

- 位置、速度和串级反馈是控制架构的一般理论参考。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 无身份冲突。

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`weak-candidate`
