---
id: "agv:index:engineering-materials"
type: index
status: active
review: verified
project: AGV
updated: 2026-07-14
tags: [AGV, 工程资料, 证据, 匹配]
---

# 工程资料与匹配工作台

## 资料来源

```dataview
TABLE source_kind AS 类型, extraction_status AS 抽取状态, authority AS 权威级别
FROM "11_Engineering_Materials/Sources"
WHERE type = "source_document"
SORT file.name ASC
```

## 工程结论

```dataview
TABLE assertion_state AS 事实状态, authority AS 权威级别, review AS 复核
FROM "11_Engineering_Materials/Entities"
WHERE type = "engineering_claim"
SORT file.name ASC
```

## 待复核匹配

```dataview
TABLE relation AS 关系, match_score AS 分数, match_status AS 状态
FROM "11_Engineering_Materials/Matches"
WHERE type = "match_record" AND match_status != "accepted"
SORT match_score DESC
```

## 规则

- [[../00_System/Decisions/ADR-001-工程资料与代码实体匹配]]
- 只保存资料摘要、定位和哈希，不复制大型原文件。
- 资料匹配概率与事实是否实现必须分开判断。

- [[../研发图谱工作台|返回研发图谱工作台]]
