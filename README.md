

1. Prerequisites ⚙️
Ensure you have the following installed on your system. This project specifically targets ROS 2 Humble running on WSL (Windows Subsystem for Linux).

ROS 2 Humble Hawksbill: The base distribution.

Gazebo Garden: The default simulator for ROS 2 Humble.

ros_gz_sim bridge: To allow communication between ROS 2 and Gazebo.

teleop_twist_keyboard: For keyboard control.

xacro: To simplify URDF creation.

Installation Commands (if needed):

Bash
```
# Install Gazebo Garden and the ROS-Gazebo bridge
sudo apt update
sudo apt install ros-humble-gazebo-ros-pkgs ros-humble-ros-gz-sim

# Install xacro
sudo apt install ros-humble-xacro

# Install the keyboard teleoperation package
sudo apt install ros-humble-teleop-twist-keyboard
```

2. Project Setup and Workspace Creation 📁
Create a ROS 2 workspace and a new package for your robot.

Bash
```
# 1. Create a ROS 2 workspace
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

# 2. Create a new package named 'four_wheeled_robot'
ros2 pkg create four_wheeled_robot --build-type ament_cmake --dependencies rclcpp

# 3. Create necessary sub-directories
cd four_wheeled_robot
mkdir launch urdf config
```
