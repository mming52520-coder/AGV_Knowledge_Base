---
id: "agv:match:016"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:ms16a-protocol-and-baud-constraint"
right_entity: "agv:ros:node:mag_sensor_reader"
target_snapshot: "code-v1"
relation: "configuration_constraint"
match_score: 99
match_probability: 0.99
match_status: "needs-review"
match_reasons: ["寄存器 0x0001 与静态代码吻合，但默认波特率不同。"]
match_keys: ["MS-16A", "16点", "RS485", "Modbus RTU", "0x0001", "9600"]
conflicts: ["手册默认9600，V1节点默认38400；需确认设备预配置"]
assertion_state: "specified"
authority: "A"
implementation_evidence: "verified-static-with-runtime-check"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# MS-16A 协议与默认波特率形成配置约束 → mag_sensor_reader

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/MS-16A 协议与默认波特率形成配置约束|MS-16A 协议与默认波特率形成配置约束]]
- 右侧代码实体：[[03_ROS/Nodes/mag_sensor_reader|mag_sensor_reader]]
- 关系：`configuration_constraint`
- 匹配概率：**99%**
- 匹配状态：`needs-review`
- 实现证据：`verified-static-with-runtime-check`

## 评分依据

- 寄存器 0x0001 与静态代码吻合，但默认波特率不同。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 手册默认9600，V1节点默认38400；需确认设备预配置

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
