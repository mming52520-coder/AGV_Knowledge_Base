---
id: "agv:claim:renew-primary-integrated-launch"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:renew-primary-integrated-launch"
derived_from: "agv:source:ros:raspberry-pi-project-complete-reading"
source_locator: "UTF-8 行 63-75、703-709"
authority: "B"
assertion_state: "historical"
applies_to_snapshot: "historical-renew-2026-04"
technical_keys: ["Renew/src", "trajectory_recorder", "integrated.launch", "bringup"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "historical"]
---

# 历史 Renew 主入口为 integrated.launch

## 原子结论

该资料把 Renew 认定为当时主工程，并把 trajectory_recorder/integrated.launch 作为主入口；bringup 被标为早期入口。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/树莓派4B配置与项目资料完整解读|树莓派4B配置与项目资料完整解读]]
- 定位：UTF-8 行 63-75、703-709
- 来源权威级别：`B`

## 适用范围

- 事实状态：`historical`
- 适用快照：`historical-renew-2026-04`

## 证据与限制

这是历史资料，不覆盖三号车最新代码的 vehicle.launch 或新分层架构。

## 候选关系

- [[11_Engineering_Materials/Matches/M001-历史 Renew 主入口为 integrated.launch-trajectory_recorder|describes → trajectory_recorder]]
