import subprocess
from setup.ros2_env import setup_ros2_env


"""Get list of all active ROS2 topics"""


def _list_topics() -> str:
    # Get list of all active ROS2 topics

    result = subprocess.run(
        ["/opt/ros/jazzy/bin/ros2", "topic", "list"],
        capture_output=True,
        text=True,
        env=setup_ros2_env(),
    )

    if result.returncode != 0:
        return f"Error: {result.stderr}"

    topics_list = result.stdout.strip().split("\n")
    return f"Found {len(topics_list)} ROS2 topics: {', '.join(topics_list)}"


"""Get information from an active ROS2 topics"""


def _get_topic_info(topic: str) -> str:
    # Get information of an active ROS2 topics

    result = subprocess.run(
        ["/opt/ros/jazzy/bin/ros2", "topic", "info", f"{topic}"],
        capture_output=True,
        text=True,
        env=setup_ros2_env(),
    )

    if result.returncode != 0:
        return f"Error: {result.stderr}"

    topic_info = result.stdout.strip().split("\n")
    return f"Information from {topic}: {', '.join(topic_info)}"


"""Get data publicated from an active ROS2 topics"""


def _get_topic_data(topic: str) -> str:
    # Get information of an active ROS2 topics

    result = subprocess.run(
        ["/opt/ros/jazzy/bin/ros2", "topic", "echo", f"{topic}", "--once"],
        capture_output=True,
        text=True,
        env=setup_ros2_env(),
    )

    if result.returncode != 0:
        return f"Error: {result.stderr}"

    topic_data = result.stdout.strip().split("\n")
    return f"Data from {topic}: {', '.join(topic_data)}"
