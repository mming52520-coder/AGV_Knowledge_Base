---
id: "agv:claim:ten-axis-imu-output-protocol"
type: "engineering_claim"
status: "active"
review: "generated"
project: "AGV"
claim_id: "agv:claim:ten-axis-imu-output-protocol"
derived_from: "agv:source:ros:ten-axis-imu-protocol"
source_locator: "输出数据与配置寄存器章节"
authority: "A"
assertion_state: "specified"
applies_to_snapshot: "vendor-ten-axis-imu-protocol"
technical_keys: ["加速度", "角速度", "角度", "磁场", "GPS", "四元数", "校准"]
updated: "2026-07-14"
tags: ["AGV", "工程结论", "specified"]
---

# 十轴 IMU 输出与配置寄存器范围

## 原子结论

协议覆盖惯性、磁场、定位与四元数输出以及校准、输出率和波特率配置。

## 来源定位

- 来源：[[11_Engineering_Materials/Sources/ROS_Project/十轴IMU模块通讯协议|十轴IMU模块通讯协议]]
- 定位：输出数据与配置寄存器章节
- 来源权威级别：`A`

## 适用范围

- 事实状态：`specified`
- 适用快照：`vendor-ten-axis-imu-protocol`

## 证据与限制

V1 imu_probe 是诊断节点，不能据手册推断其为生产 /imu 的唯一权威源。

## 候选关系

- [[11_Engineering_Materials/Matches/M037-十轴 IMU 输出与配置寄存器范围-imu_probe|reference_implementation_for → imu_probe]]
- [[11_Engineering_Materials/Matches/M038-十轴 IMU 输出与配置寄存器范围--imu|specifies_payload_for → /imu]]
- [[11_Engineering_Materials/Matches/M039-十轴 IMU 输出与配置寄存器范围-硬件探针话题|specifies_payload_for → 硬件探针话题]]
- [[11_Engineering_Materials/Matches/M040-十轴 IMU 输出与配置寄存器范围-trajectory_tracker|related_protocol → trajectory_tracker]]
