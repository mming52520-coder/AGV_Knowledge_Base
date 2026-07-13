---
id: "agv:match:057"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:c10b-reference-platform-serial-control"
right_entity: "agv:ros:node:wheeltec_robot_node"
target_snapshot: "code-v1"
relation: "reference"
match_score: 88
match_probability: 0.88
match_status: "needs-review"
match_reasons: ["115200、24字节、0x7B/0x7D 等字段高度相似，只支持参考协议关联。"]
match_keys: ["C10B", "L150", "115200", "24字节", "0x7B", "0x7D", "电磁巡线", "Ackermann"]
conflicts: ["协议相似不证明 C10B 固件或板卡被当前车辆采用"]
assertion_state: "reference"
authority: "A"
implementation_evidence: "reference-model-mismatch"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# C10B-L150参考平台定义底盘串口与巡线控制链 → wheeltec_robot_node

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/C10B-L150参考平台定义底盘串口与巡线控制链|C10B-L150参考平台定义底盘串口与巡线控制链]]
- 右侧代码实体：[[03_ROS/Nodes/wheeltec_robot_node|wheeltec_robot_node]]
- 关系：`reference`
- 匹配概率：**88%**
- 匹配状态：`needs-review`
- 实现证据：`reference-model-mismatch`

## 评分依据

- 115200、24字节、0x7B/0x7D 等字段高度相似，只支持参考协议关联。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 协议相似不证明 C10B 固件或板卡被当前车辆采用

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
