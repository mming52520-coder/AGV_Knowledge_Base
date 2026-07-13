---
id: "agv:match:040"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:ten-axis-imu-output-protocol"
right_entity: "agv:ros:node:trajectory_tracker"
target_snapshot: "code-v1"
relation: "related_protocol"
match_score: 80
match_probability: 0.8
match_status: "needs-review"
match_reasons: ["历史 tracker 声称接入 IMU，但协议手册不能证明其生产数据所有权。"]
match_keys: ["加速度", "角速度", "角度", "磁场", "GPS", "四元数", "校准"]
conflicts: ["需要目标快照静态与运行复核"]
assertion_state: "specified"
authority: "A"
implementation_evidence: "document-only"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# 十轴 IMU 输出与配置寄存器范围 → trajectory_tracker

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/十轴 IMU 输出与配置寄存器范围|十轴 IMU 输出与配置寄存器范围]]
- 右侧代码实体：[[03_ROS/Nodes/trajectory_tracker|trajectory_tracker]]
- 关系：`related_protocol`
- 匹配概率：**80%**
- 匹配状态：`needs-review`
- 实现证据：`document-only`

## 评分依据

- 历史 tracker 声称接入 IMU，但协议手册不能证明其生产数据所有权。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 需要目标快照静态与运行复核

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
