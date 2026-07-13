"""Generate the curated engineering-material graph for the AGV Obsidian vault.

The generator reads source metadata and hashes only. It never copies source
documents into the vault. Curated statements below are short, original
summaries with locators, not excerpts.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Any


UPDATED = "2026-07-14"
LEARNING_ROOT = Path(r"D:\推料车项目\9.车辆学习资料")
ROS_INVENTORY_ROOT = Path(r"D:\ROS工程文件")
ROS_ROOT = ROS_INVENTORY_ROOT / "推料车项目树莓派移植"


LEARNING_SPECS = [
    ("quadrotor-robust-nonlinear-control", "四旋翼非线性鲁棒控制", "Advanced Robust Nonlinear Control"),
    ("python-deep-learning-smart-car", "Python深度学习及智能车竞赛实践", "Python深度学习及智能车竞赛实践"),
    ("mechatronic-system-design", "机电一体化系统设计", "机电一体化系统设计"),
    ("mechanical-control-foundations", "机械控制工程基础", "机械控制工程基础"),
    ("mechanical-design-robert-norton", "机械设计（Robert Norton）", "机械设计 (（美）罗伯特·诺顿"),
    ("mechanical-design-foundations", "机械设计基础", "机械设计基础"),
    ("modern-automotive-chassis-design", "汽车底盘现代设计", "汽车底盘现代设计"),
    ("automobile-structure", "汽车构造", "汽车构造 ("),
    ("automobile-structure-3d", "汽车构造与原理三维图解", "汽车构造与原理三维图解"),
    ("smart-car-stm32-ten-days", "十天学会智能车：基于STM32", "十天学会智能车"),
    ("diy-smart-car-robot", "玩转机器人DIY智能小车机器人", "玩转机器人DIY智能小车机器人"),
    ("solidworks-robot-design", "玩转机器人基于SolidWorks的设计实例", "玩转机器人基于SolidWorks的设计实例"),
    ("unmanned-vehicle-theory-design", "无人驾驶车辆理论与设计", "无人驾驶车辆理论与设计"),
    ("autonomous-car-introduction", "无人驾驶汽车概论", "无人驾驶汽车概论"),
    ("mobile-robot-navigation-intelligent-control", "移动机器人导航与智能控制技术", "移动机器人导航与智能控制技术"),
    ("mobile-robot-3d-reconstruction", "移动机器人及室内环境三维模型重建技术", "移动机器人及室内环境三维模型重建技术"),
    ("mobile-robotics-alonzo-kelly", "移动机器人学（Alonzo Kelly）", "移动机器人学 (Alonzo Kelly)"),
    ("mobile-robot-principles-design", "移动机器人原理与设计", "移动机器人原理与设计"),
    ("smart-car-complete-design", "智能车制作：元器件到完整设计", "智能车制作 从元器件"),
    ("smart-car-robot-handbook", "智能小车机器人制作大全", "智能小车机器人制作大全"),
    ("smart-car-making", "智能小车制作", "智能小车制作 ("),
    ("slam-theory-practice", "自动驾驶与机器人中的SLAM技术", "自动驾驶与机器人中的SLAM技术"),
    ("intro-autonomous-mobile-robots", "自主移动机器人导论", "自主移动机器人导论"),
]


LEARNING_DETAILS = {
    "mechanical-control-foundations": {
        "extraction_status": "curated",
        "page_count": 226,
        "keys": ["PID", "稳定性", "时域响应", "控制系统"],
        "summary": "控制系统时域、稳定性与 PID 校正的理论资料。",
    },
    "mobile-robot-navigation-intelligent-control": {
        "extraction_status": "curated",
        "page_count": 305,
        "keys": ["移动机器人", "传感器融合", "控制", "导航", "SLAM"],
        "summary": "移动机器人架构、传感器融合、控制与导航的参考资料。",
    },
    "mobile-robotics-alonzo-kelly": {
        "extraction_status": "curated",
        "page_count": 581,
        "keys": ["轮式运动学", "里程计", "状态估计", "轨迹跟踪", "超声传感器"],
        "summary": "轮式移动机器人的运动学、状态估计、控制与传感器理论资料。",
    },
    "slam-theory-practice": {
        "extraction_status": "curated",
        "page_count": 390,
        "keys": ["SLAM", "IMU", "组合导航", "ESKF", "激光里程计"],
        "summary": "SLAM、惯性导航、误差状态滤波与定位实践的参考资料。",
    },
    "intro-autonomous-mobile-robots": {"page_count": 349},
    "unmanned-vehicle-theory-design": {"page_count": 269},
}


ROS_SOURCE_SPECS = [
    {
        "slug": "raspberry-pi-project-complete-reading",
        "title": "树莓派4B配置与项目资料完整解读",
        "rel": r"树莓派4B配置与项目资料完整解读.md",
        "kind": "project_document",
        "authority": "B",
        "confidentiality": "restricted",
        "status": "curated-sanitized",
        "keys": ["Renew", "trajectory_recorder", "integrated.launch", "bringup", "devices.yaml"],
        "summary": "历史 Renew 工作区的部署与入口说明；仅抽取不含账号、网络或凭据值的段落。",
    },
    {
        "slug": "ros-education-series-index",
        "title": "ROS教育机器人系列资料索引",
        "rel": r"readme_ROS教育机器人系列.txt",
        "kind": "vendor_index",
        "authority": "C",
        "status": "metadata-only",
        "keys": ["ROS教育机器人", "厂商资料"],
        "summary": "厂商资料导航索引，不作为三号车当前实现证据。",
    },
    {
        "slug": "raspberry-pi-ros-install",
        "title": "树莓派ROS安装说明",
        "rel": r"树莓派ros安装.docx",
        "kind": "deployment_document",
        "authority": "C",
        "status": "metadata-only",
        "keys": ["树莓派", "ROS安装"],
        "summary": "环境安装资料，未用于判定当前代码结构。",
    },
    {
        "slug": "renew-project-architecture",
        "title": "Renew历史项目架构",
        "rel": r"Renew\PROJECT_ARCHITECTURE.md",
        "kind": "architecture_document",
        "authority": "B",
        "status": "curated",
        "keys": ["trajectory_recorder", "trajectory_tracker", "/odom", "/trajectory_status", "/ultrasonic/left_distance"],
        "summary": "2026年3月 Renew 架构、节点、话题与已知问题的历史说明。",
    },
    {
        "slug": "renew-imu-integration-guide",
        "title": "YB-MRA02十轴IMU集成技术文档",
        "rel": r"Renew\docs\IMU_integration_guide.md",
        "kind": "integration_guide",
        "authority": "B",
        "status": "curated",
        "keys": ["YB-MRA02", "IMU", "navigation_fusion", "complementary", "encoder_only"],
        "summary": "历史 Renew 中 IMU 接入、融合与降级设计说明。",
    },
    {
        "slug": "renew-hardware-debug-experience",
        "title": "Renew新增硬件调试经验",
        "rel": r"Renew\CODEX_MEMORY新加硬件调试经验.md",
        "kind": "debug_record",
        "authority": "B",
        "status": "curated-sanitized",
        "keys": ["DYP-A21", "RB100", "MGS-16FP", "YZ-AIM", "RS485"],
        "summary": "历史硬件映射与现场排障记录；不摄取任何账号、网络或凭据值。",
    },
    {
        "slug": "renew-vendor-fusion-plan",
        "title": "Renew厂商资料融合方案",
        "rel": r"Renew\VENDOR_FUSION_PLAN.md",
        "kind": "engineering_plan",
        "authority": "B",
        "status": "curated",
        "keys": ["udev", "固定设备别名", "integrated.launch", "依赖补全"],
        "summary": "将厂商部署思路融合到 Renew 的规划性文档。",
    },
    {
        "slug": "ms16a-modbus-manual",
        "title": "MS-16A磁导航传感器Modbus说明书",
        "rel": r"Renew\资料\磁钉传感器资料\MS-16A (RS485)磁导航传感器资料\MS-16A (RS485)\磁导航传感器MS-16A（RS485接口）使用说明书\磁导航传感器485接口ModBus协议产品说明书v1.5.19.1.pdf",
        "kind": "vendor_protocol",
        "authority": "A",
        "confidentiality": "restricted",
        "status": "curated",
        "keys": ["MS-16A", "RS485", "Modbus RTU", "0x0001", "9600"],
        "summary": "MS-16A 规格、安装约束及 Modbus 读数协议；原件带保密标记，仅保存摘要。",
    },
    {
        "slug": "dyp-a21-datasheet",
        "title": "DYP-A21产品规格书",
        "rel": r"Renew\资料\超声波循迹资料\DYP-RD-产品规格书(DYP-A21-V1.0)-240220-A0.pdf",
        "kind": "vendor_datasheet_protocol",
        "authority": "A",
        "status": "curated",
        "keys": ["DYP-A21", "CAN", "250Kbps", "0x0520", "0xFFFE", "0xFFFD"],
        "summary": "DYP-A21 量程、异常值与 CAN 协议说明。",
    },
    {
        "slug": "h56-coulomb-protocol",
        "title": "H56库仑计串口通讯协议V3.0",
        "rel": r"Renew\资料\库仑计资料\3316832516H56库仑计串口通讯协议 V3.0.docx",
        "kind": "vendor_protocol",
        "authority": "A",
        "status": "curated",
        "keys": ["H56", "Modbus RTU", "SOC", "0x00", "0x1D", "0x1E"],
        "summary": "H56 系列通讯功能码、SOC 与状态寄存器说明；维护写命令不得自动执行。",
    },
    {
        "slug": "rb200-encoder-protocol",
        "title": "RB200单圈编码器Modbus协议",
        "rel": r"Renew\资料\编码器资料\3312698856RB200 单圈编码器-Modbus-RTU(1).pdf",
        "kind": "vendor_protocol",
        "authority": "A",
        "status": "curated",
        "keys": ["RB200", "0x0064", "0.01度", "9600"],
        "summary": "RB200 角度寄存器与缩放规则；与 V1 节点名称 RB100 存在型号冲突。",
    },
    {
        "slug": "huakong-analog-rs485-manual",
        "title": "华控模拟量输出模块RS485手册",
        "rel": r"Renew\资料\模拟量输出模块资料\模拟量输出系列使用手册(RS485版).pdf",
        "kind": "vendor_manual",
        "authority": "A",
        "status": "curated",
        "keys": ["模拟量输出", "RS485", "Modbus", "0x000A", "0-5V", "0-10V"],
        "summary": "华控模拟量模块通道、量程与输出寄存器说明。",
    },
    {
        "slug": "huakong-digital-io-rs485-manual",
        "title": "华控数字量输入输出模块RS485手册",
        "rel": r"Renew\资料\数字量输出模块资料\数字量输入输出系列使用手册(RS485版).pdf",
        "kind": "vendor_manual",
        "authority": "A",
        "status": "curated",
        "keys": ["数字量输入", "继电器输出", "Modbus", "01", "02", "05", "38400"],
        "summary": "华控数字 IO 的通道能力、功能码与默认串口参数。",
    },
    {
        "slug": "yz-aim-rs485-manual",
        "title": "立三485步进驱动通讯手册",
        "rel": r"Renew\资料\电机资料\电机\485通讯手册_sv126.1.pdf",
        "kind": "vendor_protocol",
        "authority": "A",
        "status": "curated",
        "keys": ["立三", "YZ_AIM", "RS485", "0x009F", "0x00D4", "115200"],
        "summary": "步进驱动器 RS485 寄存器资料；仅对应组合实体中的 YZ_AIM 部分，不代表 OID 后端。",
    },
    {
        "slug": "ten-axis-imu-protocol",
        "title": "十轴IMU模块通讯协议",
        "rel": r"Renew\资料\10轴IMU惯导模块\5.附件\通讯协议\10轴IMU模块通讯协议.pdf",
        "aliases": [r"Renew\融合imu\10轴IMU模块通讯协议.pdf"],
        "kind": "vendor_protocol",
        "authority": "A",
        "status": "curated",
        "keys": ["十轴IMU", "加速度", "角速度", "四元数", "GPS", "校准寄存器"],
        "summary": "十轴 IMU 的输出字段与配置寄存器说明。",
    },
    {
        "slug": "ros-driver-board-pinout",
        "title": "ROS驱动板接口定义",
        "rel": r"ROS驱动小板资料\开发资料\【必看】驱动板接口定义.pdf",
        "kind": "vendor_pinout",
        "authority": "B",
        "status": "curated",
        "keys": ["驱动板", "OLED", "JTAG", "Motor A-D", "预留IO"],
        "summary": "同系列驱动板的物理接口图，尚不能证明三号车实际采用该 PCB。",
    },
    {
        "slug": "stm32-motion-chassis-manual",
        "title": "STM32运动底盘开发手册",
        "rel": r"ROS驱动小板资料\开发资料\3.点我快速下载部分上手视频与手册\2.STM32运动底盘开发手册_ROS教育机器人.pdf",
        "kind": "vendor_protocol",
        "authority": "A",
        "status": "curated",
        "keys": ["STM32", "115200", "24字节", "0x7B", "0x7D", "BCC", "wheeltec_base"],
        "summary": "ROS 与 STM32 底盘的串口帧结构、校验及数据字段说明。",
    },
    {
        "slug": "chassis-procurement-bom-2025-10-23",
        "title": "底盘及扩充控制系统采购明细表（2025-10-23）",
        "rel": r"Renew\资料\底盘以及扩充控制系统采购明细表2025.10.23.xlsx",
        "kind": "procurement_bom",
        "authority": "A",
        "confidentiality": "restricted",
        "status": "pending-safe-extraction",
        "keys": ["实装型号", "采购明细"],
        "summary": "可能用于确认实装型号；尚未按电子表格安全流程提取，价格、联系人和供应商不入图谱。",
    },
    {
        "slug": "ackermann-multimode-proposal",
        "title": "阿克曼磁钉、超声与预录轨多模式方案",
        "rel": r"Renew\资料\ROS 阿克曼底盘磁钉、超声波巡迹与预录轨方案.docx",
        "kind": "project_proposal",
        "authority": "B",
        "status": "curated",
        "keys": ["磁钉", "超声沿墙", "Pure Pursuit", "双PID", "AckermannDriveStamped", "急停"],
        "summary": "AI 辅助的多模式设计提案；只建立 proposes 关系，不推断为现行实现。",
    },
    {
        "slug": "ackermann-magnetic-trajectory-proposal",
        "title": "阿克曼磁钉巡迹与预录轨迹方案",
        "rel": r"Renew\资料\ROS 阿克曼底盘磁钉巡迹与预录轨迹方案.docx",
        "aliases": [r"Renew\资料\ROS 阿克曼底盘磁钉、超声波巡迹与预录轨代码.docx"],
        "kind": "project_proposal",
        "authority": "B",
        "status": "curated",
        "keys": ["/fused_pose", "/recorded_path", "/cmd_ackermann", "mag_odom_fusion", "ackermann_pure_pursuit"],
        "summary": "磁钉与预录轨迹融合提案；重复别名标题含超声，但正文一致且不据别名生成主张。",
    },
]


# Curated sources outside the historical ``推料车项目树莓派移植`` subroot.
# These are vendor reference-platform materials, not evidence that the current
# three-car code runs on C10B/L150/R3mini hardware.
ROS_SOURCE_SPECS.extend(
    [
        {
            "slug": "c10b-l150-user-manual",
            "title": "C10B-L150避障巡线雷达小车用户手册",
            "scope": "inventory-root",
            "rel": r"二驱C10B\WHEELTEC L150 避障巡线雷达小车资料\WHEELTEC L150 避障巡线雷达小车附送资料_V2.8_2025.05.15\2.使用与开发手册\1.避障巡线雷达小车用户手册.pdf",
            "kind": "vendor_reference_platform_manual",
            "authority": "A",
            "status": "curated-reference",
            "page_count": 52,
            "model_scope": "C10B-L150 reference platform",
            "keys": ["C10B", "L150", "STM32", "电磁巡线", "Ackermann", "115200", "24字节", "0x7B", "0x7D"],
            "summary": "C10B/L150 参考平台的底层控制、巡线、运动学和 ROS 串口接口手册；其车型与三号车当前代码来源不同。",
            "implementation_boundary": "只能形成 reference/related_theory；即使帧字段相似，也不能证明三号车采用 C10B/L150 控制板或固件。",
        },
        {
            "slug": "c10b-mcu-app-protocol",
            "title": "C10B单片机与APP通信协议",
            "scope": "inventory-root",
            "rel": r"二驱C10B\WHEELTEC L150 避障巡线雷达小车资料\WHEELTEC L150 避障巡线雷达小车附送资料_V2.8_2025.05.15\2.使用与开发手册\2.单片机与APP通信协议.pdf",
            "content_mirrors": [
                r"二驱C10B\WHEELTEC L150 避障巡线雷达小车资料\WHEELTEC L150 避障巡线雷达小车附送资料_V2.8_2025.05.15\1.使用与开发教程视频\5.主板外设讲解\8.蓝牙接口\单片机与APP通信协议.pdf"
            ],
            "kind": "vendor_reference_protocol",
            "authority": "A",
            "status": "curated-reference",
            "page_count": 10,
            "model_scope": "C10B/L150 APP and Wi-Fi module reference",
            "keys": ["UART", "ASCII", "APP", "遥控指令", "参数帧", "状态帧"],
            "summary": "厂商 APP 与单片机之间的串口命令、调参和状态显示格式；另一目录中的 PDF 提取文本一致，作为内容镜像排除。",
            "implementation_boundary": "未发现三号车当前代码接入该 APP 协议的证据。",
        },
        {
            "slug": "electromagnetic-guidance-principles",
            "title": "电磁巡线原理教程",
            "scope": "inventory-root",
            "rel": r"二驱C10B\WHEELTEC L150 避障巡线雷达小车资料\WHEELTEC L150 避障巡线雷达小车附送资料_V2.8_2025.05.15\2.使用与开发手册\2.电磁巡线相关\电磁巡线原理教程.pdf",
            "kind": "vendor_theory_guide",
            "authority": "B",
            "status": "curated-reference",
            "page_count": 8,
            "model_scope": "three-channel inductive line-following reference",
            "keys": ["电磁感应", "20kHz", "带通滤波", "LM386", "ADC", "三路归一化", "横向位置"],
            "summary": "通电导线、感应线圈、滤波放大、整流、三路 ADC 与归一化位置估计的原理资料。",
            "implementation_boundary": "描述的是 C10B 配套三通道电磁模块，不等同于三号车 MS-16A 磁导航传感器实现。",
        },
        {
            "slug": "wheeltec-pid-guide",
            "title": "WHEELTEC PID基础入门开发手册",
            "scope": "inventory-root",
            "rel": r"二驱C10B\WHEELTEC L150 避障巡线雷达小车资料\WHEELTEC L150 避障巡线雷达小车附送资料_V2.8_2025.05.15\3.电机舵机控制基础视频教程\PID基础入门：开发手册.pdf",
            "kind": "vendor_theory_guide",
            "authority": "B",
            "status": "curated-reference",
            "page_count": 31,
            "model_scope": "MCU motor-control tutorial",
            "keys": ["位置式PID", "增量式PI", "编码器", "串级PID", "限幅"],
            "summary": "位置式 PID、增量式 PI、编码器反馈与位置-速度串级控制的入门资料。",
            "implementation_boundary": "公式与调参建议是通用参考，不能证明三号车使用其中代码或增益。",
        },
        {
            "slug": "wheeled-chassis-kinematics",
            "title": "轮式移动机器人的运动学模型",
            "scope": "inventory-root",
            "rel": r"二驱C10B\WHEELTEC L150 避障巡线雷达小车资料\WHEELTEC L150 避障巡线雷达小车附送资料_V2.8_2025.05.15\4.智能车底盘运动学解析视频教程\轮式移动机器人的运动学模型.pdf",
            "kind": "vendor_theory_guide",
            "authority": "B",
            "status": "curated-reference",
            "page_count": 27,
            "model_scope": "generic wheeled platforms including Ackermann",
            "keys": ["Ackermann", "ICR", "轮距", "轴距", "正运动学", "逆运动学", "无侧滑假设"],
            "summary": "差速、阿克曼、四驱、麦轮和全向轮模型；阿克曼章节给出 ICR、内外轮转角及正逆运动学关系。",
            "implementation_boundary": "理论模型及假设不能证明三号车采用某组几何参数、拟合曲线或转向机构。",
        },
        {
            "slug": "c10b-mainboard-schematic-2025",
            "title": "C10B主板原理图2025-02-24",
            "scope": "inventory-root",
            "rel": r"二驱C10B\WHEELTEC L150 避障巡线雷达小车资料\WHEELTEC L150 避障巡线雷达小车附送资料_V2.8_2025.05.15\8.原理图\C10B主板原理图_2025-02-24.pdf",
            "kind": "vendor_reference_schematic",
            "authority": "A",
            "status": "curated-reference",
            "page_count": 3,
            "model_scope": "C10B board revision dated 2025-02-24",
            "keys": ["STM32F103RCT6", "电源", "串口", "PWM", "ADC", "编码器"],
            "summary": "C10B 板级电源、STM32F103RCT6 主控与外设连接原理图；旧无日期版本作为被更新副本排除。",
            "implementation_boundary": "没有采购单、铭牌或布线证据证明三号车实装此 PCB。",
        },
        {
            "slug": "c10b-resource-map",
            "title": "C10B主控资源分配详情表",
            "scope": "inventory-root",
            "rel": r"二驱C10B\WHEELTEC L150 避障巡线雷达小车资料\WHEELTEC L150 避障巡线雷达小车附送资料_V2.8_2025.05.15\8.原理图\C10B主控资源分配详情表.pdf",
            "kind": "vendor_reference_pin_map",
            "authority": "A",
            "status": "curated-reference",
            "page_count": 1,
            "model_scope": "C10B board resource allocation",
            "keys": ["UART1", "UART3", "UART4", "UART5", "TIM3", "ADC", "电磁巡线", "编码器"],
            "summary": "C10B 主板的电池 ADC、电机 PWM、蓝牙、雷达、CCD/电磁、编码器等 MCU 资源分配。",
            "implementation_boundary": "仅是 C10B 引脚参考，不是三号车接线或设备清单。",
        },
        {
            "slug": "r3mini-ackermann-installation",
            "title": "R3mini阿克曼底盘安装手册",
            "scope": "inventory-root",
            "rel": r"二驱C10B\WHEELTEC L150 避障巡线雷达小车资料\WHEELTEC L150系列小车安装视频\1. 底盘安装\R3mini阿克曼小车底盘\R3mini阿克曼小车安装视频\阿克曼底盘安装手册.pdf",
            "kind": "vendor_reference_installation_manual",
            "authority": "A",
            "status": "curated-reference",
            "page_count": 2,
            "model_scope": "R3mini Ackermann reference chassis",
            "keys": ["阿克曼", "转向舵机", "转向连杆", "12V30F MG513", "底盘装配"],
            "summary": "R3mini 阿克曼参考底盘的舵机、转向连杆、驱动电机和板件装配图。",
            "implementation_boundary": "机械装配资料不能证明三号车的底盘型号、尺寸或执行器选型。",
        },
        {
            "slug": "legacy-ros-host-autostart",
            "title": "ROS主机旧式开机自启动说明",
            "scope": "inventory-root",
            "rel": r"ROS主机中设置开机自启动程序.txt",
            "kind": "legacy_deployment_note",
            "authority": "C",
            "confidentiality": "restricted",
            "status": "curated-sanitized-reference",
            "model_scope": "legacy vendor deployment recipe",
            "keys": ["NFS", "rc.local", "开机自启动", "权限"],
            "summary": "旧式 NFS 挂载与 rc.local 自启动笔记；网络地址、用户名和路径值不进入图谱。",
            "implementation_boundary": "包含宽松权限和旧式启动做法，只作风险参考，不作推荐配置或三号车部署证据。",
        },
    ]
)


@lru_cache(maxsize=None)
def sha256_file(path_text: str) -> str:
    digest = hashlib.sha256()
    with Path(path_text).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_metadata(path: Path) -> dict[str, Any]:
    stat = path.stat()
    modified = datetime.fromtimestamp(stat.st_mtime).astimezone().isoformat(timespec="seconds")
    return {
        "source_path": str(path),
        "source_hash": sha256_file(str(path)),
        "source_size": stat.st_size,
        "source_modified": modified,
    }


def discover_sources() -> list[dict[str, Any]]:
    if not LEARNING_ROOT.is_dir() or not ROS_ROOT.is_dir() or not ROS_INVENTORY_ROOT.is_dir():
        raise FileNotFoundError("Both engineering-material roots must be available")

    learning_files = sorted(path for path in LEARNING_ROOT.iterdir() if path.is_file())
    sources: list[dict[str, Any]] = []
    claimed_paths: set[Path] = set()

    for slug, title, prefix in LEARNING_SPECS:
        matches = [path for path in learning_files if path.name.startswith(prefix)]
        if slug == "mechanical-design-robert-norton":
            if len(matches) != 2:
                raise ValueError(f"Expected two Robert Norton duplicates, found {len(matches)}")
            canonical = next(path for path in matches if not path.stem.endswith("-1"))
            aliases = [next(path for path in matches if path != canonical)]
        else:
            if len(matches) != 1:
                raise ValueError(f"Expected one source for {slug}, found {len(matches)}")
            canonical, aliases = matches[0], []
        claimed_paths.update(matches)
        detail = LEARNING_DETAILS.get(slug, {})
        item = {
            "source_id": f"agv:source:learning:{slug}",
            "slug": slug,
            "page_name": title,
            "title": title,
            "source_collection": "agv:source-collection:vehicle-learning",
            "source_kind": "pdf_book" if canonical.suffix.lower() == ".pdf" else "epub_book",
            "authority": "B",
            "confidentiality": "internal",
            "extraction_status": detail.get("extraction_status", "metadata-only"),
            "duplicate_aliases": [str(path) for path in aliases],
            "technical_keys": detail.get("keys", []),
            "summary": detail.get("summary", "参考资料，仅登记书目、哈希和自有摘要。"),
            "copyright_boundary": "来源授权状态未核验；不复制原文、图片或附件，只保存定位与原创摘要。",
            **source_metadata(canonical),
        }
        if "page_count" in detail:
            item["page_count"] = detail["page_count"]
        sources.append(item)

    if claimed_paths != set(learning_files):
        missing = sorted(str(path) for path in set(learning_files) - claimed_paths)
        extra = sorted(str(path) for path in claimed_paths - set(learning_files))
        raise ValueError(f"Learning inventory mismatch; missing={missing}, extra={extra}")

    for spec in ROS_SOURCE_SPECS:
        base = ROS_INVENTORY_ROOT if spec.get("scope") == "inventory-root" else ROS_ROOT
        canonical = base / spec["rel"]
        aliases = [base / rel for rel in spec.get("aliases", [])]
        content_mirrors = [base / rel for rel in spec.get("content_mirrors", [])]
        if (
            not canonical.is_file()
            or any(not path.is_file() for path in aliases)
            or any(not path.is_file() for path in content_mirrors)
        ):
            raise FileNotFoundError(f"Missing curated source or alias for {spec['slug']}")
        canonical_hash = sha256_file(str(canonical))
        for alias in aliases:
            if sha256_file(str(alias)) != canonical_hash:
                raise ValueError(f"Alias is not byte-identical: {alias}")
        sources.append(
            {
                "source_id": f"agv:source:ros:{spec['slug']}",
                "slug": spec["slug"],
                "page_name": spec["title"],
                "title": spec["title"],
                "source_collection": "agv:source-collection:ros-engineering-files",
                "source_kind": spec["kind"],
                "authority": spec["authority"],
                "confidentiality": spec.get("confidentiality", "internal"),
                "extraction_status": spec["status"],
                "duplicate_aliases": [str(path) for path in aliases],
                "content_mirrors_excluded": [str(path) for path in content_mirrors],
                "content_mirror_metadata": [source_metadata(path) for path in content_mirrors],
                "technical_keys": spec["keys"],
                "summary": spec["summary"],
                "model_scope": spec.get("model_scope"),
                "implementation_boundary": spec.get("implementation_boundary"),
                "copyright_boundary": "只保存必要摘要、定位和哈希；不复制原始附件。",
                **source_metadata(canonical),
            }
        )
        if "page_count" in spec:
            sources[-1]["page_count"] = spec["page_count"]

    return sorted(sources, key=lambda item: item["source_id"])


ROS_COVERAGE_CATEGORY_META: dict[str, dict[str, str]] = {
    "included_curated_source": {
        "disposition": "included-metadata-and-summary",
        "reason": "已选择的规范工程来源；图谱只登记元数据、哈希、定位和原创摘要。",
    },
    "registered_duplicate_alias": {
        "disposition": "registered-alias-not-copied",
        "reason": "规范来源的字节级相同别名；只作为来源身份元数据登记。",
    },
    "excluded_duplicate_or_superseded": {
        "disposition": "excluded",
        "reason": "提取文本等价的镜像或已被更新的版本；仅保留规范或最新来源。",
    },
    "excluded_installer_activation_binary": {
        "disposition": "excluded",
        "reason": "安装器、破解/激活工具、打包应用、可执行文件或二进制依赖。",
    },
    "excluded_archive_or_incomplete_download": {
        "disposition": "excluded",
        "reason": "压缩包、磁盘镜像或未完成的云下载；不解压、不执行。",
    },
    "excluded_media_or_image": {
        "disposition": "excluded",
        "reason": "视频、音频或批量图片资产；不属于本轮精选语义图谱范围。",
    },
    "excluded_mechanical_arm_or_unrelated_platform": {
        "disposition": "excluded",
        "reason": "R550A 机械臂/MoveIt 或其他无关平台资料，不属于三号车范围。",
    },
    "excluded_code_or_build_mirror": {
        "disposition": "excluded",
        "reason": "教程/源码镜像、node_modules、build/devel/install 产物或仓库元数据；代码由独立 V2 扫描处理。",
    },
    "excluded_sensitive_or_runtime_data": {
        "disposition": "excluded",
        "reason": "凭据/网络配置、日志、bag、轨迹或其他运行数据。",
    },
    "excluded_tutorial_or_generic_training": {
        "disposition": "excluded",
        "reason": "通用 ROS/Linux 教程或未完成课程下载，不能为三号车提供直接证据。",
    },
    "excluded_vendor_boilerplate": {
        "disposition": "excluded",
        "reason": "厂商联系、版权或更新说明等样板内容，不含本图谱所需工程信息。",
    },
    "excluded_unselected_model_reference": {
        "disposition": "excluded",
        "reason": "未选择的 C10B/L150/R3mini 型号资料、重复示例或教程代码；明确保留型号不匹配边界。",
    },
    "excluded_unselected_project_material": {
        "disposition": "excluded",
        "reason": "经相关性、重复、安全和来源边界审查后未选择的项目树资料。",
    },
    "excluded_generic_or_root_material": {
        "disposition": "excluded",
        "reason": "无法形成有依据的独特工程主张的根目录或杂项目资料。",
    },
}


def _normal_path(path: Path | str) -> str:
    return os.path.normcase(os.path.normpath(str(path)))


def build_ros_coverage(sources: list[dict[str, Any]]) -> dict[str, Any]:
    """Account for every file under ``D:\\ROS工程文件`` without copying it."""

    curated_paths: dict[str, str] = {}
    curated_outside_historical_subroot = 0
    registered_aliases: set[str] = set()
    content_mirrors: set[str] = set()
    for source in sources:
        source_path = Path(source["source_path"])
        try:
            source_path.relative_to(ROS_INVENTORY_ROOT)
        except ValueError:
            continue
        curated_paths[_normal_path(source_path)] = source["source_id"]
        try:
            source_path.relative_to(ROS_ROOT)
        except ValueError:
            curated_outside_historical_subroot += 1
        registered_aliases.update(_normal_path(path) for path in source.get("duplicate_aliases", []))
        content_mirrors.update(_normal_path(path) for path in source.get("content_mirrors_excluded", []))

    superseded_relatives = {
        r"二驱C10B\WHEELTEC L150 避障巡线雷达小车资料\WHEELTEC L150 避障巡线雷达小车附送资料_V2.8_2025.05.15\1.使用与开发教程视频\4.主板原理图\C10B主板原理图.pdf"
    }
    superseded_paths = {_normal_path(ROS_INVENTORY_ROOT / rel) for rel in superseded_relatives}
    installer_roots = {"solidworks 2025 64bit", "visio安装包和激活工具"}
    mechanical_arm_roots = {"ros资料最新"}
    tutorial_roots = {"入门教程-强烈推荐", "ros理论与实践学习"}
    vendor_boilerplate_roots = {"wheeltec 直流电机附送资料"}
    code_components = {
        ".git",
        "node_modules",
        "build",
        "devel",
        "install",
        "src",
        "src-claude",
        "src-codex",
        "sensor2_ws-master",
        "__pycache__",
    }
    sensitive_names = {
        "pi-wifi-receive.txt",
        "codex_memory_exam_system_linux_deploy.md",
        "readme.md",
    }
    executable_extensions = {
        ".exe",
        ".msi",
        ".dll",
        ".cab",
        ".mst",
        ".pak",
        ".sys",
        ".so",
        ".bin",
        ".appx",
    }
    archive_extensions = {".zip", ".rar", ".7z", ".iso", ".img", ".ova", ".downloading"}
    media_extensions = {".mp4", ".avi", ".mov", ".mkv", ".wmv", ".mp3", ".wav", ".gif", ".jpg", ".jpeg", ".png"}
    runtime_extensions = {".bag", ".db3", ".log"}

    def classify(path: Path, relative: Path) -> str:
        normalized = _normal_path(path)
        parts_lower = [part.casefold() for part in relative.parts]
        top = parts_lower[0]
        suffix = path.suffix.casefold()
        if normalized in curated_paths:
            return "included_curated_source"
        if normalized in registered_aliases:
            return "registered_duplicate_alias"
        if normalized in content_mirrors or normalized in superseded_paths:
            return "excluded_duplicate_or_superseded"
        if top in installer_roots or suffix in executable_extensions:
            return "excluded_installer_activation_binary"
        if top in mechanical_arm_roots:
            return "excluded_mechanical_arm_or_unrelated_platform"
        if any(part in code_components for part in parts_lower):
            return "excluded_code_or_build_mirror"
        if path.name.casefold() in sensitive_names or suffix in runtime_extensions:
            return "excluded_sensitive_or_runtime_data"
        if suffix in archive_extensions:
            return "excluded_archive_or_incomplete_download"
        if suffix in media_extensions:
            return "excluded_media_or_image"
        if top in tutorial_roots:
            return "excluded_tutorial_or_generic_training"
        if top in vendor_boilerplate_roots:
            return "excluded_vendor_boilerplate"
        if top == "二驱c10b":
            return "excluded_unselected_model_reference"
        if top == "推料车项目树莓派移植":
            return "excluded_unselected_project_material"
        return "excluded_generic_or_root_material"

    category_stats = {
        key: {"file_count": 0, "total_bytes": 0}
        for key in ROS_COVERAGE_CATEGORY_META
    }
    top_stats: dict[str, dict[str, Any]] = {}
    inventory_lines: list[str] = []
    file_count = 0
    directory_count = 0
    total_bytes = 0
    errors: list[str] = []

    def on_walk_error(error: OSError) -> None:
        errors.append(str(error))

    for directory, dirnames, filenames in os.walk(ROS_INVENTORY_ROOT, onerror=on_walk_error):
        dirnames.sort(key=str.casefold)
        filenames.sort(key=str.casefold)
        directory_path = Path(directory)
        if directory_path != ROS_INVENTORY_ROOT:
            relative_dir = directory_path.relative_to(ROS_INVENTORY_ROOT)
            directory_count += 1
            top_name = relative_dir.parts[0]
            top_stats.setdefault(
                top_name,
                {"entry_kind": "directory", "file_count": 0, "directory_count": 0, "total_bytes": 0, "categories": {}},
            )["directory_count"] += 1
        for filename in filenames:
            path = directory_path / filename
            relative = path.relative_to(ROS_INVENTORY_ROOT)
            try:
                size = path.stat().st_size
            except OSError as error:
                errors.append(f"{relative.as_posix()}: {error}")
                continue
            category = classify(path, relative)
            file_count += 1
            total_bytes += size
            category_stats[category]["file_count"] += 1
            category_stats[category]["total_bytes"] += size
            top_name = relative.parts[0]
            row = top_stats.setdefault(
                top_name,
                {
                    "entry_kind": "file" if len(relative.parts) == 1 else "directory",
                    "file_count": 0,
                    "directory_count": 0,
                    "total_bytes": 0,
                    "categories": {},
                },
            )
            row["file_count"] += 1
            row["total_bytes"] += size
            row["categories"][category] = row["categories"].get(category, 0) + 1
            inventory_lines.append(f"{relative.as_posix()}\t{size}")

    category_summary = []
    for category in sorted(category_stats):
        stats = category_stats[category]
        category_summary.append(
            {
                "category": category,
                **ROS_COVERAGE_CATEGORY_META[category],
                **stats,
            }
        )
    top_level = [
        {"name": name, **top_stats[name], "categories": dict(sorted(top_stats[name]["categories"].items()))}
        for name in sorted(top_stats, key=str.casefold)
    ]
    inventory_fingerprint = hashlib.sha256("\n".join(sorted(inventory_lines)).encode("utf-8")).hexdigest()
    return {
        "coverage_id": "agv:material-coverage:ros-engineering-files:v1",
        "schema_version": "1.0.0",
        "generated": UPDATED,
        "root": str(ROS_INVENTORY_ROOT),
        "inventory": {
            "file_count": file_count,
            "directory_count": directory_count,
            "total_bytes": total_bytes,
            "inventory_fingerprint": inventory_fingerprint,
            "walk_errors": errors,
        },
        "accounting": {
            "classified_file_count": sum(row["file_count"] for row in category_summary),
            "classified_total_bytes": sum(row["total_bytes"] for row in category_summary),
            "all_files_accounted_for": (
                sum(row["file_count"] for row in category_summary) == file_count
                and sum(row["total_bytes"] for row in category_summary) == total_bytes
                and not errors
            ),
        },
        "curated_canonical_source_count": len(curated_paths),
        "curated_outside_historical_subroot_count": curated_outside_historical_subroot,
        "registered_duplicate_alias_count": len(registered_aliases),
        "excluded_content_mirror_count": len(content_mirrors),
        "excluded_superseded_revision_count": len(superseded_paths),
        "category_summary": category_summary,
        "top_level_scope": top_level,
        "boundaries": {
            "model_mismatch": "C10B/L150/R3mini/reference material cannot serve as implementation evidence for current three-car code.",
            "security": "No installers, activation tools, executables, credentials, network values, raw logs, bags or trajectories are copied.",
            "code": "Tutorial/project code mirrors and build outputs are excluded; code evolution is handled by the independent V2 snapshot.",
            "copyright": "No source documents, long excerpts or images are copied into the generated graph.",
        },
    }


CLAIMS: list[dict[str, Any]] = [
    {
        "slug": "renew-primary-integrated-launch",
        "title": "历史 Renew 主入口为 integrated.launch",
        "source": "agv:source:ros:raspberry-pi-project-complete-reading",
        "locator": "UTF-8 行 63-75、703-709",
        "authority": "B",
        "state": "historical",
        "snapshot": "historical-renew-2026-04",
        "keys": ["Renew/src", "trajectory_recorder", "integrated.launch", "bringup"],
        "summary": "该资料把 Renew 认定为当时主工程，并把 trajectory_recorder/integrated.launch 作为主入口；bringup 被标为早期入口。",
        "limits": "这是历史资料，不覆盖三号车最新代码的 vehicle.launch 或新分层架构。",
    },
    {
        "slug": "renew-record-track-modes",
        "title": "历史 Renew 采用 record 与 track 两种模式",
        "source": "agv:source:ros:renew-project-architecture",
        "locator": "UTF-8 行 134-165",
        "authority": "B",
        "state": "historical",
        "snapshot": "historical-renew-2026-03",
        "keys": ["trajectory_recorder", "trajectory_tracker", "record", "track"],
        "summary": "录制模式启动 trajectory_recorder，跟踪模式启动 trajectory_tracker；二者由 integrated.launch 的 mode 参数选择。",
        "limits": "只描述 Renew 历史实现，不代表 V2 新分层节点的运行模式。",
    },
    {
        "slug": "bringup-historical-entry",
        "title": "bringup 在 Renew 资料中属于旧启动方式",
        "source": "agv:source:ros:raspberry-pi-project-complete-reading",
        "locator": "UTF-8 行 68-75、703-709",
        "authority": "B",
        "state": "deprecated",
        "snapshot": "historical-renew-2026-04",
        "keys": ["bringup", "all_nodes.launch", "integrated.launch"],
        "summary": "历史资料明确把 bringup/all_nodes.launch 归类为旧入口，并推荐 integrated.launch。",
        "limits": "废弃状态只适用于该历史资料所述时期。",
    },
    {
        "slug": "devices-yaml-not-authoritative",
        "title": "历史 Renew 的 devices.yaml 不是自动生效配置源",
        "source": "agv:source:ros:raspberry-pi-project-complete-reading",
        "locator": "UTF-8 行 213-223、710-713",
        "authority": "B",
        "state": "historical",
        "snapshot": "historical-renew-2026-04",
        "keys": ["devices.yaml", "launch 参数", "integrated.launch"],
        "summary": "资料说明当时程序实际读取 launch 参数，而不是自动加载 devices.yaml。",
        "limits": "必须在目标快照重新检查配置加载链，不能跨版本外推。",
    },
    {
        "slug": "renew-monolithic-tracker-drivers",
        "title": "历史 trajectory_tracker 内联多类硬件驱动",
        "source": "agv:source:ros:renew-project-architecture",
        "locator": "UTF-8 行 58-99、161-178",
        "authority": "B",
        "state": "historical",
        "snapshot": "historical-renew-2026-03",
        "keys": ["trajectory_tracker", "Encoder", "MagSensor", "RelayController", "SteeringMotor"],
        "summary": "历史架构把编码器、磁传感器、驱动电机、转向电机和继电器等能力集中在 trajectory_tracker 及共享驱动类中。",
        "limits": "最新代码已出现拆分趋势，不能据此覆盖 V2 实体。",
    },
    {
        "slug": "renew-legacy-ros-interfaces",
        "title": "历史 Renew 的轨迹与超声接口集合",
        "source": "agv:source:ros:renew-project-architecture",
        "locator": "UTF-8 行 189-204",
        "authority": "B",
        "state": "historical",
        "snapshot": "historical-renew-2026-03",
        "keys": ["/odom", "/trajectory_status", "/ultrasonic/left_distance", "/trajectory/play", "/trajectory/stop"],
        "summary": "资料登记了 /odom、/trajectory_status、四向超声距离及轨迹播放控制服务。",
        "limits": "接口身份匹配概率高，但发布者、所有者和默认启动方式必须按 V2 重新验证。",
    },
    {
        "slug": "renew-imu-fusion-degradation",
        "title": "历史 Renew 设计了 IMU 组合导航与降级",
        "source": "agv:source:ros:renew-imu-integration-guide",
        "locator": "UTF-8 行 40-42、187-202、251-258",
        "authority": "B",
        "state": "historical",
        "snapshot": "historical-renew-2026-03",
        "keys": ["IMU", "encoder", "complementary", "encoder_only", "mag_heading"],
        "summary": "文档把 IMU 与编码器用于航向和状态融合，并描述磁力计或 IMU 不可用时的降级。",
        "limits": "这是设计与自述验证结果，本轮未独立运行代码或实车测试。",
    },
    {
        "slug": "yz-aim-rs485-wiring-debug",
        "title": "YZ-AIM 无应答曾由 RS485 接线错误导致",
        "source": "agv:source:ros:renew-hardware-debug-experience",
        "locator": "UTF-8 行 148-152",
        "authority": "B",
        "state": "observed",
        "snapshot": "historical-renew-2026-04",
        "keys": ["YZ-AIM", "RS485", "A/B", "Modbus"],
        "summary": "调试记录将一次串口可打开但 Modbus 零字节响应归因于 RS485 接线错误，并建议优先核对 A/B、端子、波特率和地址。",
        "limits": "单次历史排障经验，不代表所有无应答故障。",
    },
    {
        "slug": "udev-stable-device-aliases",
        "title": "厂商融合方案建议使用 udev 固定设备别名",
        "source": "agv:source:ros:renew-vendor-fusion-plan",
        "locator": "UTF-8 行 19-25、36-68",
        "authority": "B",
        "state": "planned",
        "snapshot": "historical-renew-2026-04",
        "keys": ["udev", "/dev/agv_*", "CP2102", "CH340", "ttyACM"],
        "summary": "方案建议以 udev 规则创建稳定设备别名，再通过 launch 参数引用。",
        "limits": "规划性内容；未把规则是否部署标记为已实现。",
    },
    {
        "slug": "ms16a-protocol-and-baud-constraint",
        "title": "MS-16A 协议与默认波特率形成配置约束",
        "source": "agv:source:ros:ms16a-modbus-manual",
        "locator": "PDF 第 4-9 页",
        "authority": "A",
        "state": "specified",
        "snapshot": "vendor-manual-v1.5.19.1",
        "keys": ["MS-16A", "16点", "RS485", "Modbus RTU", "0x0001", "9600"],
        "summary": "手册规定 16 点磁检测、RS485 Modbus RTU、数据寄存器 0x0001 和出厂默认 9600；V1 静态代码的寄存器一致，但默认波特率为 38400。",
        "limits": "需要确认实装传感器是否预先改为 38400；不能直接判定代码缺陷。",
    },
    {
        "slug": "dyp-a21-can-protocol",
        "title": "DYP-A21 CAN 帧与异常值协议",
        "source": "agv:source:ros:dyp-a21-datasheet",
        "locator": "PDF 第 4、6、26-29 页",
        "authority": "A",
        "state": "specified",
        "snapshot": "vendor-datasheet-dyp-a21-v1.0",
        "keys": ["DYP-A21", "250Kbps", "0x0520+地址", "03/83", "0xFFFE", "0xFFFD", "0xFFFF"],
        "summary": "手册规定标准 CAN 帧、默认 250 Kbps、CAN ID 0x0520 加地址，以及测量与异常值语义；V1 静态实现与核心字段吻合。",
        "limits": "静态吻合不等于已在当前车辆运行验证。",
    },
    {
        "slug": "h56-modbus-soc-status-protocol",
        "title": "H56 SOC 与状态寄存器协议",
        "source": "agv:source:ros:h56-coulomb-protocol",
        "locator": "第 1-2 节及输入寄存器表（0x00、0x1D、0x1E）",
        "authority": "A",
        "state": "specified",
        "snapshot": "vendor-protocol-h56-v3.0",
        "keys": ["H56", "03", "04", "06", "10", "9600", "SOC*0.1", "0x1D", "0x1E"],
        "summary": "协议规定 Modbus RTU 功能码、默认 9600、SOC 0.1% 缩放及报警/充放电状态寄存器；V1 静态实现匹配。",
        "limits": "协议含置满、清零等维护写命令，知识图谱不得自动执行。",
    },
    {
        "slug": "rb200-angle-scaling-conflict",
        "title": "RB200 手册与 V1 RB100 节点存在型号和缩放冲突",
        "source": "agv:source:ros:rb200-encoder-protocol",
        "locator": "PDF 第 1-3 页、寄存器 0x0064",
        "authority": "A",
        "state": "contradicted",
        "snapshot": "vendor-rb200-manual",
        "keys": ["RB200", "RB100", "0x0064", "raw/100", "raw/1024*360"],
        "summary": "手册把 0x0064 定义为 0.01 度值，而 V1 rb100_encoder 读取同一地址后按 1024 计数一圈换算；必须先由采购明细或铭牌确认实装型号。",
        "limits": "只记录冲突，不自动修改缩放公式或实体型号。",
    },
    {
        "slug": "huakong-analog-output-protocol",
        "title": "华控模拟量输出能力与寄存器基址",
        "source": "agv:source:ros:huakong-analog-rs485-manual",
        "locator": "PDF 第 3-5、8 页",
        "authority": "A",
        "state": "specified",
        "snapshot": "vendor-huakong-analog-manual",
        "keys": ["1-12路", "0-5V", "0-10V", "0-20mA", "4-20mA", "12位", "0x000A"],
        "summary": "手册规定模拟量模块量程、通道、12 位分辨率和第一路输出寄存器 0x000A；V1 对应包处于 inactive。",
        "limits": "只建立文档/预期用途关系，不把 inactive 包改为已部署。",
    },
    {
        "slug": "huakong-digital-io-protocol",
        "title": "华控数字 IO 功能码与默认串口参数",
        "source": "agv:source:ros:huakong-digital-io-rs485-manual",
        "locator": "PDF 第 4-5、9 页",
        "authority": "A",
        "state": "specified",
        "snapshot": "vendor-huakong-dio-manual",
        "keys": ["1-48路", "38400", "01", "02", "05", "线圈0", "离散输入0"],
        "summary": "手册规定数字输入、继电器输出、默认 38400/8N1 以及功能码 01/02/05；V1 hk_dio 静态实现与主要协议字段吻合。",
        "limits": "V1 已知 launch 包名不一致仍需复核；不自动执行继电器写操作。",
    },
    {
        "slug": "yz-aim-register-protocol",
        "title": "立三 YZ_AIM 部分的 RS485 寄存器协议",
        "source": "agv:source:ros:yz-aim-rs485-manual",
        "locator": "运行模式与使能/重启寄存器章节",
        "authority": "A",
        "state": "specified",
        "snapshot": "vendor-yz-aim-rs485-manual",
        "keys": ["115200", "0x009F", "0x00D4", "YZ_AIM"],
        "summary": "手册的默认 115200、运行模式 0x009F 与使能/重启 0x00D4 和 V1 YZ_AIM 后端静态代码吻合。",
        "limits": "组合硬件实体还包含 OID；本结论不得映射到 OID 的 5000/6000 段寄存器。",
    },
    {
        "slug": "ten-axis-imu-output-protocol",
        "title": "十轴 IMU 输出与配置寄存器范围",
        "source": "agv:source:ros:ten-axis-imu-protocol",
        "locator": "输出数据与配置寄存器章节",
        "authority": "A",
        "state": "specified",
        "snapshot": "vendor-ten-axis-imu-protocol",
        "keys": ["加速度", "角速度", "角度", "磁场", "GPS", "四元数", "校准"],
        "summary": "协议覆盖惯性、磁场、定位与四元数输出以及校准、输出率和波特率配置。",
        "limits": "V1 imu_probe 是诊断节点，不能据手册推断其为生产 /imu 的唯一权威源。",
    },
    {
        "slug": "ackermann-multimode-design-proposal",
        "title": "多模式方案提出磁钉、超声与预录轨协同",
        "source": "agv:source:ros:ackermann-multimode-proposal",
        "locator": "OOXML 段落 16-17、30-51、79-80",
        "authority": "B",
        "state": "planned",
        "snapshot": "proposal-undated",
        "keys": ["磁导航PID", "超声沿墙PID", "Pure Pursuit", "模式切换", "急停"],
        "summary": "方案提出磁横向偏差、超声距离偏差和预录轨迹协同控制，并定义丢磁与近障安全行为。",
        "limits": "文档注明部分内容可能由 AI 生成；只建立 proposes 关系，不能标记为实现。",
    },
    {
        "slug": "ackermann-proposal-interface-gap",
        "title": "磁轨迹方案中的接口与 V1 图谱仅部分重合",
        "source": "agv:source:ros:ackermann-magnetic-trajectory-proposal",
        "locator": "OOXML 中节点、话题与融合流程段落",
        "authority": "B",
        "state": "planned",
        "snapshot": "proposal-undated",
        "keys": ["/fused_pose", "/recorded_path", "/cmd_ackermann", "mag_odom_fusion", "ackermann_pure_pursuit"],
        "summary": "方案提出的新节点和话题大多未在 V1 同名出现；V1 odometer 的相对 ackermann_cmd 订阅提示一个潜在图谱覆盖缺口。",
        "limits": "语义相关不等于同一接口；建议人工补录候选，不自动合并实体。",
    },
    {
        "slug": "wheel-robot-kinematics-reference",
        "title": "轮式移动机器人运动学是轨迹控制参考基础",
        "source": "agv:source:learning:mobile-robotics-alonzo-kelly",
        "locator": "PDF 第 160 页起，第 4.2 节",
        "authority": "B",
        "state": "reference",
        "snapshot": "theory-reference",
        "keys": ["轮式移动机器人运动学", "约束", "车体坐标系"],
        "summary": "轮式运动学用于解释车体运动约束和轨迹控制中的状态传播。",
        "limits": "理论关系不能证明项目采用某一具体模型或参数。",
    },
    {
        "slug": "pid-control-reference",
        "title": "PID 校正是控制律设计参考",
        "source": "agv:source:learning:mechanical-control-foundations",
        "locator": "PDF 第 174 页，第 9.3 节",
        "authority": "B",
        "state": "reference",
        "snapshot": "theory-reference",
        "keys": ["PID", "比例", "积分", "微分"],
        "summary": "PID 提供误差反馈校正的一般理论框架，可用于审阅控制参数和响应。",
        "limits": "不证明三号车当前代码采用完整 PID 或任何特定增益。",
    },
    {
        "slug": "slam-inertial-fusion-reference",
        "title": "惯性导航与误差状态融合是定位参考",
        "source": "agv:source:learning:slam-theory-practice",
        "locator": "PDF 第 64-115 页，第 3 章",
        "authority": "B",
        "state": "reference",
        "snapshot": "theory-reference",
        "keys": ["IMU", "组合导航", "ESKF", "误差状态"],
        "summary": "惯性测量与其他观测通过误差状态估计融合，是评审定位架构的理论背景。",
        "limits": "理论来源不证明 V1 或 V2 已正确实现 ESKF。",
    },
    {
        "slug": "ultrasonic-sensing-reference",
        "title": "超声测距是近障感知的参考手段",
        "source": "agv:source:learning:mobile-robotics-alonzo-kelly",
        "locator": "PDF 第 455 页附近，超声传感器章节",
        "authority": "B",
        "state": "reference",
        "snapshot": "theory-reference",
        "keys": ["超声传感器", "测距", "盲区", "障碍检测"],
        "summary": "超声测距的量程、盲区和反射特性是近障安全与循墙设计的理论背景。",
        "limits": "不替代 DYP-A21 型号手册或实车标定。",
    },
    {
        "slug": "stm32-chassis-serial-framing",
        "title": "WHEELTEC STM32 底盘串口帧与 V1 静态实现吻合",
        "source": "agv:source:ros:stm32-motion-chassis-manual",
        "locator": "PDF 第 7-8 页",
        "authority": "A",
        "state": "specified",
        "snapshot": "vendor-stm32-chassis-manual",
        "keys": ["115200", "24字节", "0x7B", "0x7D", "BCC XOR", "速度", "IMU", "电池"],
        "summary": "手册规定 ROS 与 STM32 串口 115200、24 字节接收帧、0x7B/0x7D 边界和 BCC 异或校验；V1 wheeltec_base 静态实现吻合。",
        "limits": "静态协议吻合不证明三号车实装硬件或运行质量。",
    },
    {
        "slug": "ros-driver-board-physical-interface",
        "title": "ROS 驱动板接口图是 STM32 底盘候选物理证据",
        "source": "agv:source:ros:ros-driver-board-pinout",
        "locator": "接口定义图页",
        "authority": "B",
        "state": "reference",
        "snapshot": "vendor-board-pinout",
        "keys": ["Motor A-D", "JTAG", "OLED", "预留IO"],
        "summary": "接口图描述同系列驱动小板的连接器和预留接口。",
        "limits": "缺少采购明细或铭牌确认，不能判定三号车实际采用该 PCB。",
    },
]


CLAIMS.extend(
    [
        {
            "slug": "c10b-reference-platform-serial-control",
            "title": "C10B-L150参考平台定义底盘串口与巡线控制链",
            "source": "agv:source:ros:c10b-l150-user-manual",
            "locator": "PDF 第 7、15、41-45 页",
            "authority": "A",
            "state": "reference",
            "snapshot": "vendor-reference-c10b-l150",
            "keys": ["C10B", "L150", "115200", "24字节", "0x7B", "0x7D", "电磁巡线", "Ackermann"],
            "summary": "手册描述 C10B/L150 的编码器速度、三通道电磁巡线及 115200 串口底盘帧，发送帧为 24 字节并采用 0x7B/0x7D 边界。",
            "limits": "这是 C10B/L150 厂商参考平台；协议相似只支持 reference 关系，不能作为三号车硬件、固件或运行实现证据。",
        },
        {
            "slug": "c10b-mcu-app-reference-protocol",
            "title": "C10B单片机与APP使用ASCII遥控和参数帧",
            "source": "agv:source:ros:c10b-mcu-app-protocol",
            "locator": "PDF 第 4-9 页",
            "authority": "A",
            "state": "reference",
            "snapshot": "vendor-reference-c10b-app",
            "keys": ["APP", "UART", "ASCII", "遥控字符", "参数帧", "状态帧"],
            "summary": "协议定义 APP 经通信模块与 MCU 交换 ASCII 遥控字符、调参帧及状态/波形显示帧。",
            "limits": "未发现三号车当前代码使用该 APP 协议；不得把同属遥控概念视为接口同一或已实现。",
        },
        {
            "slug": "electromagnetic-guidance-three-channel-reference",
            "title": "三通道电磁巡线通过滤波放大与归一化估计横向位置",
            "source": "agv:source:ros:electromagnetic-guidance-principles",
            "locator": "PDF 第 3-8 页",
            "authority": "B",
            "state": "reference",
            "snapshot": "vendor-reference-electromagnetic-line",
            "keys": ["电磁感应", "20kHz", "带通滤波", "LM386", "三路ADC", "归一化", "横向位置"],
            "summary": "资料把感应线圈信号经过选频、放大与整流后送入三路 ADC，并用左右中三路相对值归一化估计导线位置。",
            "limits": "C10B 三通道电磁模块与三号车 MS-16A 是不同传感器体系；只提供 related_theory，不提供实现证据。",
        },
        {
            "slug": "wheeltec-pid-control-reference",
            "title": "位置式PID与增量式PI可构成位置速度串级参考",
            "source": "agv:source:ros:wheeltec-pid-guide",
            "locator": "PDF 第 16-25 页",
            "authority": "B",
            "state": "reference",
            "snapshot": "vendor-reference-pid-tutorial",
            "keys": ["位置式PID", "增量式PI", "编码器反馈", "位置环", "速度环", "限幅"],
            "summary": "手册给出编码器反馈下的位置式 PID、增量式速度 PI 和位置外环-速度内环的串级结构。",
            "limits": "教程公式和示例代码不证明三号车采用相同控制律、采样周期、限幅或增益。",
        },
        {
            "slug": "ackermann-kinematics-reference-model",
            "title": "阿克曼运动学以共同瞬心和几何约束关联车速与转角",
            "source": "agv:source:ros:wheeled-chassis-kinematics",
            "locator": "PDF 第 5-7、24-26 页",
            "authority": "B",
            "state": "reference",
            "snapshot": "vendor-reference-ackermann-kinematics",
            "keys": ["Ackermann", "ICR", "轮距", "轴距", "正运动学", "逆运动学", "转角拟合"],
            "summary": "资料以刚体、平面运动和理想转向约束推导阿克曼内外轮转角、驱动轮速度及车体正逆运动学，并说明实际机构通常需要拟合。",
            "limits": "理论假设和厂商样车拟合不等于三号车几何参数、转向机构或标定曲线。",
        },
        {
            "slug": "c10b-resource-allocation-reference",
            "title": "C10B资源表把PWM-串口-ADC-编码器分配到固定MCU外设",
            "source": "agv:source:ros:c10b-resource-map",
            "locator": "PDF 第 1 页",
            "authority": "A",
            "state": "reference",
            "snapshot": "vendor-reference-c10b-resource-map",
            "keys": ["TIM3", "UART1", "UART3", "UART4", "UART5", "ADC", "电磁巡线", "编码器"],
            "summary": "资源表登记 C10B 的电机 PWM、蓝牙、雷达、OpenMV、CCD/电磁 ADC、编码器和超声接口分配。",
            "limits": "仅能说明 C10B 板级资源，不证明三号车接线、端口或设备所有权。",
        },
        {
            "slug": "c10b-mainboard-reference-schematic",
            "title": "C10B原理图是STM32F103RCT6参考板级设计",
            "source": "agv:source:ros:c10b-mainboard-schematic-2025",
            "locator": "PDF 第 1-3 页",
            "authority": "A",
            "state": "reference",
            "snapshot": "vendor-reference-c10b-schematic-2025",
            "keys": ["STM32F103RCT6", "DCDC", "3.3V", "串口", "PWM", "ADC"],
            "summary": "原理图描述 C10B 的电源、STM32F103RCT6 主控与板级外设连接。",
            "limits": "未由采购、铭牌或三号车线束确认该 PCB；只能建立 reference 关系。",
        },
        {
            "slug": "r3mini-ackermann-assembly-reference",
            "title": "R3mini安装手册展示舵机连杆式阿克曼参考底盘",
            "source": "agv:source:ros:r3mini-ackermann-installation",
            "locator": "PDF 第 1-2 页装配图",
            "authority": "A",
            "state": "reference",
            "snapshot": "vendor-reference-r3mini-ackermann",
            "keys": ["R3mini", "阿克曼", "转向舵机", "连杆", "12V30F MG513", "装配"],
            "summary": "装配图展示 R3mini 底盘的转向舵机、连杆、前轮转向总成和双驱动电机布局。",
            "limits": "该装配只说明参考样车结构，不证明三号车底盘型号或机械尺寸。",
        },
        {
            "slug": "legacy-autostart-note-security-boundary",
            "title": "旧式NFS与rc.local自启动笔记只作部署风险参考",
            "source": "agv:source:ros:legacy-ros-host-autostart",
            "locator": "UTF-8 全文（网络和路径值已排除）",
            "authority": "C",
            "state": "reference",
            "snapshot": "legacy-reference-deployment-note",
            "keys": ["NFS", "rc.local", "开机自启动", "宽松权限"],
            "summary": "笔记采用旧式 NFS 挂载和 rc.local 启动流程，并包含不宜复用的宽松权限做法。",
            "limits": "不保存网络地址、用户名或路径值；不执行命令，不把旧式做法视为三号车当前部署。",
        },
    ]
)


for claim in CLAIMS:
    claim["claim_id"] = f"agv:claim:{claim['slug']}"
    claim["page_name"] = claim["title"]


TARGETS: dict[str, dict[str, str]] = {
    "agv:control:authority-arbitration": {"path": "05_Control/控制权仲裁.md", "title": "控制权仲裁", "type": "decision"},
    "agv:control:overview": {"path": "05_Control/控制架构总览.md", "title": "控制架构总览", "type": "system"},
    "agv:hardware:dyp-a21-ultrasonic": {"path": "02_Hardware/DYP-A21超声传感器.md", "title": "DYP-A21超声传感器", "type": "hardware"},
    "agv:hardware:encoder-odometry-feedback": {"path": "02_Hardware/编码器与里程反馈.md", "title": "编码器与里程反馈", "type": "hardware"},
    "agv:hardware:h56br-battery-meter": {"path": "02_Hardware/H56BR电池表.md", "title": "H56BR电池表", "type": "hardware"},
    "agv:hardware:huakong-io-analog": {"path": "02_Hardware/华控IO与模拟量模块.md", "title": "华控IO与模拟量模块", "type": "hardware"},
    "agv:hardware:ms16a-magnetic-sensor": {"path": "02_Hardware/MS16A磁传感器.md", "title": "MS16A磁传感器", "type": "hardware"},
    "agv:hardware:oid-yz-aim-motor-controller": {"path": "02_Hardware/OID与YZ_AIM电机控制器.md", "title": "OID与YZ_AIM电机控制器", "type": "hardware"},
    "agv:hardware:serial-can-rs485": {"path": "02_Hardware/串口CAN与RS485总线.md", "title": "串口CAN与RS485总线", "type": "hardware"},
    "agv:hardware:stm32-chassis": {"path": "02_Hardware/STM32底盘控制器.md", "title": "STM32底盘控制器", "type": "hardware"},
    "agv:navigation:magnetic": {"path": "04_Navigation/磁导航与磁钉.md", "title": "磁导航与磁钉", "type": "algorithm"},
    "agv:navigation:trajectory-system": {"path": "04_Navigation/轨迹记录与跟踪.md", "title": "轨迹记录与跟踪", "type": "algorithm"},
    "agv:navigation:ultrasonic-safety": {"path": "04_Navigation/超声安全与循墙.md", "title": "超声安全与循墙", "type": "algorithm"},
    "agv:ros:interface:battery-h56br-soc": {"path": "03_ROS/Interfaces/battery-h56br-soc.md", "title": "/battery/h56br/soc", "type": "ros_interface"},
    "agv:ros:interface:battery-h56br-status": {"path": "03_ROS/Interfaces/battery-h56br-status.md", "title": "/battery/h56br/status", "type": "ros_interface"},
    "agv:ros:interface:cmd-vel": {"path": "03_ROS/Interfaces/cmd-vel.md", "title": "/cmd_vel", "type": "ros_interface"},
    "agv:ros:interface:hardware-probe-topics": {"path": "03_ROS/Interfaces/hardware-probe-topics.md", "title": "硬件探针话题", "type": "ros_interface"},
    "agv:ros:interface:imu": {"path": "03_ROS/Interfaces/imu.md", "title": "/imu", "type": "ros_interface"},
    "agv:ros:interface:mag-sensor-raw-data": {"path": "03_ROS/Interfaces/mag-sensor-raw-data.md", "title": "/mag_sensor/raw_data", "type": "ros_interface"},
    "agv:ros:interface:odom": {"path": "03_ROS/Interfaces/odom.md", "title": "/odom", "type": "ros_interface"},
    "agv:ros:interface:relay-io-status": {"path": "03_ROS/Interfaces/relay-io-status.md", "title": "继电器与IO状态", "type": "ros_interface"},
    "agv:ros:interface:trajectory-services": {"path": "03_ROS/Interfaces/trajectory-services.md", "title": "轨迹控制服务", "type": "ros_interface"},
    "agv:ros:interface:trajectory-status": {"path": "03_ROS/Interfaces/trajectory-status.md", "title": "/trajectory_status", "type": "ros_interface"},
    "agv:ros:interface:ultrasonic-distance": {"path": "03_ROS/Interfaces/ultrasonic-distance.md", "title": "超声距离话题", "type": "ros_interface"},
    "agv:ros:interface:ultrasonic-status": {"path": "03_ROS/Interfaces/ultrasonic-status.md", "title": "超声状态话题", "type": "ros_interface"},
    "agv:ros:node:chassis_bridge": {"path": "03_ROS/Nodes/chassis_bridge.md", "title": "chassis_bridge", "type": "ros_node"},
    "agv:ros:node:dyp_a21_can_node": {"path": "03_ROS/Nodes/dyp_a21_can_node.md", "title": "dyp_a21_can_node", "type": "ros_node"},
    "agv:ros:node:h56br_node": {"path": "03_ROS/Nodes/h56br_node.md", "title": "h56br_node", "type": "ros_node"},
    "agv:ros:node:hk_dio_controller": {"path": "03_ROS/Nodes/hk_dio_controller.md", "title": "hk_dio_controller", "type": "ros_node"},
    "agv:ros:node:imu_probe": {"path": "03_ROS/Nodes/imu_probe.md", "title": "imu_probe", "type": "ros_node"},
    "agv:ros:node:mag_sensor_reader": {"path": "03_ROS/Nodes/mag_sensor_reader.md", "title": "mag_sensor_reader", "type": "ros_node"},
    "agv:ros:node:odometer": {"path": "03_ROS/Nodes/odometer.md", "title": "odometer", "type": "ros_node"},
    "agv:ros:node:rb100_encoder": {"path": "03_ROS/Nodes/rb100_encoder.md", "title": "rb100_encoder", "type": "ros_node"},
    "agv:ros:node:steering_remote": {"path": "03_ROS/Nodes/steering_remote.md", "title": "steering_remote", "type": "ros_node"},
    "agv:ros:node:trajectory_recorder": {"path": "03_ROS/Nodes/trajectory_recorder.md", "title": "trajectory_recorder", "type": "ros_node"},
    "agv:ros:node:trajectory_tracker": {"path": "03_ROS/Nodes/trajectory_tracker.md", "title": "trajectory_tracker", "type": "ros_node"},
    "agv:ros:node:wheeltec_robot_node": {"path": "03_ROS/Nodes/wheeltec_robot_node.md", "title": "wheeltec_robot_node", "type": "ros_node"},
    "agv:ros:node:yz_aim_probe": {"path": "03_ROS/Nodes/yz_aim_probe.md", "title": "yz_aim_probe", "type": "ros_node"},
    "agv:ros:package:analog_controlled_motor": {"path": "03_ROS/Packages/analog_controlled_motor.md", "title": "analog_controlled_motor", "type": "ros_package"},
    "agv:ros:package:bringup": {"path": "03_ROS/Packages/bringup.md", "title": "bringup", "type": "ros_package"},
    "agv:ros:package:trajectory_recorder": {"path": "03_ROS/Packages/trajectory_recorder.md", "title": "trajectory_recorder", "type": "ros_package"},
    "agv:ros:package:ultrasonic_controlled_motor": {"path": "03_ROS/Packages/ultrasonic_controlled_motor.md", "title": "ultrasonic_controlled_motor", "type": "ros_package"},
    "agv:system:knowledge-graph-coverage": {"path": "00_System/Knowledge-Graph-Coverage.md", "title": "Knowledge Graph Coverage", "type": "report"},
}


MATCH_SPECS = [
    ("renew-primary-integrated-launch", "agv:ros:package:trajectory_recorder", "describes", 100, "historical-document", "包名、主入口路径和架构上下文均精确命中。"),
    ("renew-record-track-modes", "agv:ros:node:trajectory_recorder", "describes", 100, "historical-document", "节点名和 record 模式精确命中。"),
    ("renew-record-track-modes", "agv:ros:node:trajectory_tracker", "describes", 100, "historical-document", "节点名和 track 模式精确命中。"),
    ("bringup-historical-entry", "agv:ros:package:bringup", "deprecates_in_context", 98, "historical-document", "包名与旧入口角色精确命中。"),
    ("devices-yaml-not-authoritative", "agv:ros:package:trajectory_recorder", "configuration_constraint", 88, "document-only", "配置文件路径和 launch 参数上下文命中；需在目标快照复核加载链。", ["跨版本配置加载方式可能变化"]),
    ("renew-monolithic-tracker-drivers", "agv:ros:package:trajectory_recorder", "describes", 100, "historical-document", "包、节点和共享驱动类路径均精确命中。"),
    ("renew-legacy-ros-interfaces", "agv:ros:interface:odom", "describes", 100, "historical-document", "ROS 话题名精确命中。"),
    ("renew-legacy-ros-interfaces", "agv:ros:interface:trajectory-status", "describes", 100, "historical-document", "ROS 话题名精确命中。"),
    ("renew-legacy-ros-interfaces", "agv:ros:interface:ultrasonic-distance", "describes", 98, "historical-document", "四向超声话题模式与聚合接口实体吻合。"),
    ("renew-legacy-ros-interfaces", "agv:ros:interface:trajectory-services", "describes", 98, "historical-document", "轨迹播放、停止和暂停服务模式命中。"),
    ("renew-imu-fusion-degradation", "agv:ros:interface:imu", "describes", 86, "documented-design", "IMU 语义与接口类型相符，但历史指南没有证明当前 /imu 所有权。", ["生产话题所有者未由本资料确认"]),
    ("renew-imu-fusion-degradation", "agv:ros:node:trajectory_tracker", "describes", 96, "historical-document", "节点名、融合类和跟踪上下文精确命中。"),
    ("yz-aim-rs485-wiring-debug", "agv:hardware:oid-yz-aim-motor-controller", "tests", 92, "field-observation", "YZ-AIM 型号和 RS485 调试上下文命中组合硬件实体。"),
    ("udev-stable-device-aliases", "agv:hardware:serial-can-rs485", "proposes", 82, "planned-only", "设备总线与稳定串口别名语义匹配；未确认规则已部署。"),
    ("ms16a-protocol-and-baud-constraint", "agv:hardware:ms16a-magnetic-sensor", "specifies", 100, "vendor-specification", "型号 MS-16A 精确命中。"),
    ("ms16a-protocol-and-baud-constraint", "agv:ros:node:mag_sensor_reader", "configuration_constraint", 99, "verified-static-with-runtime-check", "寄存器 0x0001 与静态代码吻合，但默认波特率不同。", ["手册默认9600，V1节点默认38400；需确认设备预配置"]),
    ("ms16a-protocol-and-baud-constraint", "agv:ros:interface:mag-sensor-raw-data", "specifies_protocol_for", 100, "verified-static", "16 位采样位图及读寄存器语义精确命中。"),
    ("dyp-a21-can-protocol", "agv:hardware:dyp-a21-ultrasonic", "specifies", 100, "vendor-specification", "型号 DYP-A21 精确命中。"),
    ("dyp-a21-can-protocol", "agv:ros:node:dyp_a21_can_node", "specifies_protocol_for", 100, "verified-static", "250 Kbps、CAN ID 公式、功能码和异常值均静态吻合。"),
    ("dyp-a21-can-protocol", "agv:ros:interface:ultrasonic-distance", "specifies_payload_for", 100, "verified-static", "测距值和四向距离接口语义吻合。"),
    ("dyp-a21-can-protocol", "agv:ros:interface:ultrasonic-status", "specifies_payload_for", 100, "verified-static", "异常值到状态语义的映射吻合。"),
    ("h56-modbus-soc-status-protocol", "agv:hardware:h56br-battery-meter", "specifies", 100, "vendor-specification", "H56 系列与电池表实体精确命中。"),
    ("h56-modbus-soc-status-protocol", "agv:ros:node:h56br_node", "specifies_protocol_for", 100, "verified-static", "功能码、波特率和寄存器静态吻合。"),
    ("h56-modbus-soc-status-protocol", "agv:ros:interface:battery-h56br-status", "specifies_payload_for", 100, "verified-static", "报警与充放电状态寄存器精确命中。"),
    ("h56-modbus-soc-status-protocol", "agv:ros:interface:battery-h56br-soc", "specifies_payload_for", 100, "verified-static", "SOC 寄存器 0x00 与 0.1 缩放精确命中。"),
    ("rb200-angle-scaling-conflict", "agv:hardware:encoder-odometry-feedback", "describes_family_variant", 82, "variant-conflict", "同属编码器里程反馈，但具体型号需要采购或铭牌确认。", ["资料为RB200，V1节点命名为RB100"]),
    ("rb200-angle-scaling-conflict", "agv:ros:node:rb100_encoder", "contradicts", 94, "verified-static-conflict", "寄存器 0x0064 强命中，但型号和缩放公式冲突。", ["RB200 raw/100 与 V1 raw/1024*360 不一致"]),
    ("huakong-analog-output-protocol", "agv:hardware:huakong-io-analog", "specifies", 99, "vendor-specification", "华控、模拟量、RS485 与量程字段强命中。"),
    ("huakong-analog-output-protocol", "agv:ros:package:analog_controlled_motor", "documents_intended_for", 100, "verified-static-not-deployed", "寄存器基址 0x000A 静态吻合；V1 包状态为 inactive。"),
    ("huakong-digital-io-protocol", "agv:hardware:huakong-io-analog", "specifies", 99, "vendor-specification", "组合实体包含华控数字 IO。"),
    ("huakong-digital-io-protocol", "agv:ros:node:hk_dio_controller", "specifies_protocol_for", 100, "verified-static", "38400、功能码 01/02/05 和基址静态吻合。"),
    ("huakong-digital-io-protocol", "agv:ros:interface:relay-io-status", "specifies_payload_for", 98, "verified-static-with-launch-review", "输入与继电器状态语义吻合；V1 launch 包名问题仍需复核。", ["V1已知launch包名不一致"]),
    ("yz-aim-register-protocol", "agv:hardware:oid-yz-aim-motor-controller", "specifies_component_of", 88, "vendor-specification", "仅命中组合实体的 YZ_AIM 部分。", ["不得把该手册外推到OID后端"]),
    ("yz-aim-register-protocol", "agv:ros:node:chassis_bridge", "specifies_protocol_for", 97, "verified-static", "115200、0x009F 与 0x00D4 静态命中 YZ_AIM 后端。"),
    ("yz-aim-register-protocol", "agv:ros:node:steering_remote", "specifies_protocol_for", 95, "verified-static", "转向远控节点使用相同 YZ_AIM 协议键。"),
    ("yz-aim-register-protocol", "agv:ros:node:yz_aim_probe", "specifies_protocol_for", 97, "verified-static-historical", "诊断节点名称和寄存器静态命中；V2 已移除该节点。"),
    ("ten-axis-imu-output-protocol", "agv:ros:node:imu_probe", "reference_implementation_for", 90, "diagnostic-only", "输出字段与诊断探针能力吻合。"),
    ("ten-axis-imu-output-protocol", "agv:ros:interface:imu", "specifies_payload_for", 86, "reference-topic-mismatch", "消息语义吻合，但厂商参考话题与 V1 /imu 不完全一致。", ["参考实现常用/imu/data，V1实体为/imu"]),
    ("ten-axis-imu-output-protocol", "agv:ros:interface:hardware-probe-topics", "specifies_payload_for", 90, "diagnostic-only", "探针输出字段与协议数据类型匹配。"),
    ("ten-axis-imu-output-protocol", "agv:ros:node:trajectory_tracker", "related_protocol", 80, "document-only", "历史 tracker 声称接入 IMU，但协议手册不能证明其生产数据所有权。", ["需要目标快照静态与运行复核"]),
    ("ackermann-multimode-design-proposal", "agv:navigation:magnetic", "proposes", 92, "planned-only", "磁横向偏差与磁导航 PID 概念强匹配。"),
    ("ackermann-multimode-design-proposal", "agv:navigation:ultrasonic-safety", "proposes", 97, "planned-only", "超声沿墙、近障停车与丢磁安全行为强匹配。"),
    ("ackermann-multimode-design-proposal", "agv:navigation:trajectory-system", "proposes", 96, "planned-only", "预录、重放与 Pure Pursuit 概念强匹配。"),
    ("ackermann-multimode-design-proposal", "agv:control:authority-arbitration", "proposes", 92, "planned-only", "模式切换和急停需要控制权仲裁，语义强匹配。"),
    ("ackermann-proposal-interface-gap", "agv:ros:node:odometer", "related_to", 80, "coverage-candidate", "相对 ackermann_cmd 订阅与方案控制话题部分相关，但不是同名接口。", ["/cmd_ackermann与相对ackermann_cmd不可自动合并"]),
    ("ackermann-proposal-interface-gap", "agv:system:knowledge-graph-coverage", "indicates_coverage_gap", 78, "coverage-candidate", "资料提示 V1 图谱可能漏记 odometer 的相对订阅接口。"),
    ("wheel-robot-kinematics-reference", "agv:navigation:trajectory-system", "related_theory", 60, "theory-only", "轮式运动学是轨迹控制的一般理论背景，只有语义关联。"),
    ("pid-control-reference", "agv:control:overview", "related_theory", 60, "theory-only", "PID 是控制架构的一般参考，不能证明具体实现。"),
    ("slam-inertial-fusion-reference", "agv:ros:interface:imu", "related_theory", 60, "theory-only", "惯性融合与 IMU 接口语义相关，不能证明 ESKF 实现。"),
    ("ultrasonic-sensing-reference", "agv:navigation:ultrasonic-safety", "related_theory", 60, "theory-only", "超声测距是安全与循墙的一般理论背景。"),
    ("stm32-chassis-serial-framing", "agv:hardware:stm32-chassis", "specifies", 100, "vendor-specification", "STM32 运动底盘型号域精确命中。"),
    ("stm32-chassis-serial-framing", "agv:ros:node:wheeltec_robot_node", "specifies_protocol_for", 100, "verified-static", "115200、24字节、0x7B/0x7D 与 BCC XOR 均静态吻合。"),
    ("stm32-chassis-serial-framing", "agv:ros:interface:cmd-vel", "specifies_transport_for", 96, "verified-static", "手册与节点链共同支持 /cmd_vel 到 STM32 的速度控制传输。"),
    ("stm32-chassis-serial-framing", "agv:ros:interface:odom", "specifies_transport_for", 94, "verified-static", "帧含速度/IMU数据并支撑历史里程输出，但 /odom 所有权需按版本复核。"),
    ("ros-driver-board-physical-interface", "agv:hardware:stm32-chassis", "documents_physical_interface_of", 75, "hardware-confirmation-needed", "同系列驱动板接口图与 STM32 底盘实体相关。", ["缺少三号车采购明细或铭牌确认"]),
]


MATCH_SPECS.extend(
    [
        (
            "c10b-reference-platform-serial-control",
            "agv:hardware:stm32-chassis",
            "reference",
            78,
            "reference-model-mismatch",
            "C10B/L150 同属 STM32 运动底盘参考域，但不能确认三号车实装型号。",
            ["C10B/L150 参考平台不是三号车硬件身份"],
        ),
        (
            "c10b-reference-platform-serial-control",
            "agv:ros:node:wheeltec_robot_node",
            "reference",
            88,
            "reference-model-mismatch",
            "115200、24字节、0x7B/0x7D 等字段高度相似，只支持参考协议关联。",
            ["协议相似不证明 C10B 固件或板卡被当前车辆采用"],
        ),
        (
            "c10b-mcu-app-reference-protocol",
            "agv:control:overview",
            "reference",
            55,
            "reference-model-mismatch",
            "APP 遥控与调参属于控制输入参考，但没有当前代码接口命中。",
            ["未发现三号车 APP 协议实现"],
        ),
        (
            "electromagnetic-guidance-three-channel-reference",
            "agv:navigation:magnetic",
            "related_theory",
            68,
            "theory-only",
            "三路信号估计横向位置与磁导航语义相关。",
            ["C10B 三通道电感模块与 MS-16A 不同"],
        ),
        (
            "wheeltec-pid-control-reference",
            "agv:control:overview",
            "related_theory",
            60,
            "theory-only",
            "位置、速度和串级反馈是控制架构的一般理论参考。",
        ),
        (
            "ackermann-kinematics-reference-model",
            "agv:navigation:trajectory-system",
            "related_theory",
            72,
            "theory-only",
            "阿克曼几何和正逆运动学是轨迹跟踪模型的理论背景。",
            ["车辆几何参数和模型假设尚未由三号车代码或标定确认"],
        ),
        (
            "ackermann-kinematics-reference-model",
            "agv:ros:node:odometer",
            "related_theory",
            65,
            "theory-only",
            "车体速度到位姿传播与轮式运动学相关。",
            ["不能据理论资料确认 V1 odometer 的参数或正确性"],
        ),
        (
            "c10b-resource-allocation-reference",
            "agv:hardware:stm32-chassis",
            "reference",
            70,
            "reference-model-mismatch",
            "资源表与 STM32 底盘外设类别相关，但板卡身份不同。",
            ["C10B 引脚分配不是三号车线束证据"],
        ),
        (
            "c10b-mainboard-reference-schematic",
            "agv:hardware:stm32-chassis",
            "reference",
            65,
            "reference-model-mismatch",
            "同属 STM32F103 底盘控制参考设计，缺少实装确认。",
            ["C10B 原理图不能外推为三号车 PCB"],
        ),
        (
            "legacy-autostart-note-security-boundary",
            "agv:ros:package:bringup",
            "reference",
            55,
            "legacy-reference-only",
            "旧式主机启动流程与 bringup 部署语义弱相关。",
            ["未确认三号车使用 NFS、rc.local 或该权限设置"],
        ),
    ]
)


def build_matches() -> list[dict[str, Any]]:
    claims_by_slug = {claim["slug"]: claim for claim in CLAIMS}
    matches: list[dict[str, Any]] = []
    for index, spec in enumerate(MATCH_SPECS, start=1):
        claim_slug, target_uid, relation, score, implementation, reason, *optional = spec
        conflicts = optional[0] if optional else []
        if claim_slug not in claims_by_slug or target_uid not in TARGETS:
            raise KeyError(f"Unknown claim or target in match {index}")
        if conflicts or 75 <= score < 90:
            match_status = "needs-review"
        elif score >= 90:
            match_status = "accepted"
        elif score >= 55:
            match_status = "weak-candidate"
        else:
            match_status = "rejected"
        matches.append(
            {
                "match_id": f"agv:match:{index:03d}",
                "page_name": f"M{index:03d}-{claims_by_slug[claim_slug]['title']}-{TARGETS[target_uid]['title']}",
                "left_entity": claims_by_slug[claim_slug]["claim_id"],
                "right_entity": target_uid,
                "target_snapshot": "code-v1",
                "relation": relation,
                "match_score": score,
                "match_probability": score / 100,
                "match_status": match_status,
                "match_reasons": [reason],
                "match_keys": claims_by_slug[claim_slug]["keys"],
                "conflicts": conflicts,
                "assertion_state": claims_by_slug[claim_slug]["state"],
                "authority": claims_by_slug[claim_slug]["authority"],
                "implementation_evidence": implementation,
            }
        )
    return matches


def yaml_value(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return json.dumps(value, ensure_ascii=False)


def safe_page_filename(name: str) -> str:
    cleaned = re.sub(r'[<>:"/\\|?*]', "-", name).strip().rstrip(".")
    cleaned = re.sub(r"\s+", " ", cleaned)
    if len(cleaned) > 120:
        suffix = hashlib.sha256(cleaned.encode("utf-8")).hexdigest()[:10]
        cleaned = f"{cleaned[:108].rstrip()}-{suffix}"
    return f"{cleaned}.md"


def wikilink(path: str, title: str | None = None) -> str:
    target = path[:-3] if path.endswith(".md") else path
    return f"[[{target}|{title}]]" if title else f"[[{target}]]"


def write_text(root: Path, relative: str, content: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8", newline="\n")


def write_jsonl(root: Path, relative: str, records: list[dict[str, Any]]) -> None:
    text = "\n".join(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")) for record in records)
    write_text(root, relative, text)


def frontmatter(fields: list[tuple[str, Any]]) -> str:
    lines = ["---"]
    for key, value in fields:
        lines.append(f"{key}: {yaml_value(value)}")
    lines.append("---")
    return "\n".join(lines)


def source_page_path(source: dict[str, Any]) -> str:
    branch = "Learning" if source["source_collection"].endswith("vehicle-learning") else "ROS_Project"
    return f"11_Engineering_Materials/Sources/{branch}/{safe_page_filename(source['page_name'])}"


def claim_page_path(claim: dict[str, Any]) -> str:
    return f"11_Engineering_Materials/Entities/{safe_page_filename(claim['page_name'])}"


def match_page_path(match: dict[str, Any]) -> str:
    return f"11_Engineering_Materials/Matches/{safe_page_filename(match['page_name'])}"


def render_source_page(source: dict[str, Any], linked_claims: list[dict[str, Any]]) -> str:
    aliases = source.get("duplicate_aliases", [])
    alias_lines = "\n".join(f"- `{alias}`" for alias in aliases) if aliases else "- 无。"
    content_mirrors = source.get("content_mirrors_excluded", [])
    content_mirror_metadata = {
        item["source_path"]: item for item in source.get("content_mirror_metadata", [])
    }
    content_mirror_lines = (
        "\n".join(
            f"- `{path}`；SHA-256 `{content_mirror_metadata[path]['source_hash']}`"
            for path in content_mirrors
        )
        if content_mirrors
        else "- 无。"
    )
    key_lines = "\n".join(f"- `{key}`" for key in source["technical_keys"]) or "- 暂无；仅登记元数据。"
    claim_lines = (
        "\n".join(f"- {wikilink(claim_page_path(claim), claim['title'])}" for claim in linked_claims)
        if linked_claims
        else "- 尚未抽取原子工程结论。"
    )
    collection_path = (
        "11_Engineering_Materials/Collections/车辆学习资料"
        if source["source_collection"].endswith("vehicle-learning")
        else "11_Engineering_Materials/Collections/ROS工程文件"
    )
    fields = [
        ("id", source["source_id"]),
        ("type", "source_document"),
        ("status", "active"),
        ("review", "generated"),
        ("project", "AGV"),
        ("source_id", source["source_id"]),
        ("source_collection", source["source_collection"]),
        ("source_kind", source["source_kind"]),
        ("source_path", source["source_path"]),
        ("source_hash", source["source_hash"]),
        ("source_size", source["source_size"]),
        ("source_modified", source["source_modified"]),
        ("authority", source["authority"]),
        ("confidentiality", source["confidentiality"]),
        ("extraction_status", source["extraction_status"]),
        ("duplicate_aliases", aliases),
        ("content_mirrors_excluded", content_mirrors),
    ]
    if source.get("model_scope"):
        fields.append(("model_scope", source["model_scope"]))
    if "page_count" in source:
        fields.append(("page_count", source["page_count"]))
    fields.extend([("updated", UPDATED), ("tags", ["AGV", "工程资料", "来源节点"])])
    return f"""{frontmatter(fields)}

# {source['title']}

## 资料身份

- 所属集合：{wikilink(collection_path)}
- 原始路径：`{source['source_path']}`
- SHA-256：`{source['source_hash']}`
- 大小：`{source['source_size']}` 字节
- 抽取状态：`{source['extraction_status']}`

## 内容范围

{source['summary']}

## 可匹配技术标识

{key_lines}

## 重复别名

{alias_lines}

## 已排除内容镜像

{content_mirror_lines}

## 模型与实现边界

- 模型范围：{source.get('model_scope') or '项目或通用工程资料。'}
- 实现边界：{source.get('implementation_boundary') or '按结论节点的事实状态和适用快照解释，不跨版本外推。'}

## 已抽取结论

{claim_lines}

## 安全与版权边界

{source['copyright_boundary']}

本节点不包含原始附件、账号、网络配置、密码、密钥或可直接执行的危险维护命令。

## 关联

- {wikilink("11_Engineering_Materials/_index", "工程资料与匹配工作台")}
"""


def render_claim_page(
    claim: dict[str, Any], source: dict[str, Any], linked_matches: list[dict[str, Any]]
) -> str:
    match_lines = (
        "\n".join(
            f"- {wikilink(match_page_path(match), match['relation'] + ' → ' + TARGETS[match['right_entity']]['title'])}"
            for match in linked_matches
        )
        if linked_matches
        else "- 尚无候选匹配。"
    )
    fields = [
        ("id", claim["claim_id"]),
        ("type", "engineering_claim"),
        ("status", "active"),
        ("review", "generated"),
        ("project", "AGV"),
        ("claim_id", claim["claim_id"]),
        ("derived_from", source["source_id"]),
        ("source_locator", claim["locator"]),
        ("authority", claim["authority"]),
        ("assertion_state", claim["state"]),
        ("applies_to_snapshot", claim["snapshot"]),
        ("technical_keys", claim["keys"]),
        ("updated", UPDATED),
        ("tags", ["AGV", "工程结论", claim["state"]]),
    ]
    return f"""{frontmatter(fields)}

# {claim['title']}

## 原子结论

{claim['summary']}

## 来源定位

- 来源：{wikilink(source_page_path(source), source['title'])}
- 定位：{claim['locator']}
- 来源权威级别：`{claim['authority']}`

## 适用范围

- 事实状态：`{claim['state']}`
- 适用快照：`{claim['snapshot']}`

## 证据与限制

{claim['limits']}

## 候选关系

{match_lines}
"""


def render_match_page(match: dict[str, Any], claim: dict[str, Any]) -> str:
    target = TARGETS[match["right_entity"]]
    reason_lines = "\n".join(f"- {reason}" for reason in match["match_reasons"])
    conflict_lines = "\n".join(f"- {item}" for item in match["conflicts"]) if match["conflicts"] else "- 无身份冲突。"
    fields = [
        ("id", match["match_id"]),
        ("type", "match_record"),
        ("status", "active"),
        ("review", "generated"),
        ("project", "AGV"),
        ("left_entity", match["left_entity"]),
        ("right_entity", match["right_entity"]),
        ("target_snapshot", match["target_snapshot"]),
        ("relation", match["relation"]),
        ("match_score", match["match_score"]),
        ("match_probability", match["match_probability"]),
        ("match_status", match["match_status"]),
        ("match_reasons", match["match_reasons"]),
        ("match_keys", match["match_keys"]),
        ("conflicts", match["conflicts"]),
        ("assertion_state", match["assertion_state"]),
        ("authority", match["authority"]),
        ("implementation_evidence", match["implementation_evidence"]),
        ("updated", UPDATED),
        ("tags", ["AGV", "图谱匹配", match["match_status"]]),
    ]
    return f"""{frontmatter(fields)}

# {claim['title']} → {target['title']}

## 匹配结论

- 左侧工程结论：{wikilink(claim_page_path(claim), claim['title'])}
- 右侧代码实体：{wikilink(target['path'], target['title'])}
- 关系：`{match['relation']}`
- 匹配概率：**{match['match_score']}%**
- 匹配状态：`{match['match_status']}`
- 实现证据：`{match['implementation_evidence']}`

## 评分依据

{reason_lines}

评分遵循 [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]；概率衡量“是否匹配到该实体”，不等于“方案已经实现”。

## 支持证据

- 来源定位保存在左侧工程结论节点。
- 目标实体身份取自不可变 `code-v1` 机器清单。

## 冲突与限制

{conflict_lines}

## 复核记录

- 生成日期：{UPDATED}
- 当前结论：`{match['match_status']}`
"""


def render_ros_coverage_report(coverage: dict[str, Any]) -> str:
    inventory = coverage["inventory"]
    top_rows = [
        "| 顶层范围 | 类型 | 文件 | 目录 | 字节 | 已纳入规范来源 |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for row in coverage["top_level_scope"]:
        top_rows.append(
            "| {name} | {kind} | {files} | {dirs} | {bytes_} | {included} |".format(
                name=row["name"].replace("|", "\\|"),
                kind=row["entry_kind"],
                files=row["file_count"],
                dirs=row["directory_count"],
                bytes_=row["total_bytes"],
                included=row["categories"].get("included_curated_source", 0),
            )
        )
    category_rows = [
        "| 分类 | 处置 | 文件 | 字节 | 原因 |",
        "|---|---|---:|---:|---|",
    ]
    for row in coverage["category_summary"]:
        category_rows.append(
            "| `{category}` | `{disposition}` | {files} | {bytes_} | {reason} |".format(
                category=row["category"],
                disposition=row["disposition"],
                files=row["file_count"],
                bytes_=row["total_bytes"],
                reason=row["reason"].replace("|", "\\|"),
            )
        )
    return f"""{frontmatter([('id', coverage['coverage_id']), ('type', 'coverage_report'), ('status', 'active'), ('review', 'verified'), ('project', 'AGV'), ('updated', UPDATED), ('tags', ['AGV', '工程资料', '覆盖审计', '排除规则'])])}

# ROS工程文件全树覆盖与排除报告

## 结论

- 根目录：`{coverage['root']}`
- 全树文件：**{inventory['file_count']}**；目录：**{inventory['directory_count']}**；总字节：**{inventory['total_bytes']}**。
- 规范来源：**{coverage['curated_canonical_source_count']}**；其中历史子目录之外新增 **{coverage['curated_outside_historical_subroot_count']}** 个。
- 已登记字节级重复别名：**{coverage['registered_duplicate_alias_count']}**；排除内容镜像：**{coverage['excluded_content_mirror_count']}**；排除被更新版本：**{coverage['excluded_superseded_revision_count']}**。
- 文件和字节守恒：`{str(coverage['accounting']['all_files_accounted_for']).lower()}`。
- 盘点指纹：`{inventory['inventory_fingerprint']}`。

这份报告对整个 `D:\\ROS工程文件` 做分类守恒盘点，但只把经内容核验、与推料车有直接工程价值且不重复的少量资料登记为来源节点。

## 顶层范围

{chr(10).join(top_rows)}

## 分类与排除规则

{chr(10).join(category_rows)}

## 模型与证据边界

- C10B、L150、R3mini 和其他厂商参考平台只能形成 `reference` / `related_theory`，不能成为三号车当前代码的实现证据。
- 匹配概率只表示语义或实体关系命中概率；`implementation_evidence` 单独记录，并对这些资料固定为 `reference-model-mismatch`、`theory-only` 或 `legacy-reference-only`。
- `SolidWorks 2025 64bit`、Visio 安装/激活工具、可执行文件、压缩包、镜像、视频和未完成下载均不读取或执行。
- R550A 机械臂/MoveIt、通用教程、代码镜像、`node_modules`、`build/devel/install` 不进入资料图谱。
- 账号、网络值、Wi-Fi、密钥、日志、bag、轨迹和其他运行数据不摄取。
- 不复制 PDF、图片、源代码或长摘录；只保存哈希、定位和原创摘要。

## 机器清单

- `11_Engineering_Materials/_data/ros-source-coverage.json`

## 关联

- {wikilink('11_Engineering_Materials/Collections/ROS工程文件')}
- {wikilink('11_Engineering_Materials/_index', '工程资料与匹配工作台')}
"""


def build_graph(output_root: Path) -> dict[str, Any]:
    sources = discover_sources()
    ros_coverage = build_ros_coverage(sources)
    if not ros_coverage["accounting"]["all_files_accounted_for"]:
        raise ValueError("ROS engineering-file coverage scan did not account for the full tree")
    claims = sorted(CLAIMS, key=lambda item: item["claim_id"])
    matches = build_matches()
    sources_by_id = {item["source_id"]: item for item in sources}
    claims_by_id = {item["claim_id"]: item for item in claims}

    for source in sources:
        linked_claims = [claim for claim in claims if claim["source"] == source["source_id"]]
        write_text(output_root, source_page_path(source), render_source_page(source, linked_claims))

    for claim in claims:
        if claim["source"] not in sources_by_id:
            raise KeyError(f"Unknown source for claim {claim['claim_id']}")
        linked_matches = [match for match in matches if match["left_entity"] == claim["claim_id"]]
        write_text(
            output_root,
            claim_page_path(claim),
            render_claim_page(claim, sources_by_id[claim["source"]], linked_matches),
        )

    for match in matches:
        write_text(
            output_root,
            match_page_path(match),
            render_match_page(match, claims_by_id[match["left_entity"]]),
        )

    write_text(
        output_root,
        "11_Engineering_Materials/Collections/ROS工程文件全树覆盖与排除报告.md",
        render_ros_coverage_report(ros_coverage),
    )

    learning_sources = [s for s in sources if s["source_collection"].endswith("vehicle-learning")]
    ros_sources = [s for s in sources if s["source_collection"].endswith("ros-engineering-files")]
    collection_common = [
        ("type", "source_collection"),
        ("status", "active"),
        ("review", "verified"),
        ("project", "AGV"),
        ("updated", UPDATED),
        ("tags", ["AGV", "工程资料", "资料集合"]),
    ]
    learning_collection = f"""{frontmatter([('id', 'agv:source-collection:vehicle-learning'), *collection_common])}

# 车辆学习资料

## 物理盘点

- 根目录：`D:\\推料车项目\\9.车辆学习资料`
- 物理文件：24（22 PDF、2 EPUB）
- 规范来源节点：{len(learning_sources)}
- 重复组：1；两份《机械设计（Robert Norton）》按 SHA-256 合并为一个规范节点和一个别名。
- 总体积：约 1.915 GiB。

## 摄取原则

- 教材只能形成 `reference` / `related_theory`，不能证明项目选型或代码实现。
- 23/24 文件名带非官方电子书站标记，授权状态未核验；Vault 不复制附件、图片或长摘录。
- 只保存书目、哈希、页码定位和原创工程摘要。

## 来源节点

```dataview
TABLE extraction_status AS 抽取状态, authority AS 权威级别, page_count AS 页数
FROM "11_Engineering_Materials/Sources/Learning"
WHERE type = "source_document"
SORT file.name ASC
```

- {wikilink('11_Engineering_Materials/_index', '返回工程资料工作台')}
"""
    ros_collection = f"""{frontmatter([('id', 'agv:source-collection:ros-engineering-files'), *collection_common])}

# ROS工程文件

## 物理盘点

- 根目录：`D:\\ROS工程文件`
- 全树：{ros_coverage['inventory']['file_count']} 文件、{ros_coverage['inventory']['directory_count']} 目录、{ros_coverage['inventory']['total_bytes']} 字节。
- 本轮规范来源节点：{len(ros_sources)}；其中历史 `推料车项目树莓派移植` 子目录之外 {ros_coverage['curated_outside_historical_subroot_count']} 个。
- 全量分类守恒与顶层覆盖见 {wikilink('11_Engineering_Materials/Collections/ROS工程文件全树覆盖与排除报告')}。
- 大型 ZIP、视频、安装器、虚拟机、日志与轨迹数据不进入 Vault。

## 明确排除

- `Renew/src`、`Renew/src-claude`、`Renew/src-codex`、`Renew/sensor2_ws-master` 是代码副本，不作为资料图谱的第二代码基线；最新代码只由独立 V2 扫描处理。
- 根目录 README、考试系统部署文档、Wi-Fi 配置、账号/密码/密钥或其值不摄取。
- `SolidWorks 2025 64bit`、安装器、激活工具、可执行文件、压缩包、视频、bag、node_modules、build/devel 全部排除。
- `ROS资料最新` 中的 R550A 机械臂/MoveIt 与无关平台资料排除；通用教程和代码镜像也不作为工程实现证据。
- C10B、L150、R3mini 只作为参考平台；其主张仅使用 `reference` / `related_theory`，不能证明三号车当前实现。
- 采购明细在按电子表格安全流程读取前仅登记哈希，不抽取价格、联系人或供应商。

## 来源节点

```dataview
TABLE source_kind AS 类型, extraction_status AS 抽取状态, authority AS 权威级别
FROM "11_Engineering_Materials/Sources/ROS_Project"
WHERE type = "source_document"
SORT file.name ASC
```

- {wikilink('11_Engineering_Materials/_index', '返回工程资料工作台')}
"""
    write_text(output_root, "11_Engineering_Materials/Collections/车辆学习资料.md", learning_collection)
    write_text(output_root, "11_Engineering_Materials/Collections/ROS工程文件.md", ros_collection)

    write_text(
        output_root,
        "11_Engineering_Materials/Sources/_index.md",
        f"""{frontmatter([('id', 'agv:index:material-sources'), ('type', 'index'), ('status', 'active'), ('review', 'generated'), ('project', 'AGV'), ('updated', UPDATED), ('tags', ['AGV', '工程资料', '来源'])])}

# 工程资料来源

- {wikilink('11_Engineering_Materials/Collections/车辆学习资料')}
- {wikilink('11_Engineering_Materials/Collections/ROS工程文件')}

```dataview
TABLE source_collection AS 集合, source_kind AS 类型, extraction_status AS 抽取状态, authority AS 权威级别
FROM "11_Engineering_Materials/Sources"
WHERE type = "source_document"
SORT file.name ASC
```
""",
    )
    write_text(
        output_root,
        "11_Engineering_Materials/Entities/_index.md",
        f"""{frontmatter([('id', 'agv:index:material-claims'), ('type', 'index'), ('status', 'active'), ('review', 'generated'), ('project', 'AGV'), ('updated', UPDATED), ('tags', ['AGV', '工程结论'])])}

# 工程结论

```dataview
TABLE assertion_state AS 事实状态, authority AS 权威级别, applies_to_snapshot AS 适用快照
FROM "11_Engineering_Materials/Entities"
WHERE type = "engineering_claim"
SORT assertion_state ASC, file.name ASC
```
""",
    )
    write_text(
        output_root,
        "11_Engineering_Materials/Matches/_index.md",
        f"""{frontmatter([('id', 'agv:index:material-matches'), ('type', 'index'), ('status', 'active'), ('review', 'generated'), ('project', 'AGV'), ('updated', UPDATED), ('tags', ['AGV', '图谱匹配'])])}

# 资料到代码的匹配记录

匹配概率描述实体身份或关系命中的概率；`implementation_evidence` 单独表示是否存在实现证据。

```dataview
TABLE relation AS 关系, match_score AS 匹配概率, match_status AS 状态, implementation_evidence AS 实现证据
FROM "11_Engineering_Materials/Matches"
WHERE type = "match_record"
SORT match_score DESC, file.name ASC
```
""",
    )

    index_page = f"""{frontmatter([('id', 'agv:index:engineering-materials'), ('type', 'index'), ('status', 'active'), ('review', 'verified'), ('project', 'AGV'), ('updated', UPDATED), ('tags', ['AGV', '工程资料', '证据', '匹配'])])}

# 工程资料与匹配工作台

本图谱把外部资料保留为独立证据层，不覆盖代码图谱。当前已登记 **{len(sources)}** 个规范来源、**{len(claims)}** 条原子工程结论和 **{len(matches)}** 条带概率的资料→代码匹配。

## 快速入口

- {wikilink('11_Engineering_Materials/Collections/车辆学习资料')}
- {wikilink('11_Engineering_Materials/Collections/ROS工程文件')}
- {wikilink('11_Engineering_Materials/Sources/_index', '来源目录')}
- {wikilink('11_Engineering_Materials/Entities/_index', '工程结论目录')}
- {wikilink('11_Engineering_Materials/Matches/_index', '匹配记录目录')}
- [[11_Engineering_Materials/工程资料匹配概览.canvas|工程资料匹配概览]]

## 待复核匹配

```dataview
TABLE relation AS 关系, match_score AS 概率, implementation_evidence AS 实现证据, conflicts AS 冲突
FROM "11_Engineering_Materials/Matches"
WHERE type = "match_record" AND match_status != "accepted"
SORT match_score DESC
```

## 规则

- [[00_System/Decisions/ADR-001-工程资料与代码实体匹配]]
- 只保存资料摘要、定位和哈希，不复制大型原文件。
- 匹配概率与“是否已经实现”分开判断。
- `planned` 和 `reference` 只能建立提案或理论关系。
- V1 不被覆盖；V2 作为独立快照与 V1 比较。

- [[研发图谱工作台|返回研发图谱工作台]]
"""
    write_text(output_root, "11_Engineering_Materials/_index.md", index_page)

    canvas = {
        "nodes": [
            {"id": "learning", "type": "file", "file": "11_Engineering_Materials/Collections/车辆学习资料.md", "x": -720, "y": -200, "width": 340, "height": 220},
            {"id": "ros", "type": "file", "file": "11_Engineering_Materials/Collections/ROS工程文件.md", "x": -720, "y": 120, "width": 340, "height": 220},
            {"id": "sources", "type": "file", "file": "11_Engineering_Materials/Sources/_index.md", "x": -250, "y": -40, "width": 320, "height": 220},
            {"id": "claims", "type": "file", "file": "11_Engineering_Materials/Entities/_index.md", "x": 210, "y": -40, "width": 320, "height": 220},
            {"id": "matches", "type": "file", "file": "11_Engineering_Materials/Matches/_index.md", "x": 670, "y": -40, "width": 320, "height": 220},
            {"id": "codev1", "type": "file", "file": "00_System/Graph_History/Snapshots/code-v1/V1基线说明.md", "x": 1130, "y": -40, "width": 340, "height": 220},
            {"id": "rule", "type": "text", "text": "匹配概率 ≠ 已实现\n来源、主张、匹配和代码实体保持独立。", "x": 420, "y": 280, "width": 430, "height": 180, "color": "4"},
        ],
        "edges": [
            {"id": "e1", "fromNode": "learning", "toNode": "sources", "label": "登记"},
            {"id": "e2", "fromNode": "ros", "toNode": "sources", "label": "筛选/去重/脱敏"},
            {"id": "e3", "fromNode": "sources", "toNode": "claims", "label": "定位后抽取"},
            {"id": "e4", "fromNode": "claims", "toNode": "matches", "label": "评分"},
            {"id": "e5", "fromNode": "matches", "toNode": "codev1", "label": "稳定ID匹配"},
            {"id": "e6", "fromNode": "rule", "toNode": "matches", "label": "约束"},
        ],
    }
    write_text(output_root, "11_Engineering_Materials/工程资料匹配概览.canvas", json.dumps(canvas, ensure_ascii=False, indent=2, sort_keys=True))

    source_records = [
        {key: value for key, value in source.items() if key not in {"page_name", "copyright_boundary"}}
        | {"vault_path": source_page_path(source)}
        for source in sources
    ]
    claim_records = [
        {key: value for key, value in claim.items() if key != "page_name"}
        | {"vault_path": claim_page_path(claim)}
        for claim in claims
    ]
    match_records = [match | {"vault_path": match_page_path(match)} for match in matches]
    relations: list[dict[str, Any]] = []
    for claim in claims:
        relations.append(
            {
                "from_entity_uid": claim["source"],
                "predicate": "supports_claim",
                "to_entity_uid": claim["claim_id"],
                "source_locator": claim["locator"],
            }
        )
    for match in matches:
        relations.append(
            {
                "from_entity_uid": match["left_entity"],
                "predicate": match["relation"],
                "to_entity_uid": match["right_entity"],
                "match_score": match["match_score"],
                "match_status": match["match_status"],
                "implementation_evidence": match["implementation_evidence"],
            }
        )
    relations.sort(key=lambda item: (item["from_entity_uid"], item["predicate"], item["to_entity_uid"]))

    data_dir = "11_Engineering_Materials/_data"
    write_jsonl(output_root, f"{data_dir}/sources.jsonl", source_records)
    write_jsonl(output_root, f"{data_dir}/claims.jsonl", claim_records)
    write_jsonl(output_root, f"{data_dir}/matches.jsonl", match_records)
    write_jsonl(output_root, f"{data_dir}/relations.jsonl", relations)
    write_text(
        output_root,
        f"{data_dir}/ros-source-coverage.json",
        json.dumps(ros_coverage, ensure_ascii=False, indent=2, sort_keys=True),
    )

    fingerprints: dict[str, str] = {}
    for name in (
        "sources.jsonl",
        "claims.jsonl",
        "matches.jsonl",
        "relations.jsonl",
        "ros-source-coverage.json",
    ):
        data = (output_root / data_dir / name).read_bytes()
        fingerprints[name] = hashlib.sha256(data).hexdigest()
    combined = "\n".join(f"{name}\t{fingerprints[name]}" for name in sorted(fingerprints))
    manifest = {
        "graph_id": "agv:material-graph:v1",
        "schema_version": "1.0.0",
        "generated": UPDATED,
        "source_count": len(sources),
        "claim_count": len(claims),
        "match_count": len(matches),
        "relation_count": len(relations),
        "accepted_match_count": sum(match["match_status"] == "accepted" for match in matches),
        "needs_review_match_count": sum(match["match_status"] == "needs-review" for match in matches),
        "weak_candidate_count": sum(match["match_status"] == "weak-candidate" for match in matches),
        "duplicate_alias_count": sum(len(source["duplicate_aliases"]) for source in sources),
        "fingerprints": fingerprints,
        "graph_fingerprint": hashlib.sha256(combined.encode("utf-8")).hexdigest(),
        "source_roots": [str(LEARNING_ROOT), str(ROS_ROOT.parent)],
        "excluded_code_trees": ["Renew/src", "Renew/src-claude", "Renew/src-codex", "Renew/sensor2_ws-master"],
        "security_boundary": "no credentials, network secrets, executable installers, archives, raw logs, trajectories, or copied attachments",
        "ros_coverage": {
            "file_count": ros_coverage["inventory"]["file_count"],
            "directory_count": ros_coverage["inventory"]["directory_count"],
            "total_bytes": ros_coverage["inventory"]["total_bytes"],
            "curated_canonical_source_count": ros_coverage["curated_canonical_source_count"],
            "curated_outside_historical_subroot_count": ros_coverage["curated_outside_historical_subroot_count"],
            "inventory_fingerprint": ros_coverage["inventory"]["inventory_fingerprint"],
            "all_files_accounted_for": ros_coverage["accounting"]["all_files_accounted_for"],
        },
    }
    write_text(output_root, f"{data_dir}/manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True))

    result = {
        "source_count": len(sources),
        "claim_count": len(claims),
        "match_count": len(matches),
        "relation_count": len(relations),
        "duplicate_alias_count": manifest["duplicate_alias_count"],
        "ros_coverage_file_count": ros_coverage["inventory"]["file_count"],
        "ros_curated_source_count": ros_coverage["curated_canonical_source_count"],
        "graph_fingerprint": manifest["graph_fingerprint"],
    }
    validation = validate_graph(output_root)
    if validation["errors"]:
        raise ValueError("Generated graph failed validation: " + "; ".join(validation["errors"]))
    return result


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def validate_graph(output_root: Path) -> dict[str, Any]:
    data_dir = output_root / "11_Engineering_Materials/_data"
    errors: list[str] = []
    required = [
        "sources.jsonl",
        "claims.jsonl",
        "matches.jsonl",
        "relations.jsonl",
        "ros-source-coverage.json",
        "manifest.json",
    ]
    for name in required:
        if not (data_dir / name).is_file():
            errors.append(f"missing machine file: {name}")
    if errors:
        return {"errors": errors, "source_count": 0, "claim_count": 0, "match_count": 0}

    sources = read_jsonl(data_dir / "sources.jsonl")
    claims = read_jsonl(data_dir / "claims.jsonl")
    matches = read_jsonl(data_dir / "matches.jsonl")
    relations = read_jsonl(data_dir / "relations.jsonl")
    coverage = json.loads((data_dir / "ros-source-coverage.json").read_text(encoding="utf-8"))
    source_ids = [item["source_id"] for item in sources]
    claim_ids = [item["claim_id"] for item in claims]
    match_ids = [item["match_id"] for item in matches]
    if len(source_ids) != len(set(source_ids)):
        errors.append("duplicate source_id")
    if len(claim_ids) != len(set(claim_ids)):
        errors.append("duplicate claim_id")
    if len(match_ids) != len(set(match_ids)):
        errors.append("duplicate match_id")

    source_id_set, claim_id_set = set(source_ids), set(claim_ids)
    sources_by_id = {item["source_id"]: item for item in sources}
    claims_by_id = {item["claim_id"]: item for item in claims}
    for claim in claims:
        if claim["source"] not in source_id_set:
            errors.append(f"unresolved claim source: {claim['claim_id']}")
    for match in matches:
        if match["left_entity"] not in claim_id_set:
            errors.append(f"unresolved match claim: {match['match_id']}")
        if match["right_entity"] not in TARGETS:
            errors.append(f"unresolved match target: {match['match_id']}")
        if abs(match["match_probability"] - match["match_score"] / 100) > 1e-9:
            errors.append(f"probability/score mismatch: {match['match_id']}")
        if not 0 <= match["match_score"] <= 100:
            errors.append(f"invalid match score: {match['match_id']}")
        claim = claims_by_id.get(match["left_entity"])
        if claim and (
            claim["snapshot"].startswith("vendor-reference-")
            or claim["snapshot"].startswith("legacy-reference-")
        ):
            if match["relation"] not in {"reference", "related_theory", "proposes"}:
                errors.append(f"reference material uses implementation predicate: {match['match_id']}")
            if match["implementation_evidence"] not in {
                "reference-model-mismatch",
                "theory-only",
                "legacy-reference-only",
            }:
                errors.append(f"reference material treated as implementation evidence: {match['match_id']}")

    forbidden_material_paths = [
        re.compile(r"\\Renew\\src(?:\\|$)", re.IGNORECASE),
        re.compile(r"\\Renew\\src-claude(?:\\|$)", re.IGNORECASE),
        re.compile(r"\\Renew\\src-codex(?:\\|$)", re.IGNORECASE),
        re.compile(r"\\Renew\\sensor2_ws-master(?:\\|$)", re.IGNORECASE),
    ]
    forbidden_names = {"README.md", "CODEX_MEMORY_exam_system_linux_deploy.md", "pi-wifi-receive.txt"}
    for source in sources:
        source_path = source["source_path"]
        if any(pattern.search(source_path) for pattern in forbidden_material_paths):
            errors.append(f"code tree ingested as material: {source['source_id']}")
        if Path(source_path).name in forbidden_names:
            errors.append(f"security-excluded file ingested: {source['source_id']}")
        if not re.fullmatch(r"[0-9a-f]{64}", source["source_hash"]):
            errors.append(f"invalid source hash: {source['source_id']}")
        for mirror in source.get("content_mirrors_excluded", []):
            if not Path(mirror).is_file():
                errors.append(f"missing excluded content mirror: {source['source_id']}")
            if mirror == source_path:
                errors.append(f"canonical source listed as excluded mirror: {source['source_id']}")
        for mirror in source.get("content_mirror_metadata", []):
            if not re.fullmatch(r"[0-9a-f]{64}", mirror.get("source_hash", "")):
                errors.append(f"invalid excluded mirror hash: {source['source_id']}")
            if mirror.get("source_path") not in source.get("content_mirrors_excluded", []):
                errors.append(f"unlinked excluded mirror metadata: {source['source_id']}")
        if not (output_root / source["vault_path"]).is_file():
            errors.append(f"missing source page: {source['source_id']}")
    for claim in claims:
        if not (output_root / claim["vault_path"]).is_file():
            errors.append(f"missing claim page: {claim['claim_id']}")
    for match in matches:
        if not (output_root / match["vault_path"]).is_file():
            errors.append(f"missing match page: {match['match_id']}")

    expected_relation_count = len(claims) + len(matches)
    if len(relations) != expected_relation_count:
        errors.append(f"relation count mismatch: {len(relations)} != {expected_relation_count}")

    inventory = coverage.get("inventory", {})
    accounting = coverage.get("accounting", {})
    category_summary = coverage.get("category_summary", [])
    if coverage.get("root") != str(ROS_INVENTORY_ROOT):
        errors.append("ROS coverage root mismatch")
    if inventory.get("walk_errors"):
        errors.append("ROS coverage contains walk errors")
    if not accounting.get("all_files_accounted_for"):
        errors.append("ROS coverage accounting is not conservative")
    if sum(row.get("file_count", 0) for row in category_summary) != inventory.get("file_count"):
        errors.append("ROS coverage file-count conservation mismatch")
    if sum(row.get("total_bytes", 0) for row in category_summary) != inventory.get("total_bytes"):
        errors.append("ROS coverage byte-count conservation mismatch")
    ros_source_count = sum(
        1
        for source in sources
        if source["source_collection"].endswith("ros-engineering-files")
    )
    if coverage.get("curated_canonical_source_count") != ros_source_count:
        errors.append("ROS coverage curated-source count mismatch")
    if not re.fullmatch(r"[0-9a-f]{64}", inventory.get("inventory_fingerprint", "")):
        errors.append("invalid ROS inventory fingerprint")
    coverage_page = output_root / "11_Engineering_Materials/Collections/ROS工程文件全树覆盖与排除报告.md"
    if not coverage_page.is_file():
        errors.append("missing human-readable ROS coverage report")

    material_root = output_root / "11_Engineering_Materials"
    available_links = {
        path.relative_to(output_root).as_posix().removesuffix(path.suffix)
        for path in material_root.rglob("*")
        if path.is_file() and path.suffix in {".md", ".canvas"}
    }
    available_links.update(path["path"].removesuffix(".md") for path in TARGETS.values())
    available_links.update(
        {
            "00_System/Decisions/ADR-001-工程资料与代码实体匹配",
            "00_System/Graph_History/Snapshots/code-v1/V1基线说明",
            "研发图谱工作台",
        }
    )
    for page in material_root.rglob("*.md"):
        content = page.read_text(encoding="utf-8")
        for raw_link in re.findall(r"\[\[([^\]]+)\]\]", content):
            target = raw_link.split("|", 1)[0].split("#", 1)[0].replace("\\", "/").strip()
            target = target.removesuffix(".md").removesuffix(".canvas")
            if target and target not in available_links:
                errors.append(f"unresolved wikilink in {page.relative_to(output_root).as_posix()}: {target}")

    canvas_path = material_root / "工程资料匹配概览.canvas"
    if canvas_path.is_file():
        canvas = json.loads(canvas_path.read_text(encoding="utf-8"))
        for node in canvas.get("nodes", []):
            if node.get("type") == "file":
                target = node["file"].replace("\\", "/")
                normalized = target.removesuffix(".md").removesuffix(".canvas")
                if normalized not in available_links:
                    errors.append(f"unresolved canvas file node: {target}")

    generated_text = "\n".join(
        path.read_text(encoding="utf-8", errors="strict")
        for path in (output_root / "11_Engineering_Materials").rglob("*")
        if path.is_file() and path.suffix in {".md", ".json", ".jsonl", ".canvas"}
    )
    secret_patterns = [
        re.compile(r"(?i)(?:password|passwd|token|secret)\s*[:=]\s*['\"]?[^\s'\"]{4,}"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ]
    for pattern in secret_patterns:
        if pattern.search(generated_text):
            errors.append(f"secret-like value detected by {pattern.pattern}")

    manifest = json.loads((data_dir / "manifest.json").read_text(encoding="utf-8"))
    if manifest["source_count"] != len(sources) or manifest["claim_count"] != len(claims) or manifest["match_count"] != len(matches):
        errors.append("manifest count mismatch")
    for name, expected in manifest["fingerprints"].items():
        actual = hashlib.sha256((data_dir / name).read_bytes()).hexdigest()
        if actual != expected:
            errors.append(f"fingerprint mismatch: {name}")
    manifest_coverage = manifest.get("ros_coverage", {})
    if manifest_coverage.get("inventory_fingerprint") != inventory.get("inventory_fingerprint"):
        errors.append("manifest ROS coverage fingerprint mismatch")

    return {
        "errors": errors,
        "source_count": len(sources),
        "claim_count": len(claims),
        "match_count": len(matches),
        "relation_count": len(relations),
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    if args.validate_only:
        print(json.dumps(validate_graph(args.output), ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(json.dumps(build_graph(args.output), ensure_ascii=False, indent=2, sort_keys=True))
