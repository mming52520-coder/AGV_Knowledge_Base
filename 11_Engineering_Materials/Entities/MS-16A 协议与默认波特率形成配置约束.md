---
id: "agv:claim:ms16a-protocol-and-baud-constraint"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:ms16a-protocol-and-baud-constraint"
derived_from: "agv:source:ros:ms16a-modbus-manual"
source_locator: "PDF 第 4-9 页"
authority: "A"
assertion_state: "specified"
applies_to_snapshot: "vendor-manual-v1.5.19.1"
technical_keys: ["MS-16A", "16点", "RS485", "Modbus RTU", "0x0001", "9600"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "specified"]
---

# MS-16A 协议与默认波特率形成配置约束

## 原子结论

手册规定 16 点磁检测、RS485 Modbus RTU、数据寄存器 0x0001 和出厂默认 9600；V1 静态代码的寄存器一致，但默认波特率为 38400。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/MS-16A磁导航传感器Modbus说明书|MS-16A磁导航传感器Modbus说明书]]
- 定位：PDF 第 4-9 页
- 来源权威级别：`A`

## 适用范围

- 事实状态：`specified`
- 适用快照：`vendor-manual-v1.5.19.1`

## 证据与限制

需要确认实装传感器是否预先改为 38400；不能直接判定代码缺陷。

## 候选关系

- [[11_Engineering_Materials/Matches/M015-MS-16A 协议与默认波特率形成配置约束-MS16A磁传感器|specifies → MS16A磁传感器]]
- [[11_Engineering_Materials/Matches/M016-MS-16A 协议与默认波特率形成配置约束-mag_sensor_reader|configuration_constraint → mag_sensor_reader]]
- [[11_Engineering_Materials/Matches/M017-MS-16A 协议与默认波特率形成配置约束--mag_sensor-raw_data|specifies_protocol_for → /mag_sensor/raw_data]]
