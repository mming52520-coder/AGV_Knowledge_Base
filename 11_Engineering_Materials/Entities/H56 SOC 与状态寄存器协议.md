---
id: "agv:claim:h56-modbus-soc-status-protocol"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:h56-modbus-soc-status-protocol"
derived_from: "agv:source:ros:h56-coulomb-protocol"
source_locator: "第 1-2 节及输入寄存器表（0x00、0x1D、0x1E）"
authority: "A"
assertion_state: "specified"
applies_to_snapshot: "vendor-protocol-h56-v3.0"
technical_keys: ["H56", "03", "04", "06", "10", "9600", "SOC*0.1", "0x1D", "0x1E"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "specified"]
---

# H56 SOC 与状态寄存器协议

## 原子结论

协议规定 Modbus RTU 功能码、默认 9600、SOC 0.1% 缩放及报警/充放电状态寄存器；V1 静态实现匹配。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/H56库仑计串口通讯协议V3.0|H56库仑计串口通讯协议V3.0]]
- 定位：第 1-2 节及输入寄存器表（0x00、0x1D、0x1E）
- 来源权威级别：`A`

## 适用范围

- 事实状态：`specified`
- 适用快照：`vendor-protocol-h56-v3.0`

## 证据与限制

协议含置满、清零等维护写命令，知识图谱不得自动执行。

## 候选关系

- [[11_Engineering_Materials/Matches/M022-H56 SOC 与状态寄存器协议-H56BR电池表|specifies → H56BR电池表]]
- [[11_Engineering_Materials/Matches/M023-H56 SOC 与状态寄存器协议-h56br_node|specifies_protocol_for → h56br_node]]
- [[11_Engineering_Materials/Matches/M024-H56 SOC 与状态寄存器协议--battery-h56br-status|specifies_payload_for → /battery/h56br/status]]
- [[11_Engineering_Materials/Matches/M025-H56 SOC 与状态寄存器协议--battery-h56br-soc|specifies_payload_for → /battery/h56br/soc]]
