---
id: "agv:index:engineering-materials"
type: "index"
status: "active"
review: "verified"
project: "AGV"
updated: "2026-07-14"
tags: ["AGV", "工程资料", "证据", "匹配"]
---

# 工程资料与匹配工作台

本图谱把外部资料保留为独立证据层，不覆盖代码图谱。当前已登记 **52** 个规范来源、**34** 条原子工程结论和 **65** 条带概率的资料→代码匹配。

## 快速入口

- [[11_Engineering_Materials/Collections/车辆学习资料]]
- [[11_Engineering_Materials/Collections/ROS工程文件]]
- [[11_Engineering_Materials/Sources/_index|来源目录]]
- [[11_Engineering_Materials/Entities/_index|工程结论目录]]
- [[11_Engineering_Materials/Matches/_index|匹配记录目录]]
- [[11_Engineering_Materials/工程资料匹配概览.canvas|工程资料匹配概览]]

## 待复核匹配

```dataview
TABLE relation AS 关系, match_score AS 概率, implementation_evidence AS 实现证据, conflicts AS 冲突
FROM "11_Engineering_Materials/Matches"
WHERE type = "match_record" AND match_status != "accepted"
SORT match_score DESC
```

## 规则

- [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]
- 只保存资料摘要、定位和哈希，不复制大型原文件。
- 匹配概率与“是否已经实现”分开判断。
- `planned` 和 `reference` 只能建立提案或理论关系。
- V1 不被覆盖；V2 作为独立快照与 V1 比较。

- [[研发图谱工作台|返回研发图谱工作台]]
