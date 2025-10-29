import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Get the package directory
    pkg_four_wheeled_robot = get_package_share_directory('four_wheeled_robot')
    
    # Define paths
    urdf_path = os.path.join(pkg_four_wheeled_robot, 'urdf', 'robot.urdf.xacro')

    # Arguments
    use_rviz = LaunchConfiguration('use_rviz', default='true')
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    # 1. Start Gazebo simulation (empty world)
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
        launch_arguments={'world': 'empty.world'}.items(),
    )

    # 2. Xacro to URDF conversion
    robot_description_content = Node(
        package='xacro',
        executable='xacro',
        arguments=[urdf_path],
        name='xacro_to_urdf',
        output='screen'
    )
    
    # 3. Publish the robot model to the 'robot_description' topic
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[
            {'use_sim_time': use_sim_time},
            {'robot_description': robot_description_content.execute()} # Pass the generated URDF string
        ],
    )
    
    # 4. Spawn the robot in Gazebo
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'four_wheeled_robot'],
                        output='screen')

    # 5. RViz Visualization
    rviz_config_file = os.path.join(pkg_four_wheeled_robot, 'config', 'default.rviz')
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file],
        condition=launch.conditions.IfCondition(use_rviz)
    )

    return LaunchDescription([
        DeclareLaunchArgument('use_rviz', default_value='true', description='Set to true to launch RViz'),
        gazebo,
        robot_state_publisher,
        spawn_entity,
        rviz_node,
    ])
