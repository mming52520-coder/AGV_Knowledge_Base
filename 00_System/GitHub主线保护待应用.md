---
id: "agv:system:github-main-protection-plan"
type: standard
status: proposed
review: needs-review
project: AGV
updated: 2026-09-24
tags: [GitHub, 分支治理]
---

# GitHub main 保护待应用方案

本文件只记录待负责人审查的线上操作，不代表 GitHub 规则已经启用。2026-09-24 读取仓库规则集列表为空；读取 main 旧式 Branch Protection 返回 404（未配置）。当前仓库为 Public，负责人已明确要求保持公开。

## 建议在 GitHub Settings → Rules → Rulesets 中核对

1. 仅针对 main 建立分支规则：通过 PR 合并，禁止强制推送和删除，要求对话已解决。
2. 单人维护阶段不要设置无法由其他人完成的强制自我批准。待有合适审查人后再设置审批人数。
3. 本轮 CI 的检查名须在真实 PR 运行后确认，再将该稳定检查列为 required。不要在检查尚未产生时猜测名称并启用。
4. 建议保留普通 merge commit；不要同时设置要求线性历史。启用前复查已有规则及功能，避免覆盖更严格的配置。

本轮没有改写仓库 Ruleset、Branch Protection、成员权限或合并设置。负责人应用规则后，应在网页确认作用范围与执行状态，并用一条受控 PR 验证不能直接绕过。
