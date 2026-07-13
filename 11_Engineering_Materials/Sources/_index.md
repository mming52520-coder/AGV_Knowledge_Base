---
id: "agv:index:material-sources"
type: "index"
status: "active"
review: "generated"
project: "AGV"
updated: "2026-07-14"
tags: ["AGV", "工程资料", "来源"]
---

# 工程资料来源

- [[11_Engineering_Materials/Collections/车辆学习资料]]
- [[11_Engineering_Materials/Collections/ROS工程文件]]

```dataview
TABLE source_collection AS 集合, source_kind AS 类型, extraction_status AS 抽取状态, authority AS 权威级别
FROM "11_Engineering_Materials/Sources"
WHERE type = "source_document"
SORT file.name ASC
```
