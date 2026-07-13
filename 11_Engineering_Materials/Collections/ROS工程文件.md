---
id: "agv:source-collection:ros-engineering-files"
type: "source_collection"
status: "active"
review: "verified"
project: "AGV"
updated: "2026-07-14"
tags: ["AGV", "工程资料", "资料集合"]
---

# ROS工程文件

## 物理盘点

- 根目录：`D:\ROS工程文件`
- 全树：23,256 文件、2,678 目录、约 121.229 GiB。
- 本轮规范来源节点：20；只登记推料车直接相关的架构文档、厂商协议、调试记录、方案与采购明细元数据。
- 大型 ZIP、视频、安装器、虚拟机、日志与轨迹数据不进入 Vault。

## 明确排除

- `Renew/src`、`Renew/src-claude`、`Renew/src-codex`、`Renew/sensor2_ws-master` 是代码副本，不作为资料图谱的第二代码基线；最新代码只由独立 V2 扫描处理。
- 根目录 README、考试系统部署文档、Wi-Fi 配置、账号/密码/密钥或其值不摄取。
- `SolidWorks 2025 64bit`、安装器、激活工具、可执行文件、压缩包、视频、bag、node_modules、build/devel 全部排除。
- 采购明细在按电子表格安全流程读取前仅登记哈希，不抽取价格、联系人或供应商。

## 来源节点

```dataview
TABLE source_kind AS 类型, extraction_status AS 抽取状态, authority AS 权威级别
FROM "11_Engineering_Materials/Sources/ROS_Project"
WHERE type = "source_document"
SORT file.name ASC
```

- [[11_Engineering_Materials/_index|返回工程资料工作台]]
