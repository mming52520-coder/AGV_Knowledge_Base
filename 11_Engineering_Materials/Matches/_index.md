---
id: "agv:index:material-matches"
type: "index"
status: "active"
review: "generated"
project: "AGV"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配"]
---

# 资料到代码的匹配记录

匹配概率描述实体身份或关系命中的概率；`implementation_evidence` 单独表示是否存在实现证据。

```dataview
TABLE relation AS 关系, match_score AS 匹配概率, match_status AS 状态, implementation_evidence AS 实现证据
FROM "11_Engineering_Materials/Matches"
WHERE type = "match_record"
SORT match_score DESC, file.name ASC
```
