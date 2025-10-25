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


"""Get information from an active ROS2 topic"""


def _get_topic_info(topic: str) -> str:
    # Get information of an active ROS2 topic

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


"""Get data publicated from an active ROS2 topic"""


def _get_topic_data(topic: str) -> str:
    # Get information of an active ROS2 topic

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


"""Publish information on an active ROS2 topic"""


def _publish_topic_data(topic: str, message_type: str, data: str) -> str:
    # Publish information on an active ROS2 topic

    result = subprocess.run(
        [
            "/opt/ros/jazzy/bin/ros2",
            "topic",
            "pub",
            "--once",
            f"{topic}",
            f"{message_type}",
            f"data: {data}",
        ],
        capture_output=True,
        text=True,
        env=setup_ros2_env(),
    )

    if result.returncode != 0:
        return f"Error: {result.stderr}"

    return f"Published to f{topic}"
