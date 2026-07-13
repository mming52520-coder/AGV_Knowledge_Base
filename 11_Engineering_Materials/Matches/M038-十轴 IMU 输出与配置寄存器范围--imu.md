---
id: "agv:match:038"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:ten-axis-imu-output-protocol"
right_entity: "agv:ros:interface:imu"
target_snapshot: "code-v1"
relation: "specifies_payload_for"
match_score: 86
match_probability: 0.86
match_status: "needs-review"
match_reasons: ["消息语义吻合，但厂商参考话题与 V1 /imu 不完全一致。"]
match_keys: ["加速度", "角速度", "角度", "磁场", "GPS", "四元数", "校准"]
conflicts: ["参考实现常用/imu/data，V1实体为/imu"]
assertion_state: "specified"
authority: "A"
implementation_evidence: "reference-topic-mismatch"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# 十轴 IMU 输出与配置寄存器范围 → /imu

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/十轴 IMU 输出与配置寄存器范围|十轴 IMU 输出与配置寄存器范围]]
- 右侧代码实体：[[03_ROS/Interfaces/imu|/imu]]
- 关系：`specifies_payload_for`
- 匹配概率：**86%**
- 匹配状态：`needs-review`
- 实现证据：`reference-topic-mismatch`

## 评分依据

- 消息语义吻合，但厂商参考话题与 V1 /imu 不完全一致。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 参考实现常用/imu/data，V1实体为/imu

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
