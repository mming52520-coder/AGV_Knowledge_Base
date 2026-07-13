---
id: "agv:claim:legacy-autostart-note-security-boundary"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:legacy-autostart-note-security-boundary"
derived_from: "agv:source:ros:legacy-ros-host-autostart"
source_locator: "UTF-8 全文（网络和路径值已排除）"
authority: "C"
assertion_state: "reference"
applies_to_snapshot: "legacy-reference-deployment-note"
technical_keys: ["NFS", "rc.local", "开机自启动", "宽松权限"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "reference"]
---

# 旧式NFS与rc.local自启动笔记只作部署风险参考

## 原子结论

笔记采用旧式 NFS 挂载和 rc.local 启动流程，并包含不宜复用的宽松权限做法。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/ROS主机旧式开机自启动说明|ROS主机旧式开机自启动说明]]
- 定位：UTF-8 全文（网络和路径值已排除）
- 来源权威级别：`C`

## 适用范围

- 事实状态：`reference`
- 适用快照：`legacy-reference-deployment-note`

## 证据与限制

不保存网络地址、用户名或路径值；不执行命令，不把旧式做法视为三号车当前部署。

## 候选关系

- [[11_Engineering_Materials/Matches/M065-旧式NFS与rc.local自启动笔记只作部署风险参考-bringup|reference → bringup]]
