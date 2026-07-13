---
id: "agv:match:045"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:ackermann-proposal-interface-gap"
right_entity: "agv:ros:node:odometer"
target_snapshot: "code-v1"
relation: "related_to"
match_score: 80
match_probability: 0.8
match_status: "needs-review"
match_reasons: ["相对 ackermann_cmd 订阅与方案控制话题部分相关，但不是同名接口。"]
match_keys: ["/fused_pose", "/recorded_path", "/cmd_ackermann", "mag_odom_fusion", "ackermann_pure_pursuit"]
conflicts: ["/cmd_ackermann与相对ackermann_cmd不可自动合并"]
assertion_state: "planned"
authority: "B"
implementation_evidence: "coverage-candidate"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# 磁轨迹方案中的接口与 V1 图谱仅部分重合 → odometer

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/磁轨迹方案中的接口与 V1 图谱仅部分重合|磁轨迹方案中的接口与 V1 图谱仅部分重合]]
- 右侧代码实体：[[03_ROS/Nodes/odometer|odometer]]
- 关系：`related_to`
- 匹配概率：**80%**
- 匹配状态：`needs-review`
- 实现证据：`coverage-candidate`

## 评分依据

- 相对 ackermann_cmd 订阅与方案控制话题部分相关，但不是同名接口。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- /cmd_ackermann与相对ackermann_cmd不可自动合并

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
