from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Declare the world file path dynamically using the bot_world package
    world_file = LaunchConfiguration(
        'world_file',
        default=FindPackageShare('bot_world').find('bot_world') + '/worlds/squareworld.world'
    )

    return LaunchDescription([
        # Declare the argument for the world file
        DeclareLaunchArgument(
            'world_file',
            default_value=world_file,
            description='Path to the world file to launch in Gazebo'
        ),

        # Execute Gazebo with the specified world file and ROS plugins
        ExecuteProcess(
            cmd=[
                'gazebo', '--verbose',
                '-s', 'libgazebo_ros_init.so',  # Load Gazebo ROS initialization plugin
                '-s', 'libgazebo_ros_factory.so',  # Load Gazebo ROS factory plugin
                LaunchConfiguration('world_file')  # Pass the world file
            ],
            output='screen'
        )
    ])

