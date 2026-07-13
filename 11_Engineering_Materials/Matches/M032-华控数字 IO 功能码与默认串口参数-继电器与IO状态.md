---
id: "agv:match:032"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:huakong-digital-io-protocol"
right_entity: "agv:ros:interface:relay-io-status"
target_snapshot: "code-v1"
relation: "specifies_payload_for"
match_score: 98
match_probability: 0.98
match_status: "needs-review"
match_reasons: ["输入与继电器状态语义吻合；V1 launch 包名问题仍需复核。"]
match_keys: ["1-48路", "38400", "01", "02", "05", "线圈0", "离散输入0"]
conflicts: ["V1已知launch包名不一致"]
assertion_state: "specified"
authority: "A"
implementation_evidence: "verified-static-with-launch-review"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# 华控数字 IO 功能码与默认串口参数 → 继电器与IO状态

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/华控数字 IO 功能码与默认串口参数|华控数字 IO 功能码与默认串口参数]]
- 右侧代码实体：[[03_ROS/Interfaces/relay-io-status|继电器与IO状态]]
- 关系：`specifies_payload_for`
- 匹配概率：**98%**
- 匹配状态：`needs-review`
- 实现证据：`verified-static-with-launch-review`

## 评分依据

- 输入与继电器状态语义吻合；V1 launch 包名问题仍需复核。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- V1已知launch包名不一致

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
