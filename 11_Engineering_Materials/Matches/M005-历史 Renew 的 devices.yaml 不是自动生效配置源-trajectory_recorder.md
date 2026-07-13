---
id: "agv:match:005"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:devices-yaml-not-authoritative"
right_entity: "agv:ros:package:trajectory_recorder"
target_snapshot: "code-v1"
relation: "configuration_constraint"
match_score: 88
match_probability: 0.88
match_status: "needs-review"
match_reasons: ["配置文件路径和 launch 参数上下文命中；需在目标快照复核加载链。"]
match_keys: ["devices.yaml", "launch 参数", "integrated.launch"]
conflicts: ["跨版本配置加载方式可能变化"]
assertion_state: "historical"
authority: "B"
implementation_evidence: "document-only"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# 历史 Renew 的 devices.yaml 不是自动生效配置源 → trajectory_recorder

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/历史 Renew 的 devices.yaml 不是自动生效配置源|历史 Renew 的 devices.yaml 不是自动生效配置源]]
- 右侧代码实体：[[03_ROS/Packages/trajectory_recorder|trajectory_recorder]]
- 关系：`configuration_constraint`
- 匹配概率：**88%**
- 匹配状态：`needs-review`
- 实现证据：`document-only`

## 评分依据

- 配置文件路径和 launch 参数上下文命中；需在目标快照复核加载链。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 跨版本配置加载方式可能变化

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
