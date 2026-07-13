---
id: "agv:index:architecture-decisions"
type: index
status: active
review: verified
project: AGV
updated: 2026-07-14
tags: [AGV, ADR, 决策]
---

# 架构决策记录

```dataview
TABLE status AS 状态, date AS 日期
FROM "00_System/Decisions"
WHERE type = "decision" AND file.name != "_index"
SORT file.name ASC
```

## 当前决策

- [[ADR-001-工程资料与代码实体匹配]]
- [[ADR-002-代码图谱快照与增量差异]]

- [[../../研发图谱工作台|返回研发图谱工作台]]
