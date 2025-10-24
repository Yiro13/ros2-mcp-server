import os


def setup_ros2_env():
    # ROS2 Environment
    env = os.environ.copy()
    env.update(
        {
            "AMENT_PREFIX_PATH": "/opt/ros/jazzy",
            "PYTHONPATH": "/opt/ros/jazzy/lib/python3.12/site-packages",
            "LD_LIBRARY_PATH": "/opt/ros/jazzy/lib",
            "PATH": f"/opt/ros/jazzy/bin:{env.get('PATH', '')}",
        }
    )

    return env
