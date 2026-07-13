---
id: "agv:claim:renew-imu-fusion-degradation"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:renew-imu-fusion-degradation"
derived_from: "agv:source:ros:renew-imu-integration-guide"
source_locator: "UTF-8 行 40-42、187-202、251-258"
authority: "B"
assertion_state: "historical"
applies_to_snapshot: "historical-renew-2026-03"
technical_keys: ["IMU", "encoder", "complementary", "encoder_only", "mag_heading"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "historical"]
---

# 历史 Renew 设计了 IMU 组合导航与降级

## 原子结论

文档把 IMU 与编码器用于航向和状态融合，并描述磁力计或 IMU 不可用时的降级。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/YB-MRA02十轴IMU集成技术文档|YB-MRA02十轴IMU集成技术文档]]
- 定位：UTF-8 行 40-42、187-202、251-258
- 来源权威级别：`B`

## 适用范围

- 事实状态：`historical`
- 适用快照：`historical-renew-2026-03`

## 证据与限制

这是设计与自述验证结果，本轮未独立运行代码或实车测试。

## 候选关系

- [[11_Engineering_Materials/Matches/M011-历史 Renew 设计了 IMU 组合导航与降级--imu|describes → /imu]]
- [[11_Engineering_Materials/Matches/M012-历史 Renew 设计了 IMU 组合导航与降级-trajectory_tracker|describes → trajectory_tracker]]
