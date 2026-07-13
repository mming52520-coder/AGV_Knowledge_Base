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

- 远程仓库必须为 Private，并使用一个不带 README、License 或 `.gitignore` 的空仓库接收首次推送。
- Windows 是 Obsidian 笔记和 `.obsidian` 配置的主要写入端。
- Ubuntu Codex 主要读取方案并回写代码分析、接口说明和测试结果。
- 两端不要同时编辑同一篇笔记。
- 有未提交修改时，不自动拉取、变基、合并或丢弃内容。

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
git add .
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
