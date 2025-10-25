import logging
from mcp.server.fastmcp import FastMCP
from pydantic import Field
from core.topics.topics_controller import (
    _list_topics,
    _get_topic_info,
    _get_topic_data,
    _publish_topic_data,
)

mcp = FastMCP("ros2-mcp-server")


# List of MCP tools


@mcp.tool()
async def get_topics() -> str:
    """
    Retrieve a list of all active ROS2 topics.

    Returns a comma-separated list of topic names currently available
    in the ROS2 network, including their full paths with leading slashes.

    Example: /chatter, /parameter_events, /rosout
    """
    return _list_topics()


@mcp.tool()
async def get_topic_information(
    topic: str = Field(description="Full topic name with leading slash"),
) -> str:
    """
    Get detailed information about a specific ROS2 topic.

    Provides the message type, number of publishers, and number of subscribers
    for the specified topic. Useful for understanding topic structure and activity.

    Example: Type: std_msgs/msg/String, Publisher count: 1, Subscription count: 0
    """
    return _get_topic_info(topic=topic)


@mcp.tool()
async def get_topic_data(
    topic: str = Field(description="Full topic name with leading slash"),
) -> str:
    """
    Retrieve the latest message data from a ROS2 topic.

    Returns the most recent message published to the specified topic.
    Useful for monitoring topic activity and inspecting current values.

    Note: Requires an active publisher on the topic to receive data.
    """
    return _get_topic_data(topic=topic)


@mcp.tool()
async def publish_topic_data(
    topic: str = Field(description="Full topic name with leading slash"),
    message_type: str = Field(description="ROS2 Message Type"),
    data: str = Field(
        description="""Message data to publish. Format depends on message type:
    - For String messages: just the text (e.g., 'Hello World')
    - For Twist: '{linear: {x: 0.5, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}'
    - For other types: provide complete YAML dictionary structure"""
    ),
) -> str:
    """
    Publish a message to a ROS2 topic.

    For String messages, provide just the text content.
    For complex messages (Twist, etc), provide the full YAML structure.

    Examples:
    - String: data='Hello from robot'
    - Twist: data='{linear: {x: 0.5}, angular: {z: 0.0}}'
    """
    return _publish_topic_data(topic=topic, message_type=message_type, data=data)


def main():
    # Initialize and run the server
    logging.info("ROS2 - MCP SERVER: ready")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
