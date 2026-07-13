---
type: procedure
status: draft
updated: 2026-07-14
tags:
  - Ubuntu
  - Codex
  - Git
---

# Ubuntu 接入步骤

> 前提：Windows 端已完成首次提交，并推送到空的私人远程仓库。

## 克隆

```bash
cd ~
git clone https://github.com/mming52520-coder/AGV_Knowledge_Base.git AGV_Knowledge_Base
cd ~/AGV_Knowledge_Base
git status
```

如果使用 SSH，应先独立验证 `ssh -T`，不要把私钥复制进知识库。

## Codex 使用方式

在 ROS 工作区启动 Codex 时，通过相邻路径引用知识库：

```text
请先阅读：
~/AGV_Knowledge_Base/AGENTS.md
~/AGV_Knowledge_Base/04_Navigation/相关方案.md

再分析当前 ROS 工程。修改代码前说明方案与影响；测试完成后，将结果写回知识库对应测试记录。
```

## Ubuntu 端边界

- 不需要安装 Obsidian 社区插件即可让 Codex 读取 Markdown。
- 默认不修改 `.obsidian`。
- 不在 ROS 仓库和知识库仓库之间复制 `.git` 目录。
- 代码提交留在 ROS 工程仓库；方案、接口、问题和测试结论留在知识库仓库。
