# 🚀 robot_speed_calculator

A simple ROS 2 Humble package that calculates a robot's linear speed based on wheel RPM and diameter.

## 📦 Package Overview

This package includes:
- A ROS 2 Python node that subscribes to or accepts parameters for RPM and wheel size.
- Computes and publishes or prints the robot's linear speed.
- Lightweight and easy to integrate.

## 🛠️ Installation

Clone the package into your ROS 2 workspace and build it:

```bash
cd ~/ros2_ws/src
mkdir robot_speed
cd robot_speed
git clone https://github.com/Vishalkm206/simple-robot-speed-calculator-using-ROS2_Humble.git
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
terminal 1: ros2 run robot_speed calc_speed
terminal 2 : ros2 run robot_speed rpm_publisher
