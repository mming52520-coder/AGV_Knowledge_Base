---
id: "agv:index:graph-history"
type: "index"
status: "active"
review: "verified"
candidate_status: "candidate_pending_review"
candidate_review: "generated"
project: "AGV"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "快照", "差异"]
---

# 代码图谱版本与差异

## 当前指针

- 当前推荐：[[00_System/Graph_History/Snapshots/code-v1/V1基线说明|code-v1-e8a1b3d]]
- 待复核候选：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 对比：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/_index|V1 → V2 差异总览]]
- 指针说明：[[00_System/Graph_History/当前推荐快照|当前推荐快照]]

V1 保持不可变；V2 使用独立快照实例页，不覆盖现有 `03_ROS` 页面。

## 快照

```dataview
TABLE snapshot_id AS 快照, source_snapshot AS 源码哈希, status AS 状态
FROM "00_System/Graph_History/Snapshots"
WHERE type = "graph_snapshot"
SORT file.name ASC
```

## 差异

```dataview
TABLE baseline_snapshot AS 基线, target_snapshot AS 目标, change_kind AS 类型, review AS 复核
FROM "00_System/Graph_History/Changes"
WHERE type = "graph_change"
SORT file.name ASC
```

## 规范

- [[图谱快照与差异Schema]]
- [[../Decisions/ADR-002-代码图谱快照与增量差异]]

- [[../../研发图谱工作台|返回研发图谱工作台]]
