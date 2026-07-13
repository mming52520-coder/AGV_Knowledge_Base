---
id: "agv:match:055"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:ros-driver-board-physical-interface"
right_entity: "agv:hardware:stm32-chassis"
target_snapshot: "code-v1"
relation: "documents_physical_interface_of"
match_score: 75
match_probability: 0.75
match_status: "needs-review"
match_reasons: ["同系列驱动板接口图与 STM32 底盘实体相关。"]
match_keys: ["Motor A-D", "JTAG", "OLED", "预留IO"]
conflicts: ["缺少三号车采购明细或铭牌确认"]
assertion_state: "reference"
authority: "B"
implementation_evidence: "hardware-confirmation-needed"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# ROS 驱动板接口图是 STM32 底盘候选物理证据 → STM32底盘控制器

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/ROS 驱动板接口图是 STM32 底盘候选物理证据|ROS 驱动板接口图是 STM32 底盘候选物理证据]]
- 右侧代码实体：[[02_Hardware/STM32底盘控制器|STM32底盘控制器]]
- 关系：`documents_physical_interface_of`
- 匹配概率：**75%**
- 匹配状态：`needs-review`
- 实现证据：`hardware-confirmation-needed`

## 评分依据

- 同系列驱动板接口图与 STM32 底盘实体相关。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 缺少三号车采购明细或铭牌确认

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
