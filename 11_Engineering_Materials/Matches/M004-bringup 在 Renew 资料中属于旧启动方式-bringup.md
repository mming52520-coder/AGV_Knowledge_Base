---
id: "agv:match:004"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:bringup-historical-entry"
right_entity: "agv:ros:package:bringup"
target_snapshot: "code-v1"
relation: "deprecates_in_context"
match_score: 98
match_probability: 0.98
match_status: "accepted"
match_reasons: ["包名与旧入口角色精确命中。"]
match_keys: ["bringup", "all_nodes.launch", "integrated.launch"]
conflicts: []
assertion_state: "deprecated"
authority: "B"
implementation_evidence: "historical-document"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "accepted"]
---

# bringup 在 Renew 资料中属于旧启动方式 → bringup

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/bringup 在 Renew 资料中属于旧启动方式|bringup 在 Renew 资料中属于旧启动方式]]
- 右侧代码实体：[[03_ROS/Packages/bringup|bringup]]
- 关系：`deprecates_in_context`
- 匹配概率：**98%**
- 匹配状态：`accepted`
- 实现证据：`historical-document`

## 评分依据

- 包名与旧入口角色精确命中。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 无身份冲突。

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`accepted`
