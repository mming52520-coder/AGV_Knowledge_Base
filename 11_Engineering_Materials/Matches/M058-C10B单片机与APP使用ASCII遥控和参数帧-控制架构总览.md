---
id: "agv:match:058"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:c10b-mcu-app-reference-protocol"
right_entity: "agv:control:overview"
target_snapshot: "code-v1"
relation: "reference"
match_score: 55
match_probability: 0.55
match_status: "needs-review"
match_reasons: ["APP 遥控与调参属于控制输入参考，但没有当前代码接口命中。"]
match_keys: ["APP", "UART", "ASCII", "遥控字符", "参数帧", "状态帧"]
conflicts: ["未发现三号车 APP 协议实现"]
assertion_state: "reference"
authority: "A"
implementation_evidence: "reference-model-mismatch"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# C10B单片机与APP使用ASCII遥控和参数帧 → 控制架构总览

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/C10B单片机与APP使用ASCII遥控和参数帧|C10B单片机与APP使用ASCII遥控和参数帧]]
- 右侧代码实体：[[05_Control/控制架构总览|控制架构总览]]
- 关系：`reference`
- 匹配概率：**55%**
- 匹配状态：`needs-review`
- 实现证据：`reference-model-mismatch`

## 评分依据

- APP 遥控与调参属于控制输入参考，但没有当前代码接口命中。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 未发现三号车 APP 协议实现

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
