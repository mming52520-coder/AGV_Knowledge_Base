---
type: standard
status: active
owner: Windows Obsidian
updated: 2026-07-14
tags:
  - Git
  - 同步
  - Codex
---

# Git 同步规范

## 总体原则

- 仓库负责人已明确要求当前 GitHub 仓库保持 Public。可见性是负责人显式决定的仓库级策略；发布前复核当前 visibility、来源权限、敏感字段和历史影响。Public 仓库不能依靠分支实现保密隔离；AI 未获新授权不得自行更改 visibility 或改写安全规范来适配现状。本规范不授予任何资料再许可。
- 冻结的 Graph_History/Tools/README.md 中关于 Private 的句子是历史工具包发布时的条件，为保持清单与树哈希不改写；当前仓库可见性以负责人本次决定为准。
- Windows 是 Obsidian 笔记和 `.obsidian` 配置的主要写入端。
- Ubuntu Codex 主要读取方案并回写代码分析、接口说明和测试结果。
- 两端不要同时编辑同一篇笔记。
- 有未提交修改时，不自动拉取、变基、合并或丢弃内容。
- main 为经过审查的知识主线，不代表其中描述的机器人能力已获实车验证。

## 任务分支与审查

- 每项任务从已核对的 main 建立短期 docs/*、feature/*、fix/* 或 chore/* 分支；完成后通过 PR 审查再合并。不要建立长期 develop、human/ai 或按电脑、人员、车型划分的常驻分支。
- AI 只在获授权的任务分支提交、推送；main 的合并由负责人审核。一个任务可以用多个清晰提交，但不得混入机器人源码或其他任务。
- Windows 和 Ubuntu 顺序交接同一任务分支。多个会话使用独立目录或 worktree，并划定修改文件。
- 开始同步先检查状态与远端分叉；工作区干净且适用时才执行 git pull --ff-only。若发生分叉或冲突，停止自动处理，保留两侧内容。
- 既有标签和历史快照保持不变；候选快照不能因 PR 合并自动升级为验收通过。
- PR 使用 .github/pull_request_template.md 核对范围、证据、验证、历史保护和回退。主线规则的待应用方案见 [[GitHub主线保护待应用]]。

## Windows 开始工作

```powershell
cd D:\AGV_Knowledge_Base
git status
git pull --ff-only
```

只有在 `git status` 干净时才执行拉取。如果 `pull --ff-only` 失败，应停止并检查分支是否分叉。

## Windows 完成工作

```powershell
git status
git diff
git add <本次任务明确修改的文件>
git diff --staged
git commit -m "docs: describe the completed knowledge change"
git push
```

提交前确认：

- staged 内容只包含本次逻辑变更；
- 没有密码、Token、私钥、客户账号或未脱敏数据；
- 没有误加入视频、ROS bag、日志、构建目录或异常大文件；
- 没有仅由大小写变化产生的重复文件。

## Ubuntu/Codex 开始工作

```bash
cd ~/AGV_Knowledge_Base
git status
git pull --ff-only
```

Ubuntu 不主动修改 `.obsidian`。完成 Markdown 更新后，执行同样的 `status -> diff -> add -> staged diff -> commit -> push` 流程。

## 冲突处理

1. 停止自动操作，不使用强制推送。
2. 保存 `git status`、冲突文件列表及双方差异。
3. 逐篇合并，保留双方有效内容和 Obsidian 双链。
4. 重新检查 Markdown 与链接后再提交。
5. 禁止使用 `git reset --hard` 或 `git clean -fd` 解决冲突。

## 大文件

添加 PDF、Office 文件或图片前先查看大小。大文件确有版本管理价值时，再单独评估 Git LFS；ROS bag、视频和构建产物默认不进入知识库仓库。
