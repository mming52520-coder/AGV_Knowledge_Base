---
id: "agv:material-coverage:ros-engineering-files:v1"
type: "coverage_report"
status: "active"
review: "verified"
project: "AGV"
updated: "2026-07-14"
tags: ["AGV", "工程资料", "覆盖审计", "排除规则"]
---

# ROS工程文件全树覆盖与排除报告

## 结论

- 根目录：`D:\ROS工程文件`
- 全树文件：**23256**；目录：**2678**；总字节：**130169126820**。
- 规范来源：**29**；其中历史子目录之外新增 **9** 个。
- 已登记字节级重复别名：**2**；排除内容镜像：**1**；排除被更新版本：**1**。
- 文件和字节守恒：`true`。
- 盘点指纹：`3711a66754c17b097dc3f8d60ff14d47e68fd0fbcac1df39114edbe928d507ca`。

这份报告对整个 `D:\ROS工程文件` 做分类守恒盘点，但只把经内容核验、与推料车有直接工程价值且不重复的少量资料登记为来源节点。

## 顶层范围

| 顶层范围 | 类型 | 文件 | 目录 | 字节 | 已纳入规范来源 |
|---|---:|---:|---:|---:|---:|
| 1.Ubuntu配置教程.pdf | file | 1 | 0 | 5148607 | 0 |
| CP2102修改串口号软件(除串口号，其它不可修改).zip | file | 1 | 0 | 40416933 | 0 |
| ROS主机中设置开机自启动程序.txt | file | 1 | 0 | 487 | 1 |
| ros理论与实践学习 | directory | 5 | 4 | 943500669 | 0 |
| ROS资料最新 | directory | 192 | 97 | 6390679143 | 0 |
| rqt可视化工具集.pdf | file | 1 | 0 | 1401127 | 0 |
| SolidWorks 2025 64bit | directory | 2273 | 191 | 16599615333 | 0 |
| visio安装包和激活工具 | directory | 593 | 37 | 222288591 | 0 |
| WHEELTEC 直流电机附送资料 | directory | 3 | 2 | 699749 | 0 |
| 串口插头连接器.doc | file | 1 | 0 | 610816 | 0 |
| 串口插头连接器.pdf | file | 1 | 0 | 601443 | 0 |
| 二驱C10B | directory | 215 | 124 | 5438269959 | 8 |
| 入门教程-强烈推荐 | directory | 60 | 19 | 3136304695 | 0 |
| 推料车项目树莓派移植 | directory | 19909 | 2204 | 97389589268 | 20 |

## 分类与排除规则

| 分类 | 处置 | 文件 | 字节 | 原因 |
|---|---|---:|---:|---|
| `excluded_archive_or_incomplete_download` | `excluded` | 296 | 71202750310 | 压缩包、磁盘镜像或未完成的云下载；不解压、不执行。 |
| `excluded_code_or_build_mirror` | `excluded` | 15291 | 128415067 | 教程/源码镜像、node_modules、build/devel/install 产物或仓库元数据；代码由独立 V2 扫描处理。 |
| `excluded_duplicate_or_superseded` | `excluded` | 2 | 1160991 | 提取文本等价的镜像或已被更新的版本；仅保留规范或最新来源。 |
| `excluded_generic_or_root_material` | `excluded` | 4 | 7761993 | 无法形成有依据的独特工程主张的根目录或杂项目资料。 |
| `excluded_installer_activation_binary` | `excluded` | 3492 | 18809576261 | 安装器、破解/激活工具、打包应用、可执行文件或二进制依赖。 |
| `excluded_mechanical_arm_or_unrelated_platform` | `excluded` | 192 | 6390679143 | R550A 机械臂/MoveIt 或其他无关平台资料，不属于三号车范围。 |
| `excluded_media_or_image` | `excluded` | 759 | 30819923346 | 视频、音频或批量图片资产；不属于本轮精选语义图谱范围。 |
| `excluded_sensitive_or_runtime_data` | `excluded` | 16 | 618346981 | 凭据/网络配置、日志、bag、轨迹或其他运行数据。 |
| `excluded_tutorial_or_generic_training` | `excluded` | 27 | 250144507 | 通用 ROS/Linux 教程或未完成课程下载，不能为三号车提供直接证据。 |
| `excluded_unselected_model_reference` | `excluded` | 87 | 116013873 | 未选择的 C10B/L150/R3mini 型号资料、重复示例或教程代码；明确保留型号不匹配边界。 |
| `excluded_unselected_project_material` | `excluded` | 3056 | 1761510963 | 经相关性、重复、安全和来源边界审查后未选择的项目树资料。 |
| `excluded_vendor_boilerplate` | `excluded` | 3 | 699749 | 厂商联系、版权或更新说明等样板内容，不含本图谱所需工程信息。 |
| `included_curated_source` | `included-metadata-and-summary` | 29 | 61741621 | 已选择的规范工程来源；图谱只登记元数据、哈希、定位和原创摘要。 |
| `registered_duplicate_alias` | `registered-alias-not-copied` | 2 | 402015 | 规范来源的字节级相同别名；只作为来源身份元数据登记。 |

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

- [[11_Engineering_Materials/Collections/ROS工程文件]]
- [[11_Engineering_Materials/_index|工程资料与匹配工作台]]
