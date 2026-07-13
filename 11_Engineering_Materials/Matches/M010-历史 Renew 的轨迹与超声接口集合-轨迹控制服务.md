---
id: "agv:match:010"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:renew-legacy-ros-interfaces"
right_entity: "agv:ros:interface:trajectory-services"
target_snapshot: "code-v1"
relation: "describes"
match_score: 98
match_probability: 0.98
match_status: "accepted"
match_reasons: ["轨迹播放、停止和暂停服务模式命中。"]
match_keys: ["/odom", "/trajectory_status", "/ultrasonic/left_distance", "/trajectory/play", "/trajectory/stop"]
conflicts: []
assertion_state: "historical"
authority: "B"
implementation_evidence: "historical-document"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "accepted"]
---

# 历史 Renew 的轨迹与超声接口集合 → 轨迹控制服务

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/历史 Renew 的轨迹与超声接口集合|历史 Renew 的轨迹与超声接口集合]]
- 右侧代码实体：[[03_ROS/Interfaces/trajectory-services|轨迹控制服务]]
- 关系：`describes`
- 匹配概率：**98%**
- 匹配状态：`accepted`
- 实现证据：`historical-document`

## 评分依据

- 轨迹播放、停止和暂停服务模式命中。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 无身份冲突。

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`accepted`
