---
id: "agv:graph-change:code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087:agv:ros:interface:hardware-probe-topics"
type: "graph_change"
baseline_snapshot: "code-v1-e8a1b3d"
target_snapshot: "code-v2-aef23b8c-wt-03fcd3118087"
logical_entity_uid: "agv:ros:interface:hardware-probe-topics"
change_kind: "removed_with_migration"
before_fingerprint: "78b687e0e3608eba2f4dcbe12c4749de8d914d153c595806347b7812892ec7c5"
after_fingerprint: ""
changed_fields: []
breaking: false
match_method: "baseline_only"
match_confidence: 1.0
review: "generated"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V1-V2差异", "removed_with_migration"]
---

# removed_with_migration: /imu/probe_* + /encoder_probe/* + ~yz_aim_probe/*

- 逻辑实体：`agv:ros:interface:hardware-probe-topics`
- 差异索引：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/_index|V1 → V2 差异总览]]
- 匹配方法：`baseline_only`
- 匹配置信度：`1.0`
- 潜在破坏性：`false`

## 版本实例

- V1 原始节点：[[03_ROS/Interfaces/hardware-probe-topics|/imu/probe_* + /encoder_probe/* + ~yz_aim_probe/*]]
- V1 实例 ID：`code-v1-e8a1b3d::agv:ros:interface:hardware-probe-topics`
- V2：本次快照未抽取到该逻辑实体；这不是删除 V1 页面。

## 字段差异

- 变化字段：无逐字段变化记录
- 变更前指纹：`78b687e0e3608eba2f4dcbe12c4749de8d914d153c595806347b7812892ec7c5`
- 变更后指纹：``

> [!warning] 复核要求
> V1 没有逐文件清单，因此这里只能判定“V1 有、V2 当前扫描未匹配”；不能据此断言源码已删除。
