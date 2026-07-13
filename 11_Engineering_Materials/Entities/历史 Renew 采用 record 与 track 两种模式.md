---
id: "agv:claim:renew-record-track-modes"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:renew-record-track-modes"
derived_from: "agv:source:ros:renew-project-architecture"
source_locator: "UTF-8 行 134-165"
authority: "B"
assertion_state: "historical"
applies_to_snapshot: "historical-renew-2026-03"
technical_keys: ["trajectory_recorder", "trajectory_tracker", "record", "track"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "historical"]
---

# 历史 Renew 采用 record 与 track 两种模式

## 原子结论

录制模式启动 trajectory_recorder，跟踪模式启动 trajectory_tracker；二者由 integrated.launch 的 mode 参数选择。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/Renew历史项目架构|Renew历史项目架构]]
- 定位：UTF-8 行 134-165
- 来源权威级别：`B`

## 适用范围

- 事实状态：`historical`
- 适用快照：`historical-renew-2026-03`

## 证据与限制

只描述 Renew 历史实现，不代表 V2 新分层节点的运行模式。

## 候选关系

- [[11_Engineering_Materials/Matches/M002-历史 Renew 采用 record 与 track 两种模式-trajectory_recorder|describes → trajectory_recorder]]
- [[11_Engineering_Materials/Matches/M003-历史 Renew 采用 record 与 track 两种模式-trajectory_tracker|describes → trajectory_tracker]]
