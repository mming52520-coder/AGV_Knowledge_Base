---
id: "agv:index:graph-history"
type: index
status: active
review: verified
project: AGV
updated: 2026-07-14
tags: [AGV, 代码图谱, 快照, 差异]
---

# 代码图谱版本与差异

## 当前状态

- 当前推荐快照：`code-v1`
- V1 Git 提交：`e8a1b3d`
- V1 Git 标签：`kg-code-v1-e8a1b3d`
- V1 原页面：保持不可变

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
