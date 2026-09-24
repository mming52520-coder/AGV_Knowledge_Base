# 机器检索入口

本目录提供同一知识库的机器视图。Markdown 正文仍是人类维护的权威说明；config.json 只补充少量别名、类型化关系和证据入口，index.json 由工具确定性生成。现有图谱快照、资料清单和 current 指针保持原状。

## 调用

在仓库根目录运行 Python 3.10 或以上版本：

~~~bash
python3 00_System/AI_Index/kb_index.py build
python3 00_System/AI_Index/kb_index.py check
python3 00_System/AI_Index/kb_index.py query "左侧双超声循墙"
python3 00_System/AI_Index/kb_index.py query "left_wall_node" --snapshot code-v2-aef23b8c-wt-03fcd3118087
python3 00_System/AI_Index/kb_index.py query "超声" --project AGV --vehicle 三号车 --limit 10
~~~

query 返回有限个候选，不替用户选定同名实体。默认结果不把 V2 候选或历史差异页当成当前事实；显式提供快照或 --include-candidate 才展开。没有结果时输出空列表。查询前会重算输入哈希并运行 check；正文、证据、关系配置或保护路径变化后，旧索引会报过期，必须重新 build 并复核。

每条结果包含文档 id、正文路径、类型、项目/车型/范围、快照、审查状态、正文 SHA-256、别名、摘要、证据定位及证据 SHA-256。没有资料支持的字段为 null 或空列表，不会补造版本、测试结果或实车状态。文档身份与逻辑实体 UID、快照实例键分开；同一逻辑 UID 在不同快照出现是合法的。文件重命名后只要保留 frontmatter id，重建索引即可更新路径；身份不明的迁移仍需人工复核。

check 核对 419 个基线受保护文件组成的树指纹及两个既有标签，包括历史 Snapshots、Changes、冻结 Tools 及 current.json；验证文档身份、实例键、登记关系和关键阅读页的 Wiki 链接。链接检查支持显示别名、相对/根路径、Markdown 与 Canvas 目标、单段标题和 #^块锚点，并跳过围栏代码块；不解析多级标题链、Markdown 格式链接或内联代码中的示例。全库既有链接不在本轮强制范围，含动态查询及复杂嵌入的 Obsidian 视觉表现仍需人工核对。保护指纹取自基线提交 a072378b54583aa12bcd383eb36489863e88c861。

## 人工阅读与 Obsidian

从 [[知识库首页|首页]]进入专题，随后看 [[研发图谱工作台|图谱工作台]]核查代码快照和资料来源。在 Obsidian 中，可于 Settings → Editor → Properties in document 选择 Hidden；这只隐藏笔记顶部属性的显示，不会从 Markdown 删除字段，也不是保密措施。中文显示名可用 Wiki 链接的别名格式；局部图可用于看某篇笔记周围的原生链接，全局 Graph 的 Filters 可限制文件范围。原生链接图不是类型化工程关系图；机器索引文件也不保证在所有客户端文件列表中自动隐藏。本轮未运行 Obsidian 图形界面，视觉效果待人工验收。

设置名称参考 [Obsidian Properties](https://obsidian.md/help/properties)、[Internal links](https://obsidian.md/help/links) 和 [Graph view](https://obsidian.md/help/plugins/graph) 官方说明。
