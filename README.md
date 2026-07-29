# AGV Knowledge Base

智能机器人研发知识库，采用 **Windows Obsidian 主编辑 + Git 私有仓库同步 + Ubuntu Codex/ROS 工程协作** 的工作方式。

## 环境分工

- Windows：Obsidian 笔记、方案设计、会议记录、测试归档与 `.obsidian` 配置维护。
- Ubuntu：Codex 读取方案、分析 ROS 工程、补充接口与测试结果。
- Git：版本历史和双端同步；不替代备份，也不允许两端同时编辑同一篇笔记。

## 快速入口

- [[知识库首页]]
- [[00_System/Git同步规范]]
- [[00_System/Plugin-Lock]]
- [[00_System/Ubuntu接入步骤]]

## 安全原则

- 仓库必须保持为 Private。
- 不提交密码、令牌、私钥、车辆现场账号或未脱敏的客户数据。
- 大型数据包、视频、ROS bag、构建产物和日志不直接进入本仓库。
- 遇到 Git 冲突时停止自动操作，保留双方内容后人工审查。
