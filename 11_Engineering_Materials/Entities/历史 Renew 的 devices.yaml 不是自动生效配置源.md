---
id: "agv:claim:devices-yaml-not-authoritative"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:devices-yaml-not-authoritative"
derived_from: "agv:source:ros:raspberry-pi-project-complete-reading"
source_locator: "UTF-8 行 213-223、710-713"
authority: "B"
assertion_state: "historical"
applies_to_snapshot: "historical-renew-2026-04"
technical_keys: ["devices.yaml", "launch 参数", "integrated.launch"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "historical"]
---

# 历史 Renew 的 devices.yaml 不是自动生效配置源

## 原子结论

资料说明当时程序实际读取 launch 参数，而不是自动加载 devices.yaml。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/树莓派4B配置与项目资料完整解读|树莓派4B配置与项目资料完整解读]]
- 定位：UTF-8 行 213-223、710-713
- 来源权威级别：`B`

## 适用范围

- 事实状态：`historical`
- 适用快照：`historical-renew-2026-04`

## 证据与限制

必须在目标快照重新检查配置加载链，不能跨版本外推。

## 候选关系

- [[11_Engineering_Materials/Matches/M005-历史 Renew 的 devices.yaml 不是自动生效配置源-trajectory_recorder|configuration_constraint → trajectory_recorder]]
