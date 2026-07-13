---
id: "agv:match:033"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:yz-aim-register-protocol"
right_entity: "agv:hardware:oid-yz-aim-motor-controller"
target_snapshot: "code-v1"
relation: "specifies_component_of"
match_score: 88
match_probability: 0.88
match_status: "needs-review"
match_reasons: ["仅命中组合实体的 YZ_AIM 部分。"]
match_keys: ["115200", "0x009F", "0x00D4", "YZ_AIM"]
conflicts: ["不得把该手册外推到OID后端"]
assertion_state: "specified"
authority: "A"
implementation_evidence: "vendor-specification"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# 立三 YZ_AIM 部分的 RS485 寄存器协议 → OID与YZ_AIM电机控制器

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/立三 YZ_AIM 部分的 RS485 寄存器协议|立三 YZ_AIM 部分的 RS485 寄存器协议]]
- 右侧代码实体：[[02_Hardware/OID与YZ_AIM电机控制器|OID与YZ_AIM电机控制器]]
- 关系：`specifies_component_of`
- 匹配概率：**88%**
- 匹配状态：`needs-review`
- 实现证据：`vendor-specification`

## 评分依据

- 仅命中组合实体的 YZ_AIM 部分。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 不得把该手册外推到OID后端

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
