# AGV 知识图谱可复现工具包

本目录保存三条可复现流程的生成器、测试与审计脚本：

1. 工程资料 → 资料证据图谱；
2. 最新三号车代码 → 独立 V2 机器快照，并与不可变 V1 比较；
3. V2 机器快照 → Obsidian 版本实例页、差异页与 Canvas 暂存投影。

所有原始生成器与测试均从本次已验证工作区按原字节复制。`MANIFEST.sha256` 用于检查这些字节以及本文档、校验脚本是否发生变化；`BUNDLE_TREE_SHA256.txt` 保存除自身之外的规范化目录树哈希。

## 目录

```text
graph_tools_bundle/
├── material_graph/
│   ├── generate_material_graph.py
│   └── test_generate_material_graph.py
├── v2_snapshot/
│   ├── generate_v2_snapshot.py
│   ├── audit_v2_snapshot.py
│   └── test_generate_v2_snapshot.py
├── obsidian_projection/
│   ├── generate_obsidian_projection.py
│   └── test_generate_obsidian_projection.py
├── verify_bundle.ps1
├── MANIFEST.sha256
└── BUNDLE_TREE_SHA256.txt
```

## 环境与统一参数

- Windows PowerShell 5.1 或 PowerShell 7；
- Python 3.10 或更高版本；
- Git 命令行可用（V2 生成器会读取源码工作树的 HEAD 和脏状态）；
- 仅使用 Python 标准库，不需要额外 `pip install`。

以下示例假定本工具包最终复制到：

```text
D:\AGV_Knowledge_Base\00_System\Graph_History\Tools
```

先在 PowerShell 设置参数。日期必须显式给出，保证相同输入产生相同输出：

```powershell
$Python = "python"
$Vault = "D:\AGV_Knowledge_Base"
$GraphHistory = Join-Path $Vault "00_System\Graph_History"
$Tools = Join-Path $GraphHistory "Tools"
$StageRoot = Join-Path $GraphHistory "_repro_staging"

$LatestCode = "D:\推料车项目\1.各车辆主代码\3.num3 improve\num3"
$V1Source = "D:\推料车项目\1.各车辆主代码\3.三号车代码\3号车代码\二代车代码"
$V1Snapshot = Join-Path $GraphHistory "Snapshots\code-v1"
$SnapshotDate = "2026-07-14"
```

`$StageRoot` 必须是专用、可丢弃的暂存目录，不应提交到 Git，也不能与源码、V1、Vault 根目录、`.git` 或本工具目录重合。

## 流程一：生成工程资料证据图谱

输入：

- `D:\推料车项目\9.车辆学习资料`；
- `D:\ROS工程文件` 全树；
- 脚本内的人工策展来源、主张与匹配规则。

这两个输入根目录被固定在 `generate_material_graph.py` 顶部的 `LEARNING_ROOT` 与 `ROS_INVENTORY_ROOT` 常量中，以便复现本版图谱。若来源迁移，应复制工具包形成新版本、审查路径和策展规则后再改常量，不要在旧版本上静默改写。

输出：`$MaterialStage\11_Engineering_Materials`，包括来源节点、结论节点、匹配节点、覆盖排除报告、Canvas 与 `_data` 机器清单。生成器只登记资料元数据、哈希、定位和短摘要，不复制原始 PDF、Word、压缩包、安装包或代码镜像。

请使用一个空的专用暂存目录：

```powershell
$MaterialStage = Join-Path $StageRoot "material-graph"
& $Python (Join-Path $Tools "material_graph\generate_material_graph.py") $MaterialStage
& $Python (Join-Path $Tools "material_graph\generate_material_graph.py") $MaterialStage --validate-only
```

运行单元测试：

```powershell
Push-Location (Join-Path $Tools "material_graph")
& $Python -m unittest discover -s . -p "test_*.py" -v
Pop-Location
```

注意：资料生成器不会主动清除旧页面。为避免已删除节点残留，必须生成到新的空暂存目录，校验通过后再按受控差异合并到 Vault。

## 流程二：生成并审计 V2 代码快照

输入：

- `$LatestCode`：最新三号车代码工作树；
- `$V1Snapshot`：不可变 V1 机器快照；
- `$V1Source`：当前机器上的 V1 历史源码，仅用于补充风险上下文。V1 没有逐文件清单，因此这些文件哈希不能证明与最初提取输入逐字节相同；
- `$SnapshotDate`：显式快照日期。

输出：`$V2Machine` 中固定的 8 个机器制品：源码清单、实体、语义关系、迁移关系、提取警告、V1→V2 差异 JSON、差异摘要和 manifest。

```powershell
$V2Machine = Join-Path $StageRoot "v2-machine"

& $Python (Join-Path $Tools "v2_snapshot\generate_v2_snapshot.py") `
  --source $LatestCode `
  --v1 $V1Snapshot `
  --v1-source $V1Source `
  --output $V2Machine `
  --created $SnapshotDate

& $Python (Join-Path $Tools "v2_snapshot\audit_v2_snapshot.py") `
  --output $V2Machine `
  --source $LatestCode `
  --v1 $V1Snapshot `
  --v1-source $V1Source
```

运行单元测试：

```powershell
Push-Location (Join-Path $Tools "v2_snapshot")
& $Python -m unittest discover -s . -p "test_*.py" -v
Pop-Location
```

生成器在写入前检查源码、V1、V1 历史源码和输出目录互不包含；拒绝符号链接、目录联接与硬链接式输出别名；并比较 V1 写入前后的目录树哈希。输出目录仍应为空或只包含该生成器认可的固定制品。

`unchanged` 只表示图谱语义字段未变，不等于源码实现未变。V1 没有逐文件清单，V1 独有关系只应视为 `extraction_limited` 待复核项，不能直接断言运行时关系已删除。

## 流程三：生成 Obsidian 暂存投影

输入：

- `$V2Machine`：流程二且审计通过的机器制品；
- `$V1Snapshot`：不可变 V1；
- `$Vault`：只读取必要的既有索引、ADR 与工作台页面作为投影上下文。

输出：`$ProjectionStage\AGV_Knowledge_Base`。该目录是一份待检查、待合并的增量投影，包含独立 V2 版本实例页、Added/Modified/Removed 差异页、风险页、迁移页、Canvas，以及机器制品的逐字节副本。它不会自动合并回正式 Vault。

```powershell
$ProjectionStage = Join-Path $GraphHistory "_projection_staging"

& $Python (Join-Path $Tools "obsidian_projection\generate_obsidian_projection.py") `
  --machine-dir $V2Machine `
  --v1-dir $V1Snapshot `
  --vault-dir $Vault `
  --output-dir $ProjectionStage
```

运行单元测试：

```powershell
Push-Location (Join-Path $Tools "obsidian_projection")
& $Python -m unittest discover -s . -p "test_*.py" -v
Pop-Location
```

投影生成器会整体删除并重建 `--output-dir`，因此该参数只能指向专用暂存目录，绝不能指向 `$Vault`、`$GraphHistory`、V1、源码树、`.git` 或 `$Tools`。脚本还要求输出位于其受控工作区内；按上述安装位置，应放在 `$GraphHistory` 的专用子目录中。

校验通过后仍应先检查 Git diff，再把暂存树中的目标文件合并到 Vault。不要把 `.obsidian`、暂存目录或测试临时目录纳入提交。

## V1 不可变与发布规则

- `Snapshots/code-v1` 是只读基线。任何流程都不得覆盖、清理、重命名或重新生成 V1；
- V2 必须使用新的 snapshot ID 和独立目录，V1 页面继续保留；
- 脏工作树生成的 V2 只能保持 `candidate`，不得自动更新 `current` 指针；
- 在推广候选快照前，必须人工复核高风险项、提取警告和所有 `needs-review` / `extraction_limited` 差异；
- 静态抽取与单元测试不等于 ROS 编译、节点联调、仿真或真车验证；
- 合并前再次确认 V1 树哈希未变、机器制品哈希一致、Obsidian wiki 链接与 Canvas 文件节点均可解析。

## 安全边界

- 原始工程资料、源码、绝对路径和项目命名都可能是敏感信息；远程仓库必须保持私有；
- 不执行资料树中的安装包、激活程序、压缩包、脚本镜像或未知二进制；
- 不把账号、令牌、网络密钥、原始日志、轨迹、整本资料或附件复制到知识库；
- 输出目录必须与所有输入目录分离。不要用目录联接、符号链接或硬链接绕过保护；
- 所有写入先落到暂存目录，验证和人工审查后再通过 Git 进行受控合并；
- 推送前检查 `git status` 与仓库可见性，确保 `.obsidian` 用户状态和无关改动未被暂存。

## 校验工具包自身

在工具包根目录运行：

```powershell
powershell -ExecutionPolicy Bypass -File .\verify_bundle.ps1
```

成功时输出每个清单文件的 `OK`，随后输出规范化树哈希并返回退出码 `0`。任何文件缺失、哈希不符、清单格式错误或目录树被增删都会返回非零退出码。
