---
id: "agv:claim:renew-monolithic-tracker-drivers"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:renew-monolithic-tracker-drivers"
derived_from: "agv:source:ros:renew-project-architecture"
source_locator: "UTF-8 行 58-99、161-178"
authority: "B"
assertion_state: "historical"
applies_to_snapshot: "historical-renew-2026-03"
technical_keys: ["trajectory_tracker", "Encoder", "MagSensor", "RelayController", "SteeringMotor"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "historical"]
---

# 历史 trajectory_tracker 内联多类硬件驱动

## 原子结论

历史架构把编码器、磁传感器、驱动电机、转向电机和继电器等能力集中在 trajectory_tracker 及共享驱动类中。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/Renew历史项目架构|Renew历史项目架构]]
- 定位：UTF-8 行 58-99、161-178
- 来源权威级别：`B`

## 适用范围

- 事实状态：`historical`
- 适用快照：`historical-renew-2026-03`

## 证据与限制

最新代码已出现拆分趋势，不能据此覆盖 V2 实体。

## 候选关系

- [[11_Engineering_Materials/Matches/M006-历史 trajectory_tracker 内联多类硬件驱动-trajectory_recorder|describes → trajectory_recorder]]
