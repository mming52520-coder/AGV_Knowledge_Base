---
id: "agv:match:063"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:c10b-resource-allocation-reference"
right_entity: "agv:hardware:stm32-chassis"
target_snapshot: "code-v1"
relation: "reference"
match_score: 70
match_probability: 0.7
match_status: "needs-review"
match_reasons: ["资源表与 STM32 底盘外设类别相关，但板卡身份不同。"]
match_keys: ["TIM3", "UART1", "UART3", "UART4", "UART5", "ADC", "电磁巡线", "编码器"]
conflicts: ["C10B 引脚分配不是三号车线束证据"]
assertion_state: "reference"
authority: "A"
implementation_evidence: "reference-model-mismatch"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# C10B资源表把PWM-串口-ADC-编码器分配到固定MCU外设 → STM32底盘控制器

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/C10B资源表把PWM-串口-ADC-编码器分配到固定MCU外设|C10B资源表把PWM-串口-ADC-编码器分配到固定MCU外设]]
- 右侧代码实体：[[02_Hardware/STM32底盘控制器|STM32底盘控制器]]
- 关系：`reference`
- 匹配概率：**70%**
- 匹配状态：`needs-review`
- 实现证据：`reference-model-mismatch`

## 评分依据

- 资源表与 STM32 底盘外设类别相关，但板卡身份不同。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- C10B 引脚分配不是三号车线束证据

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
