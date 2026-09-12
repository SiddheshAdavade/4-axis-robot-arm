from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    pkg_moveit = get_package_share_directory("four_axis_moveit_config")

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_moveit, "launch", "gazebo.launch.py")
        )
    )

    move_group_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_moveit, "launch", "move_group.launch.py")
        )
    )

    rviz_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_moveit, "launch", "moveit_rviz.launch.py")
        )
    )

    return LaunchDescription([
        gazebo_launch,

        # Give Gazebo, robot spawn, and controllers time to initialize
        TimerAction(
            period=8.0,
            actions=[move_group_launch],
        ),

        TimerAction(
            period=10.0,
            actions=[rviz_launch],
        ),
    ])