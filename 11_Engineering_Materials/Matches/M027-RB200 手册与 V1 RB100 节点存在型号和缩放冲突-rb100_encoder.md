---
id: "agv:match:027"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:rb200-angle-scaling-conflict"
right_entity: "agv:ros:node:rb100_encoder"
target_snapshot: "code-v1"
relation: "contradicts"
match_score: 94
match_probability: 0.94
match_status: "needs-review"
match_reasons: ["寄存器 0x0064 强命中，但型号和缩放公式冲突。"]
match_keys: ["RB200", "RB100", "0x0064", "raw/100", "raw/1024*360"]
conflicts: ["RB200 raw/100 与 V1 raw/1024*360 不一致"]
assertion_state: "contradicted"
authority: "A"
implementation_evidence: "verified-static-conflict"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# RB200 手册与 V1 RB100 节点存在型号和缩放冲突 → rb100_encoder

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/RB200 手册与 V1 RB100 节点存在型号和缩放冲突|RB200 手册与 V1 RB100 节点存在型号和缩放冲突]]
- 右侧代码实体：[[03_ROS/Nodes/rb100_encoder|rb100_encoder]]
- 关系：`contradicts`
- 匹配概率：**94%**
- 匹配状态：`needs-review`
- 实现证据：`verified-static-conflict`

## 评分依据

- 寄存器 0x0064 强命中，但型号和缩放公式冲突。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- RB200 raw/100 与 V1 raw/1024*360 不一致

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
