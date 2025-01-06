from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Node for teleop keyboard control
        Node(
            package='bot_description',  # Replace with your package name
            executable='teleop_keyboard',  # Replace with your teleop script's name
            name='teleop_keyboard',
            output='screen',
            parameters=[{
                'use_sim_time': True  # If you're using Gazebo or simulation
            }]
        ),
    ])
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Node for teleop keyboard control
        Node(
            package='bot_description',  # Replace with your package name
            executable='teleop_keyboard',  # Replace with your teleop script's name
            name='teleop_keyboard',
            output='screen',
            parameters=[{
                'use_sim_time': True  # If you're using Gazebo or simulation
            }]
        ),
    ])

