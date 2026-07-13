---
id: "agv:match:046"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:ackermann-proposal-interface-gap"
right_entity: "agv:system:knowledge-graph-coverage"
target_snapshot: "code-v1"
relation: "indicates_coverage_gap"
match_score: 78
match_probability: 0.78
match_status: "needs-review"
match_reasons: ["资料提示 V1 图谱可能漏记 odometer 的相对订阅接口。"]
match_keys: ["/fused_pose", "/recorded_path", "/cmd_ackermann", "mag_odom_fusion", "ackermann_pure_pursuit"]
conflicts: []
assertion_state: "planned"
authority: "B"
implementation_evidence: "coverage-candidate"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# 磁轨迹方案中的接口与 V1 图谱仅部分重合 → Knowledge Graph Coverage

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/磁轨迹方案中的接口与 V1 图谱仅部分重合|磁轨迹方案中的接口与 V1 图谱仅部分重合]]
- 右侧代码实体：[[00_System/Knowledge-Graph-Coverage|Knowledge Graph Coverage]]
- 关系：`indicates_coverage_gap`
- 匹配概率：**78%**
- 匹配状态：`needs-review`
- 实现证据：`coverage-candidate`

## 评分依据

- 资料提示 V1 图谱可能漏记 odometer 的相对订阅接口。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 无身份冲突。

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
