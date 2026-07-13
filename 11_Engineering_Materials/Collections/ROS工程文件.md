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
- 全树：23256 文件、2678 目录、130169126820 字节。
- 本轮规范来源节点：29；其中历史 `推料车项目树莓派移植` 子目录之外 9 个。
- 全量分类守恒与顶层覆盖见 [[11_Engineering_Materials/Collections/ROS工程文件全树覆盖与排除报告]]。
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

- [[11_Engineering_Materials/_index|返回工程资料工作台]]
