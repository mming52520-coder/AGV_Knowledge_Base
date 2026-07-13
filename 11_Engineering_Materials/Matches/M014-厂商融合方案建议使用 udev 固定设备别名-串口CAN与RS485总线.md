---
id: "agv:match:014"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:udev-stable-device-aliases"
right_entity: "agv:hardware:serial-can-rs485"
target_snapshot: "code-v1"
relation: "proposes"
match_score: 82
match_probability: 0.82
match_status: "needs-review"
match_reasons: ["设备总线与稳定串口别名语义匹配；未确认规则已部署。"]
match_keys: ["udev", "/dev/agv_*", "CP2102", "CH340", "ttyACM"]
conflicts: []
assertion_state: "planned"
authority: "B"
implementation_evidence: "planned-only"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# 厂商融合方案建议使用 udev 固定设备别名 → 串口CAN与RS485总线

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/厂商融合方案建议使用 udev 固定设备别名|厂商融合方案建议使用 udev 固定设备别名]]
- 右侧代码实体：[[02_Hardware/串口CAN与RS485总线|串口CAN与RS485总线]]
- 关系：`proposes`
- 匹配概率：**82%**
- 匹配状态：`needs-review`
- 实现证据：`planned-only`

## 评分依据

- 设备总线与稳定串口别名语义匹配；未确认规则已部署。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 无身份冲突。

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
