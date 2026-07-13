---
id: "agv:index:material-claims"
type: "index"
status: "active"
review: "generated"
project: "AGV"
updated: "2026-07-14"
tags: ["AGV", "工程结论"]
---

# 工程结论

```dataview
TABLE assertion_state AS 事实状态, authority AS 权威级别, applies_to_snapshot AS 适用快照
FROM "11_Engineering_Materials/Entities"
WHERE type = "engineering_claim"
SORT assertion_state ASC, file.name ASC
```
