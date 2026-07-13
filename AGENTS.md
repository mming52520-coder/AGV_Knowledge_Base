# AGV Knowledge Base Rules

## Purpose

This repository is the engineering knowledge base for mobile robot R&D. Windows Obsidian is the primary authoring environment; Ubuntu Codex and ROS workspaces consume and update Markdown through Git.

## Before editing

1. Run `git status`.
2. If the worktree is clean, run `git pull --ff-only`.
3. If the worktree is dirty or branches have diverged, stop and report the state. Do not stash, reset, rebase, merge, or discard changes automatically.
4. Read the relevant existing notes before creating a new one.

## Content model

- Organize project work by stable role responsibility, not only by temporary functional modules.
- Keep management-platform front-end and back-end work separate from the Algorithm role.
- Preserve traceability between project/task/daily report/file/version, responsible person, status, experiment or issue number, attachment path, review or acceptance conclusion, and remarks.
- Use the lifecycle: task intake -> scheme/preparation -> development or debugging experiment -> test verification -> issue closure -> version release -> archive.
- Prefer explicit Obsidian internal links to duplicate explanations.

## File rules

- Use UTF-8 Markdown and LF line endings.
- Do not create names that differ only by letter case.
- Avoid Windows reserved names, trailing spaces or dots, and these characters: `< > : " / \\ | ? *`.
- Windows owns `.obsidian` configuration. Ubuntu agents should not edit `.obsidian` unless explicitly requested.
- Do not commit `.obsidian/plugins`, plugin `data.json`, workspace state, secrets, ROS bags, logs, or build outputs.
- Put large attachments under review before adding them to Git; use Git LFS only after explicit approval.

## Knowledge graph evolution

- Treat `00_System/Graph_History/Snapshots/*` as immutable version evidence. Generate a new snapshot and a separate `Changes/<baseline>__<target>` comparison; never overwrite an older snapshot.
- Keep `03_ROS` as the stable logical-entity layer. Version-instance pages under a snapshot are generated views and must not silently replace those logical pages.
- Preserve stable `entity_uid` values only when strong keys match. Record decomposition, replacement, removal and ownership changes explicitly; do not infer a rename from name similarity alone.
- Engineering-material matches must keep `match_probability` separate from `implementation_evidence`. Proposals, textbooks and different vehicle models are reference evidence, not proof that current code implements a feature.
- A snapshot from a dirty or untracked code worktree remains a review candidate even when its extraction is validated. Promote the current pointer only after the source state is reproducible and the diff has been reviewed.
- Run the graph generators and their validators before staging. Report unresolved links, extraction limitations, risk records and source-state drift.

## Git rules

- One logical change per commit.
- Use descriptive messages such as `docs: add dual-magnetic navigation test record`.
- Review `git diff --staged` and scan for secrets before committing.
- Never use force push, `git reset --hard`, or `git clean -fd`.
- Do not edit the same note concurrently on Windows and Ubuntu.
- After completing a coherent change, commit and push promptly.

## Completion

Report changed notes, verification performed, unresolved links, conflicts, large files, and any action still required from the user.
