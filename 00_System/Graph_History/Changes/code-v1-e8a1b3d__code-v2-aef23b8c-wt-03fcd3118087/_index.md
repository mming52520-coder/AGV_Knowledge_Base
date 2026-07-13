---
id: "agv:graph-diff:code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087"
type: "graph_diff"
baseline_snapshot: "code-v1-e8a1b3d"
target_snapshot: "code-v2-aef23b8c-wt-03fcd3118087"
status: "candidate"
review: "generated"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V1-V2差异"]
---

# V1 → V2 差异总览

- V1：[[00_System/Graph_History/Snapshots/code-v1/V1基线说明|code-v1-e8a1b3d]]
- V2：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]

## 数量守恒

| 范围 | 基线 | 匹配 | 新增 | 修改 | 未变化 | 未匹配 | 目标 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 实体 | 62 | 49 | 143 | 33 | 16 | 13 | 192 |

| 关系 | V1 | 新增 | 未匹配 | V2 |
|---|---:|---:|---:|---:|
| 语义关系 | 171 | 379 | 54 | 496 |

## 导航

- [[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/实体差异|实体差异]]
- [[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/关系差异|关系差异]]
- [[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/迁移与分解|迁移与分解]]
- [[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/风险与复核|风险与复核]]
- [[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/V1→V2架构演化|V1 → V2 架构演化 Canvas]]

## 比较限制

- **`unchanged-graph-semantics-not-source-code`**：Entity unchanged compares only declared graph semantic fields (identity/status/ROS name/executable/interface kind/message type/version/vehicles). It does not prove unchanged implementation or configuration source; V1 has no per-file manifest and its hashes are graph-page provenance.
- **`cross-extractor-relation-drift`**：V1 relations use codex-v1-export-1 while V2 uses codex-v2-staging-1; relation deltas can reflect extractor coverage/schema drift as well as architecture changes.

> [!important] 未匹配不等于删除
> V1 只有来源集聚合哈希，没有逐文件清单。`removed` 仅表示 V2 当前扫描未匹配到同一逻辑实体，V1 页面继续保留。
