---
id: "agv:match:065"
type: "match_record"
status: "active"
review: "generated"
project: "AGV"
left_entity: "agv:claim:legacy-autostart-note-security-boundary"
right_entity: "agv:ros:package:bringup"
target_snapshot: "code-v1"
relation: "reference"
match_score: 55
match_probability: 0.55
match_status: "needs-review"
match_reasons: ["旧式主机启动流程与 bringup 部署语义弱相关。"]
match_keys: ["NFS", "rc.local", "开机自启动", "宽松权限"]
conflicts: ["未确认三号车使用 NFS、rc.local 或该权限设置"]
assertion_state: "reference"
authority: "C"
implementation_evidence: "legacy-reference-only"
updated: "2026-07-14"
tags: ["AGV", "图谱匹配", "needs-review"]
---

# 旧式NFS与rc.local自启动笔记只作部署风险参考 → bringup

## 匹配结论

- 左侧工程结论：[[11_Engineering_Materials/Entities/旧式NFS与rc.local自启动笔记只作部署风险参考|旧式NFS与rc.local自启动笔记只作部署风险参考]]
- 右侧代码实体：[[03_ROS/Packages/bringup|bringup]]
- 关系：`reference`
- 匹配概率：**55%**
- 匹配状态：`needs-review`
- 实现证据：`legacy-reference-only`

## 评分依据

- 旧式主机启动流程与 bringup 部署语义弱相关。

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

- 未确认三号车使用 NFS、rc.local 或该权限设置

## 复核记录

- 生成日期：2026-07-14
- 当前结论：`needs-review`
