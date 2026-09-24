---
id: "agv:system:knowledge-graph-schema"
type: decision
status: active
review: verified
project: AGV
updated: 2026-07-14
tags: [AGV, 知识图谱, Obsidian, Codex]
---

# 知识图谱 Schema

## 目标

把人工整理的项目架构、当前车辆代码和研发证据连接成可追溯的工程图谱。图谱服务于检索、影响分析和 Codex 增量维护，不代替源代码。

## 核心实体

| `type` | 含义 | 示例 |
|---|---|---|
| `system` | 整车或跨域系统 | AGV 系统 |
| `layer` | 代码逻辑层 | 导航决策与安全层 |
| `vehicle_variant` | 车辆代码版本 | 三号车 |
| `ros_package` | ROS Package | trajectory_recorder |
| `ros_node` | ROS 运行节点 | trajectory_tracker |
| `ros_interface` | Topic、Service 或 Action | /chassis/cmd |
| `hardware` | 设备或总线 | MS16A 磁传感器 |
| `algorithm` | 算法或状态机 | 磁导航 |
| `test` | 测试证据 | 实车轨迹测试 |
| `issue` | 问题与闭环记录 | 对接偏移 |
| `decision` | 架构或流程决策 | 本 Schema |

## 稳定字段

```yaml
id: "命名空间:类型:稳定名称"
type: ros_node
status: active
review: generated
project: AGV
updated: 2026-07-14
source_scope: 三号车当前工作区
source_snapshot: SHA-256
source_paths: []
parent:
depends_on: []
related: []
tags: []
```

ROS 节点可增加：

```yaml
package:
publishes: []
subscribes: []
provides_services: []
calls_services: []
parameters: []
launches: []
```

## 关系语义

- `parent`：上级系统或逻辑层。
- `depends_on`：运行或构建依赖。
- `publishes` / `subscribes`：ROS 通信方向。
- `controls`：控制目标。
- `reads_from`：硬件或数据来源。
- `implements`：软件实体实现的算法或能力。
- `verified_by`：测试或运行证据。
- `related`：无法用上述稳定关系表达的弱关联。

## 自动生成边界

- 自动事实必须来自当前源码、Launch、配置或明确的人工架构文档。
- 动态拼接的 Topic、参数和条件启动项标记为 `needs-review`，不猜测最终运行值。
- 测试文件存在不等于测试已通过。
- 自动区块以后使用 `<!-- codex:auto:start -->` 与 `<!-- codex:auto:end -->` 包围；人工结论写在区块外。
- 不把密码、令牌、服务器地址、账号或私钥写入知识库。
- 不复制源码、ROS bag、构建目录、插件二进制和大型手册。

## 命名约定

- 文件名使用稳定中文概念或 ROS 实体名。
- Topic 文件名移除开头斜杠并用安全短横线表达层级，完整名称保留在 `ros_name`。
- 同名 Package 在三辆车中只建立一个逻辑节点，版本差异记录在节点内。
- 归档包和停用包保留节点，但明确标记状态，不能与当前实现混用。

## 关联

- [[代码来源与扫描范围]]
- [[../01_Project_AGV/AGV系统总览]]

## 人机检索兼容扩展

[[AI_Index/README|机器检索入口]]读取现有 frontmatter 的文档 id、正文路径、类型、状态与版本，再增加可再生的内容指纹、别名、证据和少量类型化关系，不另建第二套权威正文。

- 文档 id 标识一篇笔记或来源节点；不能把所有 id 都当成代码实体 UID。
- logical_entity_uid 标识跨快照的逻辑工程对象；snapshot_instance_id 由 snapshot_id 和 logical_entity_uid 组成，并以项目、范围、快照区分实例。
- 文档移动或标题改变时保留 id；内容 SHA-256 仅用于发现过期，不参与身份分配。没有强证据的重命名或别名冲突列为候选，不自动合并。
- 关系只在两端身份与证据都可定位时登记。来源主张的 planned/reference 与源码静态事实、测试运行和实车验收保持分离。
- 机器索引的合法性与单元测试通过不改变 current.json，也不提升历史候选或实车验证状态。
