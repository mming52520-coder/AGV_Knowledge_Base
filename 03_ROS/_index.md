---
type: index
status: active
updated: 2026-07-14
tags: [AGV, ROS]
---

# ROS

## 入口

- [[ROS系统总览]]
- [[ROS节点与通信图]]
- [[ROS接口目录]]
- [[Launch目录]]

## Package

```dataview
TABLE status AS 状态, review AS 复核, vehicles AS 车辆
FROM "03_ROS/Packages"
WHERE type = "ros_package"
SORT file.name ASC
```

## Node

```dataview
TABLE status AS 状态, review AS 复核, package AS Package
FROM "03_ROS/Nodes"
WHERE type = "ros_node"
SORT file.name ASC
```

## 待复核接口

```dataview
TABLE ros_name AS 接口, status AS 状态, review AS 复核
FROM "03_ROS/Interfaces"
WHERE review = "needs-review"
SORT file.name ASC
```

- [[../知识库首页|返回知识库首页]]
