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
3. PR #1 的真实 Actions 运行已确认检查名为 knowledge-check，push 与 pull_request 两次运行均为 success。负责人复核该工作流和保护范围后，可考虑将 knowledge-check 列为 required；本轮未应用该设置。
4. 建议保留普通 merge commit；不要同时设置要求线性历史。启用前复查已有规则及功能，避免覆盖更严格的配置。

本轮没有改写仓库 Ruleset、Branch Protection、成员权限或合并设置。负责人应用规则后，应在网页确认作用范围与执行状态，并用一条受控 PR 验证不能直接绕过。

已观察的运行证据：[PR 检查](https://github.com/mming52520-coder/AGV_Knowledge_Base/actions/runs/35963134499)、[分支推送检查](https://github.com/mming52520-coder/AGV_Knowledge_Base/actions/runs/35963080363)。
