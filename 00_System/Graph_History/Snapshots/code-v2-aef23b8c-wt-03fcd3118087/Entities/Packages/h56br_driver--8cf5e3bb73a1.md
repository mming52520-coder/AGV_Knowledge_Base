---
id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:h56br_driver"
type: "graph_entity_instance"
logical_entity_uid: "agv:ros:package:h56br_driver"
snapshot_instance_id: "code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:h56br_driver"
snapshot_id: "code-v2-aef23b8c-wt-03fcd3118087"
entity_type: "ros_package"
title: "h56br_driver"
status: "available"
review: "generated"
source_snapshot: "03fcd31180875699d27d72a28fc52de5d812eb8b6ea1663663039ade901a2122"
semantic_fingerprint: "fe4a561dc014f7860b57c9b41f1001c468017dadb46fe73a4299014069000600"
relation_fingerprint: "6de625653bca360506dbdc5850406146b35e38b5334499574b27ba409a6b5ee7"
updated: "2026-07-14"
tags: ["AGV", "代码图谱", "V2", "实体实例"]
---

# h56br_driver

- 逻辑实体：`agv:ros:package:h56br_driver`
- 快照实例：`code-v2-aef23b8c-wt-03fcd3118087::agv:ros:package:h56br_driver`
- 所属快照：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/V2快照说明|code-v2-aef23b8c-wt-03fcd3118087]]
- 分组索引：[[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/_index|Packages]]
- 代码证据主路径：`src/h56br_driver/package.xml`

## 语义属性

| 字段 | 值 |
|---|---|
| `executable` |  |
| `interface_kind` |  |
| `message_type` |  |
| `ros_name` |  |
| `status` | available |
| `type` | ros_package |
| `vehicles` | ["一号车","二号车","三号车"] |
| `version` | 0.1.0 |

## 证据

| 路径 | 行 | 操作 | 文件 SHA-256 |
|---|---:|---|---|
| `src/h56br_driver/package.xml` | 1 | `package_manifest` | `2d81f4217f99d05d90e9e7babbb957d31318321118b8ceb2bbe0398a867a96a0` |

## 出向关系

- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/h56br_driver-H56BRStatus--e74878990af5|agv:ros:message:h56br-driver-h56brstatus]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/h56br_driver-CapacityFull--6719a9803ef3|agv:ros:service-type:h56br-driver-capacityfull]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/h56br_driver-CapacityZero--19ca371a9728|agv:ros:service-type:h56br-driver-capacityzero]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/h56br_driver-CurrentZero--c3c8c9681dc8|agv:ros:service-type:h56br-driver-currentzero]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/h56br_driver-ReadParams--c3050280acb2|agv:ros:service-type:h56br-driver-readparams]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/h56br_driver-RestoreDefault--9ad5d4dbe803|agv:ros:service-type:h56br-driver-restoredefault]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/h56br_driver-SetChargeMode--cb4fab6482be|agv:ros:service-type:h56br-driver-setchargemode]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/h56br_driver-SetFullVoltage--b426d29b062d|agv:ros:service-type:h56br-driver-setfullvoltage]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/h56br_driver-SetNominalCapacity--02d34e0362ee|agv:ros:service-type:h56br-driver-setnominalcapacity]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/h56br_driver-SetZeroVoltage--35ae27d9b421|agv:ros:service-type:h56br-driver-setzerovoltage]]
- `defines` → [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/h56br_driver-WriteHoldingRegister--c9f9853a8062|agv:ros:service-type:h56br-driver-writeholdingregister]]

## 入向关系

- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Packages/agv_mqtt_bridge--001d465b2aae|agv:ros:package:agv_mqtt_bridge]] → `depends_on`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Nodes/h56br_node--74030e2108af|agv:ros:node:h56br_node]] → `package`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-current--994c4cef7d41|agv:ros:interface:battery-h56br-current]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-soc--fb01514bedd7|agv:ros:interface:battery-h56br-soc]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-status--355f7fc2c130|agv:ros:interface:battery-h56br-status]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-voltage--dbc3b1489da1|agv:ros:interface:battery-h56br-voltage]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-capacity_full--403ca82410b7|agv:ros:service:battery-h56br-capacity-full]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-capacity_zero--88b00cd54235|agv:ros:service:battery-h56br-capacity-zero]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-current_zero--8e179c2756bf|agv:ros:service:battery-h56br-current-zero]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-read_params--e3331a08eea7|agv:ros:service:battery-h56br-read-params]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-restore_default--52a91e8888f6|agv:ros:service:battery-h56br-restore-default]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-set_charge_mode--e2649739bec2|agv:ros:service:battery-h56br-set-charge-mode]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-set_full_voltage--3e55a5dd6e5f|agv:ros:service:battery-h56br-set-full-voltage]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-set_nominal_capacity--046746b15944|agv:ros:service:battery-h56br-set-nominal-capacity]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-set_zero_voltage--e57a4135f50b|agv:ros:service:battery-h56br-set-zero-voltage]] → `related_packages`
- [[00_System/Graph_History/Snapshots/code-v2-aef23b8c-wt-03fcd3118087/Entities/Interfaces/battery-h56br-write_holding_register--8b195e5386f4|agv:ros:service:battery-h56br-write-holding-register]] → `related_packages`

## 相对 V1 的变化

- 变化类型：`modified`
- 变化字段：`status`
- 差异记录：[[00_System/Graph_History/Changes/code-v1-e8a1b3d__code-v2-aef23b8c-wt-03fcd3118087/Entities/Modified/h56br_driver--8cf5e3bb73a1|agv:ros:package:h56br_driver]]
