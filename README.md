# Ogmen
bot_description package:
The bot_description package is designed to provide the robot's model and facilitate its visualization in RViz. This package includes the SDF model of the robot, along with the necessary launch files and RViz configuration files for easy testing and visualization. The package is organized with a clear directory structure: models for storing the robot's SDF file, launch for the RViz launch file, and rviz for any custom RViz configuration files.

To test this package, ensure you have the dependencies robot_state_publisher and rviz2 installed. These can be installed using the command:

**sudo apt install ros-<distro>-robot-state-publisher ros-<distro>-rviz2**

(replace <distro> with your ROS2 distribution, such as humble or iron).

After ensuring all dependencies are met, build the package by navigating to your workspace and running colcon build. Source the workspace with source install/setup.bash to load the package into your ROS2 environment. The robot can be visualized in RViz using the command:

**ros2 launch bot_description rviz.launch.py**

This will open RViz, and you should see the robot model. If the model doesn't appear, verify the file path in the launch file and ensure the SDF file exists in the models directory.


bot_world package:
The bot_world package is created to define and simulate the robot in a Gazebo environment. This package contains the robot's SDF file, the world file for Gazebo, and launch files that handle spawning the robot in the simulation. It is organized with models for the robot description, worlds for the Gazebo world files, and launch for launching the simulation.

To test the package, make sure you have the required dependencies installed: gazebo_ros and robot_state_publisher. These can be installed using the command:

**sudo apt install ros-<distro>-gazebo-ros-pkgs ros-<distro>-robot-state-publisher**

Replace <distro> with your ROS2 distribution, such as humble or iron.

Once dependencies are installed, build the package by running colcon build in your workspace, and then source the workspace using source install/setup.bash. To simulate the robot in Gazebo, launch the provided file with the command:

**ros2 launch bot_world world.launch.py**

Gazebo will open, and the robot should appear in the specified environment. If the robot or the environment does not load, verify the paths in the launch file and ensure the necessary files are correctly placed in the models and worlds directories.

Both packages are structured to ensure easy extensibility and testing, providing a straightforward setup for robotic simulation and visualization tasks.





