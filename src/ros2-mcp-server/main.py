import logging
from mcp.server.fastmcp import FastMCP
from pydantic import Field
from core.topics.topics_controller import _list_topics, _get_topic_info, _get_topic_data

mcp = FastMCP("ros2-mcp-server")


# List of MCP tools


@mcp.tool()
async def get_topics() -> str:
    return _list_topics()


@mcp.tool()
async def get_topic_information(
    topic: str = Field(description="Full topic name with leading slash"),
) -> str:
    return _get_topic_info(topic)


@mcp.tool()
async def get_topic_data(
    topic: str = Field(description="Full topic name with leading slash"),
) -> str:
    return _get_topic_data(topic)


def main():
    # Initialize and run the server
    logging.info("ROS2 - MCP SERVER: ready")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
