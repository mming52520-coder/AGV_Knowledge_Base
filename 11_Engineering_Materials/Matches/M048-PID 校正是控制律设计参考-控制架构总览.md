---
id: "agv:match:048"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:pid-control-reference"
right_entity: "agv:control:overview"
target_snapshot: "code-v1"
relation: "related_theory"
match_score: 60
match_probability: 0.6
match_status: "weak-candidate"
match_reasons: ["PID 是控制架构的一般参考，不能证明具体实现。"]
match_keys: ["PID", "比例", "积分", "微分"]
conflicts: []
assertion_state: "reference"
authority: "B"
implementation_evidence: "theory-only"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "weak-candidate"]
---

# PID 校正是控制律设计参考 → 控制架构总览

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/PID 校正是控制律设计参考|PID 校正是控制律设计参考]]
- 右侧代码实体：[[05_Control/控制架构总览|控制架构总览]]
- 关系：`related_theory`
- 匹配概率：**60%**
- 匹配状态：`weak-candidate`
- 实现证据：`theory-only`

## 评分依据

- PID 是控制架构的一般参考，不能证明具体实现。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 无身份冲突。

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`weak-candidate`
