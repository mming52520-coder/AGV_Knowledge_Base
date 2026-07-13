---
id: "agv:match:062"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:ackermann-kinematics-reference-model"
right_entity: "agv:ros:node:odometer"
target_snapshot: "code-v1"
relation: "related_theory"
match_score: 65
match_probability: 0.65
match_status: "needs-review"
match_reasons: ["车体速度到位姿传播与轮式运动学相关。"]
match_keys: ["Ackermann", "ICR", "轮距", "轴距", "正运动学", "逆运动学", "转角拟合"]
conflicts: ["不能据理论资料确认 V1 odometer 的参数或正确性"]
assertion_state: "reference"
authority: "B"
implementation_evidence: "theory-only"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# 阿克曼运动学以共同瞬心和几何约束关联车速与转角 → odometer

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/阿克曼运动学以共同瞬心和几何约束关联车速与转角|阿克曼运动学以共同瞬心和几何约束关联车速与转角]]
- 右侧代码实体：[[03_ROS/Nodes/odometer|odometer]]
- 关系：`related_theory`
- 匹配概率：**65%**
- 匹配状态：`needs-review`
- 实现证据：`theory-only`

## 评分依据

- 车体速度到位姿传播与轮式运动学相关。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 不能据理论资料确认 V1 odometer 的参数或正确性

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
