from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    pkg_moveit = get_package_share_directory("four_axis_moveit_config")
    pkg_ros_gz_sim = get_package_share_directory("ros_gz_sim")

    # Path to our custom Gazebo world
    world = os.path.join(
        pkg_moveit,
        "worlds",
        "workcell.sdf",
    )

    # Robot State Publisher
    rsp_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_moveit, "launch", "rsp.launch.py")
        ),
        launch_arguments={
            "use_sim_time": "true"
        }.items()
    )

    # Launch Gazebo with custom world
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, "launch", "gz_sim.launch.py")
        ),
        launch_arguments={
            "gz_args": f"-r {world}"
        }.items()
    )

    # Spawn robot into Gazebo
    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-topic", "robot_description",
            "-name", "four_axis_robot"
        ],
        output="screen",
    )

    # Bridge Gazebo clock to ROS
    clock_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            "/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock"
        ],
        output="screen",
    )

    # Spawn Joint State Broadcaster
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
        parameters=[{"use_sim_time": True}],
        output="screen",
    )

    # Spawn Arm Controller
    arm_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["arm_controller"],
        parameters=[{"use_sim_time": True}],
        output="screen",
    )

    return LaunchDescription([
        rsp_launch,
        gazebo,
        spawn_robot,
        clock_bridge,
        TimerAction(
            period=5.0,
            actions=[joint_state_broadcaster_spawner]
        ),
        TimerAction(
            period=7.0,
            actions=[arm_controller_spawner]
        ),
    ])