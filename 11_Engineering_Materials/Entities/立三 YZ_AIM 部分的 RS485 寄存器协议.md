---
id: "agv:claim:yz-aim-register-protocol"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:yz-aim-register-protocol"
derived_from: "agv:source:ros:yz-aim-rs485-manual"
source_locator: "运行模式与使能/重启寄存器章节"
authority: "A"
assertion_state: "specified"
applies_to_snapshot: "vendor-yz-aim-rs485-manual"
technical_keys: ["115200", "0x009F", "0x00D4", "YZ_AIM"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "specified"]
---

# 立三 YZ_AIM 部分的 RS485 寄存器协议

## 原子结论

手册的默认 115200、运行模式 0x009F 与使能/重启 0x00D4 和 V1 YZ_AIM 后端静态代码吻合。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/立三485步进驱动通讯手册|立三485步进驱动通讯手册]]
- 定位：运行模式与使能/重启寄存器章节
- 来源权威级别：`A`

## 适用范围

- 事实状态：`specified`
- 适用快照：`vendor-yz-aim-rs485-manual`

## 证据与限制

组合硬件实体还包含 OID；本结论不得映射到 OID 的 5000/6000 段寄存器。

## 候选关系

- [[11_Engineering_Materials/Matches/M033-立三 YZ_AIM 部分的 RS485 寄存器协议-OID与YZ_AIM电机控制器|specifies_component_of → OID与YZ_AIM电机控制器]]
- [[11_Engineering_Materials/Matches/M034-立三 YZ_AIM 部分的 RS485 寄存器协议-chassis_bridge|specifies_protocol_for → chassis_bridge]]
- [[11_Engineering_Materials/Matches/M035-立三 YZ_AIM 部分的 RS485 寄存器协议-steering_remote|specifies_protocol_for → steering_remote]]
- [[11_Engineering_Materials/Matches/M036-立三 YZ_AIM 部分的 RS485 寄存器协议-yz_aim_probe|specifies_protocol_for → yz_aim_probe]]
