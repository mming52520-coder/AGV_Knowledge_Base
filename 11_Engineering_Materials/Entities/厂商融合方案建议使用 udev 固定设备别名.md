---
id: "agv:claim:udev-stable-device-aliases"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:udev-stable-device-aliases"
derived_from: "agv:source:ros:renew-vendor-fusion-plan"
source_locator: "UTF-8 行 19-25、36-68"
authority: "B"
assertion_state: "planned"
applies_to_snapshot: "historical-renew-2026-04"
technical_keys: ["udev", "/dev/agv_*", "CP2102", "CH340", "ttyACM"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "planned"]
---

# 厂商融合方案建议使用 udev 固定设备别名

## 原子结论

方案建议以 udev 规则创建稳定设备别名，再通过 launch 参数引用。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/Renew厂商资料融合方案|Renew厂商资料融合方案]]
- 定位：UTF-8 行 19-25、36-68
- 来源权威级别：`B`

## 适用范围

- 事实状态：`planned`
- 适用快照：`historical-renew-2026-04`

## 证据与限制

规划性内容；未把规则是否部署标记为已实现。

## 候选关系

- [[11_Engineering_Materials/Matches/M014-厂商融合方案建议使用 udev 固定设备别名-串口CAN与RS485总线|proposes → 串口CAN与RS485总线]]
