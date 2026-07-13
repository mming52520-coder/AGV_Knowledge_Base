---
id: "agv:match:037"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:ten-axis-imu-output-protocol"
right_entity: "agv:ros:node:imu_probe"
target_snapshot: "code-v1"
relation: "reference_implementation_for"
match_score: 90
match_probability: 0.9
match_status: "accepted"
match_reasons: ["输出字段与诊断探针能力吻合。"]
match_keys: ["加速度", "角速度", "角度", "磁场", "GPS", "四元数", "校准"]
conflicts: []
assertion_state: "specified"
authority: "A"
implementation_evidence: "diagnostic-only"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "accepted"]
---

# 十轴 IMU 输出与配置寄存器范围 → imu_probe

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/十轴 IMU 输出与配置寄存器范围|十轴 IMU 输出与配置寄存器范围]]
- 右侧代码实体：[[03_ROS/Nodes/imu_probe|imu_probe]]
- 关系：`reference_implementation_for`
- 匹配概率：**90%**
- 匹配状态：`accepted`
- 实现证据：`diagnostic-only`

## 评分依据

- 输出字段与诊断探针能力吻合。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 无身份冲突。

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`accepted`
