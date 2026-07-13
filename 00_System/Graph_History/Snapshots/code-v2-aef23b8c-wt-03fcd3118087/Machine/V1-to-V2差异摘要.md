# V1 → V2 代码图谱差异摘要

- 基线：`code-v1-e8a1b3d`
- 目标：`code-v2-aef23b8c-wt-03fcd3118087`
- 源码 Git HEAD：`aef23b8cc796ab791bae0c8f7516c195c359c846`
- 工作区脏状态：`True`

## 实体守恒

| 项目 | 数量 |
| --- | ---: |
| V1 代码实体 | 62 |
| V2 代码实体 | 192 |
| 稳定 ID 匹配 | 49 |
| 未变化 | 16 |
| 语义变化 | 33 |
| 新增 | 143 |
| V1 独有 | 13 |

数量校验：`V1 = matched + removed`，`V2 = matched + added`，已由生成器验证。

> `unchanged` 仅表示图谱身份与声明的 ROS 语义字段未变，**不等于源代码或配置未变**。V1 没有逐文件清单，内部实现变化只能由单独静态风险证据补充。本报告是图谱级代码实体差异，不是完整源代码 diff。

## 关系差异

- V1 关系：171
- V2 关系：496
- 新增关系：379
- V1 独有关系：54
- 其中解析受限候选：54（不作为确定性破坏删除）
- 显式迁移关系：50

## 扫描范围变化

- 新增包范围：agv_bringup、agv_decision、agv_execution、agv_interfaces、agv_legacy、agv_mission、agv_perception、agv_safety、agv_state_estimation、agv_telemetry、dyp_ultrasonic_driver
- V1 没有逐文件清单，因此不能从文件级差异直接断言删除；此限制已单列为 `scope_change`。
- 分解与替代不覆盖 V1 实体，详见 `migration-relations.jsonl`。

## 静态风险审计（R01–R16）

> 以下 16 条来自静态代码、配置、launch、V1 图谱与 Git 工作区证据；本次未独立运行 ROS 单元测试、集成测试或实车测试。

| ID | 级别 | 类型 | 风险 |
| --- | --- | --- | --- |
| R01 | critical | release_risk | V2 含 31 个 modified 与 126 个 untracked 文件，Git HEAD 不能单独还原当前快照。 |
| R02 | high | breaking | trajectory_tracker 的 control_output_mode 默认值由 V1 的 chassis_cmd 改为 V2 的 legacy；V2 默认会禁用 /chassis/cmd 发布。 |
| R03 | high | breaking | remote_controller 在 V1 默认发布 /chassis/cmd 并支持 remote_joy 云端输入；V2 改为直接发布 /motor_speed 与 /motor_brake，且云端输入路径已删除。 |
| R04 | high | breaking | V1 chassis_bridge 的 OID 重连、通信丢失后运动抑制与 HuakongAoBackend 实现，在 V2 当前文件中均不再存在；Huakong 后端被明确标记为已移除。 |
| R05 | high | breaking | /odom 唯一所有者改为 vehicle_state_estimator_node；与旧发布者并跑会发生多发布者冲突。 |
| R06 | high | breaking | GPS NMEA 节点、launch、/gps/fix_json 与 MQTT GPS 遥测链在 V2 中删除且无替代。 |
| R07 | high | breaking | drive_feedback_odom 链删除，录制与跟踪里程转为 FT-EPC 累计脉冲；encoder_ppr 未配置时无有效里程。 |
| R08 | high | integration_gap | vehicle.launch 不启动传感器驱动或真实底盘驱动，单独启动不能形成完整实车链。 |
| R09 | high | integration_gap | teleop_node 需要 /teleop/cmd 与 /teleop/stop，但生产 launch 没有输入转换生产者。 |
| R10 | high | validation_blocker | MagFrame.line_position 尚未换算为真实 magnetic_error_m，必须进行实车标定。 |
| R11 | medium | deployment_change | V1→V2 的 IMU 与磁传感器默认端口均发生变化，部署映射需复核。 |
| R12 | medium | deployment_change | 旧栈与新栈必须互斥，否则会争抢 /odom、电机话题和串口。 |
| R13 | medium | scope_contraction | encoder_probe 与 yz_aim_probe 删除，硬件探针能力收缩。 |
| R14 | medium | parity_gap | 磁转向保持/释放、精确磁钉触发、滑移检测及部分高级 EKF 未迁移。 |
| R15 | medium | breaking | agv_mqtt_bridge 默认 vehicle_id 从 V1 的 agv_002 改为 V2 的 agv_001。 |
| R16 | medium | safe_default_change | vehicle.launch 默认 backend=mock 且 hardware_enabled=false，显式启用前车辆不会运动。 |

## 提取与发布限制

- launch 解析不展开 `include`、`arg/替换表达式`、`if/unless` 或 `remap`。
- 端点解析仍是静态语法扫描；宏、运行时拼接名称和动态循环可能缺失。
- V1 独有关系统一标为 `extraction_limited`，不是已确认的运行时删除。
- 快照包含源目录定位与相对证据路径；仅用于私有仓库，公开前必须脱敏。
