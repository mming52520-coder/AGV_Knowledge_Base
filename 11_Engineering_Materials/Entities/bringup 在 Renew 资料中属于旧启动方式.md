---
id: "agv:claim:bringup-historical-entry"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:bringup-historical-entry"
derived_from: "agv:source:ros:raspberry-pi-project-complete-reading"
source_locator: "UTF-8 行 68-75、703-709"
authority: "B"
assertion_state: "deprecated"
applies_to_snapshot: "historical-renew-2026-04"
technical_keys: ["bringup", "all_nodes.launch", "integrated.launch"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "deprecated"]
---

# bringup 在 Renew 资料中属于旧启动方式

## 原子结论

历史资料明确把 bringup/all_nodes.launch 归类为旧入口，并推荐 integrated.launch。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/树莓派4B配置与项目资料完整解读|树莓派4B配置与项目资料完整解读]]
- 定位：UTF-8 行 68-75、703-709
- 来源权威级别：`B`

## 适用范围

- 事实状态：`deprecated`
- 适用快照：`historical-renew-2026-04`

## 证据与限制

废弃状态只适用于该历史资料所述时期。

## 候选关系

- [[11_Engineering_Materials/Matches/M004-bringup 在 Renew 资料中属于旧启动方式-bringup|deprecates_in_context → bringup]]
