---
id: "agv:system:graph-history-schema"
type: standard
status: active
review: verified
project: AGV
updated: 2026-07-14
tags: [AGV, Schema, 代码图谱, 版本]
---

# 图谱快照与差异 Schema

## 快照最小字段

```yaml
id: "agv:graph-snapshot:<snapshot_id>"
type: graph_snapshot
snapshot_id:
graph_version:
status: active
review: generated
vault_baseline_commit:
graph_schema_version:
extractor_version:
scope_id:
source_snapshot:
entities_fingerprint:
relations_fingerprint:
created:
```

## 差异最小字段

```yaml
id: "agv:graph-change:<baseline>__<target>:<entity_uid>"
type: graph_change
baseline_snapshot:
target_snapshot:
entity_uid:
change_kind:
before_fingerprint:
after_fingerprint:
changed_fields: []
breaking: false
match_method:
match_confidence:
review: generated
```

## 规范化规则

- 相对路径统一使用 `/`，不把盘符和文件修改时间写入身份哈希。
- 实体、关系和字段按稳定键排序后再计算 SHA-256。
- 空数组与缺失字段按 Schema 固定规则规范化。
- 关系键为 `(from_entity_uid, predicate, to_entity_uid, qualifiers)`。
- 扫描范围变化单列为 `scope_change`，不能误报成代码删除。

## 数量守恒

```text
V1 实体数 = matched + removed
V2 实体数 = matched + added
matched = unchanged + semantic_changed
renamed ⊆ matched
```

## 关联

- [[_index]]
- [[../Decisions/ADR-002-代码图谱快照与增量差异]]
