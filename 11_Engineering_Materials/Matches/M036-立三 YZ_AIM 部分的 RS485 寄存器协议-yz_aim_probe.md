---
id: "agv:match:036"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:yz-aim-register-protocol"
right_entity: "agv:ros:node:yz_aim_probe"
target_snapshot: "code-v1"
relation: "specifies_protocol_for"
match_score: 97
match_probability: 0.97
match_status: "accepted"
match_reasons: ["诊断节点名称和寄存器静态命中；V2 已移除该节点。"]
match_keys: ["115200", "0x009F", "0x00D4", "YZ_AIM"]
conflicts: []
assertion_state: "specified"
authority: "A"
implementation_evidence: "verified-static-historical"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "accepted"]
---

# 立三 YZ_AIM 部分的 RS485 寄存器协议 → yz_aim_probe

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/立三 YZ_AIM 部分的 RS485 寄存器协议|立三 YZ_AIM 部分的 RS485 寄存器协议]]
- 右侧代码实体：[[03_ROS/Nodes/yz_aim_probe|yz_aim_probe]]
- 关系：`specifies_protocol_for`
- 匹配概率：**97%**
- 匹配状态：`accepted`
- 实现证据：`verified-static-historical`

## 评分依据

- 诊断节点名称和寄存器静态命中；V2 已移除该节点。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 无身份冲突。

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`accepted`
