---
id: "agv:match:051"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:stm32-chassis-serial-framing"
right_entity: "agv:hardware:stm32-chassis"
target_snapshot: "code-v1"
relation: "specifies"
match_score: 100
match_probability: 1.0
match_status: "accepted"
match_reasons: ["STM32 运动底盘型号域精确命中。"]
match_keys: ["115200", "24字节", "0x7B", "0x7D", "BCC XOR", "速度", "IMU", "电池"]
conflicts: []
assertion_state: "specified"
authority: "A"
implementation_evidence: "vendor-specification"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "accepted"]
---

# WHEELTEC STM32 底盘串口帧与 V1 静态实现吻合 → STM32底盘控制器

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/WHEELTEC STM32 底盘串口帧与 V1 静态实现吻合|WHEELTEC STM32 底盘串口帧与 V1 静态实现吻合]]
- 右侧代码实体：[[02_Hardware/STM32底盘控制器|STM32底盘控制器]]
- 关系：`specifies`
- 匹配概率：**100%**
- 匹配状态：`accepted`
- 实现证据：`vendor-specification`

## 评分依据

- STM32 运动底盘型号域精确命中。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 无身份冲突。

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`accepted`
