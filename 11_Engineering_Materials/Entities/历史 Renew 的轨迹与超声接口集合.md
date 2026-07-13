---
id: "agv:claim:renew-legacy-ros-interfaces"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:renew-legacy-ros-interfaces"
derived_from: "agv:source:ros:renew-project-architecture"
source_locator: "UTF-8 行 189-204"
authority: "B"
assertion_state: "historical"
applies_to_snapshot: "historical-renew-2026-03"
technical_keys: ["/odom", "/trajectory_status", "/ultrasonic/left_distance", "/trajectory/play", "/trajectory/stop"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "historical"]
---

# 历史 Renew 的轨迹与超声接口集合

## 原子结论

资料登记了 /odom、/trajectory_status、四向超声距离及轨迹播放控制服务。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/Renew历史项目架构|Renew历史项目架构]]
- 定位：UTF-8 行 189-204
- 来源权威级别：`B`

## 适用范围

- 事实状态：`historical`
- 适用快照：`historical-renew-2026-03`

## 证据与限制

接口身份匹配概率高，但发布者、所有者和默认启动方式必须按 V2 重新验证。

## 候选关系

- [[11_Engineering_Materials/Matches/M007-历史 Renew 的轨迹与超声接口集合--odom|describes → /odom]]
- [[11_Engineering_Materials/Matches/M008-历史 Renew 的轨迹与超声接口集合--trajectory_status|describes → /trajectory_status]]
- [[11_Engineering_Materials/Matches/M009-历史 Renew 的轨迹与超声接口集合-超声距离话题|describes → 超声距离话题]]
- [[11_Engineering_Materials/Matches/M010-历史 Renew 的轨迹与超声接口集合-轨迹控制服务|describes → 轨迹控制服务]]
