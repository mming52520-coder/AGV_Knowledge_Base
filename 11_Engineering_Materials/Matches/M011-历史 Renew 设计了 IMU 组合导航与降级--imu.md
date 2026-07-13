---
id: "agv:match:011"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:renew-imu-fusion-degradation"
right_entity: "agv:ros:interface:imu"
target_snapshot: "code-v1"
relation: "describes"
match_score: 86
match_probability: 0.86
match_status: "needs-review"
match_reasons: ["IMU 语义与接口类型相符，但历史指南没有证明当前 /imu 所有权。"]
match_keys: ["IMU", "encoder", "complementary", "encoder_only", "mag_heading"]
conflicts: ["生产话题所有者未由本资料确认"]
assertion_state: "historical"
authority: "B"
implementation_evidence: "documented-design"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# 历史 Renew 设计了 IMU 组合导航与降级 → /imu

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/历史 Renew 设计了 IMU 组合导航与降级|历史 Renew 设计了 IMU 组合导航与降级]]
- 右侧代码实体：[[03_ROS/Interfaces/imu|/imu]]
- 关系：`describes`
- 匹配概率：**86%**
- 匹配状态：`needs-review`
- 实现证据：`documented-design`

## 评分依据

- IMU 语义与接口类型相符，但历史指南没有证明当前 /imu 所有权。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 生产话题所有者未由本资料确认

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
