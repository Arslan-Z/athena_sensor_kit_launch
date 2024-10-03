from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='topic_tools',
            executable='throttle',
            arguments=['messages', '/sensing/imu/vn100/imu/data', '20', '/sensing/imu/vn100/imu/data/throttle'],
            name='throttle_imu_data',
            output='screen'
        ),
        Node(
            package='topic_tools',
            executable='throttle',
            arguments=['messages', '/localization/kinematic_state', '20', '/localization/kinematic_state/throttle'],
            name='throttle_kinematic_state',
            output='screen'
        )
    ])
