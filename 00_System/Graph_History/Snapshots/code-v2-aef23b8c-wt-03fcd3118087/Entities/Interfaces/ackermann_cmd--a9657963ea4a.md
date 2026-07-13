---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:ackermann-cmd"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:interface:ackermann-cmd"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:ackermann-cmd"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_interface"
title: "/ackermann_cmd"
status: "compatibility"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "3a3fc0eb51e3ce08b1afe9872424196362c96b7b0f9db7a697fb833304d23294"
relation_fingerprint: "e230a7fa7565def94a7aadb911e2ea49b488264ce081546a6c22ffcf1960ee9b"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# /ackermann_cmd

- 逻辑实体：`agv:ros:interface:ackermann-cmd`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:interface:ackermann-cmd`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/_index|Interfaces]]
- 代码证据主路径：`src/odometer/src/odometer.cpp`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` | topic |
| `message_type` | unknown |
| `ros_name` | /ackermann_cmd |
| `status` | compatibility |
| `type` | ros_interface |
| `vehicles` | ["三号车"] |
| `version` |  |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/odometer/src/odometer.cpp` | 150 | `subscribes` | `f1a235cae5e0fa57a303bd0b2853cf7498f75249ece10e5749a43b69210c8bb6` |

## 出向关系

- `related_packages` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/odometer--6b13553e3c5a|agv:ros:package:odometer]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/odometer--4d91289aece7|agv:ros:node:odometer]] → `subscribes`

## 相对 V1 的变化

- 变化类型：`added`
- 变化字段：无
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Added/ackermann-cmd--a9657963ea4a|agv:ros:interface:ackermann-cmd]]
