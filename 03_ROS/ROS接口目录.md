---
id: "agv:ros:interface-catalog"
type: index
status: active
review: generated
project: AGV
updated: 2026-07-14
tags: [AGV, ROS, Topic, Service]
---

# ROS 接口目录

本目录优先为跨包共享、安全关键或需要单独解释的接口建立节点。包内局部 Topic 仍保留在源码和节点页中，避免图谱过度膨胀。

| 接口 | 类型 | 消息/服务 | 状态 |
|---|---|---|---|
| [[Interfaces/chassis-cmd|/chassis/cmd]] | topic | `chassis_controller/ChassisCommand` | active |
| [[Interfaces/chassis-state|/chassis/state]] | topic | `chassis_controller/ChassisState` | active |
| [[Interfaces/motor-speed|/motor_speed]] | topic | `std_msgs/Float32` | compatibility |
| [[Interfaces/motor-command|/motor_command]] | topic | `std_msgs/String` | compatibility |
| [[Interfaces/motor-brake|/motor_brake]] | topic | `std_msgs/UInt8` | compatibility |
| [[Interfaces/cmd-vel|/cmd_vel]] | topic | `geometry_msgs/Twist` | compatibility |
| [[Interfaces/odom|/odom]] | topic | `nav_msgs/Odometry` | active |
| [[Interfaces/imu|/imu]] | topic | `sensor_msgs/Imu` | active |
| [[Interfaces/mag-sensor-raw-data|/mag_sensor/raw_data]] | topic | `std_msgs/UInt16` | active |
| [[Interfaces/mag-sensor-frame|/mag_sensor/frame]] | topic | `magnetic_controlled_motor/MagFrame` | active |
| [[Interfaces/mag-sensor-nail-event|/mag_sensor/nail_event]] | topic | `magnetic_controlled_motor/MagNailEvent` | active |
| [[Interfaces/mag-line-position|/mag_line_position]] | topic | `std_msgs/Float32` | active |
| [[Interfaces/ultrasonic-distance|/ultrasonic/*_distance]] | topic_group | `std_msgs/Float32` | active |
| [[Interfaces/ultrasonic-status|/ultrasonic/*_status]] | topic_group | `ultrasonic_controlled_motor/UltrasonicStatus` | active |
| [[Interfaces/battery-h56br-status|/battery/h56br/status]] | topic | `h56br_driver/H56BRStatus` | active |
| [[Interfaces/battery-h56br-soc|/battery/h56br/soc]] | topic | `std_msgs/Float32` | active |
| [[Interfaces/drive-feedback|/drive_feedback_odom + /drive_feedback_speed + /drive_feedback_twist]] | topic_group | `nav_msgs/Odometry; std_msgs/Float32; geometry_msgs/TwistStamped` | active |
| [[Interfaces/trajectory-status|/trajectory_status]] | topic | `std_msgs/String` | active |
| [[Interfaces/agv-task-state|/agv/task_state]] | topic | `std_msgs/String` | active |
| [[Interfaces/gps-fix-json|/gps/fix_json]] | topic | `std_msgs/String (JSON)` | active |
| [[Interfaces/encoder-state|/encoder_angle + encoder_twist]] | topic_group | `std_msgs/Float32; geometry_msgs/TwistStamped/相关类型` | active |
| [[Interfaces/trajectory-services|/trajectory/* + /imu/* + /steering/*]] | service_group | `std_srvs/Trigger` | active |
| [[Interfaces/motor-services|/motor_init + /motor_enable]] | service_group | `std_srvs/Trigger; std_srvs/SetBool` | active |
| [[Interfaces/hardware-probe-topics|/imu/probe_* + /encoder_probe/* + ~yz_aim_probe/*]] | topic_group | `多种诊断消息` | diagnostic |
| [[Interfaces/relay-io-status|hk_dio/input_status + hk_dio/relay_status]] | topic_group | `std_msgs/相关类型` | compatibility |

## 关键复核项

- [[Interfaces/odom|/odom]] 存在多个静态发布者，必须在运行时确认唯一权威来源。
- [[Interfaces/motor-speed|/motor_speed]] 与 [[Interfaces/motor-command|/motor_command]] 存在多个潜在控制源。
- [[Interfaces/chassis-cmd|/chassis/cmd]] 是三号车新底盘主接口。
- 动态参数化 Topic 必须结合启动参数或运行时快照复核。

## 关联

- [[ROS系统总览]]
- [[../05_Control/控制架构总览]]
- [[../04_Navigation/导航系统总览]]
