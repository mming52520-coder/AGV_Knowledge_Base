---
id: "agv:system:knowledge-graph-coverage"
type: report
status: active
review: generated
project: AGV
updated: 2026-07-14
tags: [AGV, 知识图谱, 覆盖率, 验证]
---

# Knowledge Graph Coverage

## 当前范围

- 主源：三号车二代代码当前工作区。
- 差异源：一号车、二号车当前主代码。
- 人工架构源：`code_logic_layers.md`。
- 历史代码、构建产物、bag、压缩包、凭据配置和大文件已排除。

## 实体覆盖

| 实体 | 数量 | 说明 |
|---|---:|---|
| ROS Package | 14 | 12 个当前/兼容包、1 个停用包壳、1 个归档包 |
| ROS Node | 23 | 当前、兼容和诊断节点 |
| ROS Interface | 25 | 跨包共享、安全关键 Topic 与 Service 组 |
| Hardware | 8 | 代码可验证的主要设备/总线 |
| Architecture Layer | 6 | 人工整理的六层架构 |
| Navigation Algorithm | 4 | 总览、磁导航、超声安全、轨迹系统 |

## 自动验证

- Markdown 文件：`118`
- Wiki 双链引用：`857`
- 未解析 Wiki 链接：`0`
- 重复稳定 ID：`0`
- Canvas JSON：有效
- Git `diff --check`：通过
- 插件二进制与源码数据：未加入提交
- 敏感内容扫描：仅保留“不记录凭据”的规则说明，无凭据值

## 待人工/运行时复核

1. [[../03_ROS/Interfaces/odom|/odom]] 多个潜在发布者的权威来源。
2. [[../05_Control/控制权仲裁]] 的实际模式切换、安全优先级和超时行为。
3. [[../03_ROS/Packages/analog_controlled_motor]] 在三号车中的停用状态。
4. [[../03_ROS/Nodes/hk_dio_controller]] 的 Launch package 名称不一致。
5. MQTT 和多方向超声等动态参数化 Topic 的最终运行名称。
6. 二号车、三号车源工作区存在未提交修改，当前知识对应文件快照而非纯 Git 提交。
7. 静态扫描尚未与真车 `rosnode list`、`rostopic info`、Service 列表做差异核对。

## 下一轮建议

- 在三号车运行时采集只读 ROS 图快照，补齐静态图与运行图差异。
- 从工作记忆提炼测试、Bug 和版本演化节点。
- 对精选硬件手册生成参数与寄存器摘要，不复制大型 PDF。

## 关联

- [[知识图谱Schema]]
- [[代码来源与扫描范围]]
- [[../01_Project_AGV/AGV系统总览]]
- [[../03_ROS/ROS节点与通信图]]
