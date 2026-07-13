---
id: "agv:ros:communication-graph"
type: system
status: active
review: generated
project: AGV
updated: 2026-07-14
tags: [AGV, ROS, Mermaid, 通信图]
---

# ROS 节点与通信图

```mermaid
flowchart LR
    MQTT["agv_mqtt_bridge"]
    REMOTE["remote_controller"]
    TRACK["trajectory_tracker"]
    REC["trajectory_recorder"]

    MAGDRV["mag_sensor_reader"] --> MAGRAW["/mag_sensor/raw_data"]
    MAGRAW --> MAGFOLLOW["magnetic_follower"]
    MAGDRV --> MAGFRAME["/mag_sensor/frame + nail_event"]
    MAGFRAME --> REC

    USDRV["dyp_a21_can_node"] --> USDATA["/ultrasonic/*"]
    USDATA --> USFOLLOW["ultrasonic_follower"]
    USDATA --> TRACK
    USDATA --> REMOTE

    MAGFOLLOW --> OLD["/motor_speed + /motor_command"]
    USFOLLOW --> OLD
    TRACK --> OLD
    REMOTE --> OLD
    REMOTE --> BRAKE["/motor_brake"]

    TRACK --> NEW["/chassis/cmd"]
    REMOTE --> NEW
    NEW --> BRIDGE["chassis_bridge"]
    BRIDGE --> STATE["/chassis/state"]
    STATE --> FB["drive_feedback_odom"]
    FB --> TRACK
    FB --> REC

    OLD --> ADAPTER["cmd_vel_adapter"]
    BRAKE --> ADAPTER
    ADAPTER --> CMDVEL["/cmd_vel"]
    CMDVEL --> STM32["wheeltec_robot"]

    OLD --> DIO["hk_dio_remote"]
    BRAKE --> DIO
    OLD --> MQTT
    BRAKE --> MQTT

    TRACK --> STATUS["task_state + trajectory_status"]
    STATUS --> MQTT
    REC --> MQTT
```

## 主控制链

- 新链：[[Nodes/trajectory_tracker]] 或 [[Nodes/remote_controller]] → [[Interfaces/chassis-cmd]] → [[Nodes/chassis_bridge]] → [[Interfaces/chassis-state]]
- 兼容链：多个控制源 → [[Interfaces/motor-speed]] / [[Interfaces/motor-command]] / [[Interfaces/motor-brake]] → [[Nodes/cmd_vel_adapter]] → [[Interfaces/cmd-vel]] → [[Nodes/wheeltec_robot_node]]

## 主感知链

- 磁导航：[[Nodes/mag_sensor_reader]] → [[Interfaces/mag-sensor-raw-data]] / [[Interfaces/mag-sensor-frame]] / [[Interfaces/mag-sensor-nail-event]] → [[Nodes/magnetic_follower]] 与轨迹系统
- 超声安全：[[Nodes/dyp_a21_can_node]] → [[Interfaces/ultrasonic-distance]] / [[Interfaces/ultrasonic-status]] → 跟踪、遥控和安全逻辑
- 底盘反馈：[[Nodes/chassis_bridge]] → [[Interfaces/chassis-state]] → [[Nodes/drive_feedback_odom]] → [[Interfaces/drive-feedback]]

## 注意

此图基于静态源码和 Launch。运行时实际节点、重映射和发布者必须通过 ROS 运行快照复核，尤其是 [[../05_Control/控制权仲裁]] 与 [[Interfaces/odom|/odom 多发布者问题]]。

## 关联

- [[ROS系统总览]]
- [[ROS接口目录]]
- [[Launch目录]]
