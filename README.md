 1. Prerequisites ⚙️
Ensure you have the following installed on your system. This project specifically targets ROS 2 Humble running on WSL (Windows Subsystem for Linux).

ROS 2 Humble Hawksbill: The base distribution.

Gazebo Garden: The default simulator for ROS 2 Humble.

ros_gz_sim bridge: To allow communication between ROS 2 and Gazebo.

teleop_twist_keyboard: For keyboard control.

xacro: To simplify URDF creation.

Installation Commands:

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

3. Robot Description (URDF/Xacro) 📐
The Universal Robot Description Format (URDF) defines the physical properties of the robot. We use Xacro for a cleaner, modular file structure.
```
  Check this github repo for the codes you are to copy
```
 
4. Launch Files (Python) 🚀
This launch file starts the Gazebo simulation, loads the robot model, and optionally launches RViz for visualization.
```
  Check this github repo for the codes you are to copy
```
 
5. Configuration and Setup 💾
A. RViz Configuration
Create an empty RViz configuration file to avoid errors on first run.
```
  Check this github repo for the codes you are to copy
```

B. Update package.xml
Make sure your package.xml declares the necessary dependencies for the build and execution.
```
  Check this github repo for the codes you are to copy
```

C. Update CMakeLists.txt
```
  Check this github repo for the codes you are to copy
```

6. Build and Run the Project 🏃
A. Build the Workspace
Navigate to your workspace root and build the package.

Bash
```
cd ~/ros2_ws
colcon build --packages-select four_wheeled_robot
```

B. Source the Workspace
Source the setup file to make the new package available.

Bash
```
# In your terminal
source install/setup.bash
```

C. Launch the Simulation
Start the robot in Gazebo and RViz.
Bash
```
ros2 launch four_wheeled_robot start_simulation.launch.py
```

D. Control the Robot (Teleoperation)
In a new terminal, source the workspace and run the keyboard teleop node.

Bash
```
# New terminal
source ~/ros2_ws/install/setup.bash
```
# Run the teleop node, mapping to the 'cmd_vel' topic
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=cmd_vel
```
Now, the robot in Gazebo should respond to the key commands displayed in the terminal!
<img width="1366" height="768" alt="Screenshot (209)" src="https://github.com/user-attachments/assets/e0cde235-14e2-4e94-907a-dd8d2c69f63a" />
