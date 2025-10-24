# ROS2 MCP Server

A Model Context Protocol (MCP) server that provides tools for interacting with ROS2 (Robot Operating System 2) topics. This server allows you to list active ROS2 topics, retrieve information about specific topics, and fetch data from topics using MCP-compatible tools.

## Architecture

The server interacts with ROS2 through subprocess calls to the ROS2 command-line tools (`ros2 topic list`, `ros2 topic info`, `ros2 topic echo`), rather than using a ROS2 client library. This approach provides a lightweight integration that doesn't require initializing a full ROS2 node, making it suitable for tooling and development environments. The ROS2 environment is set up programmatically by configuring the necessary environment variables (AMENT_PREFIX_PATH, PYTHONPATH, LD_LIBRARY_PATH, PATH) to point to the ROS2 Jazzy installation.

## Features

- **List Topics**: Retrieve a list of all currently active ROS2 topics.
- **Topic Information**: Get detailed information about a specific ROS2 topic, including message type, publisher count, and subscriber count.
- **Topic Data**: Fetch the latest data published on a specific ROS2 topic.

## Requirements

- Python 3.14.0 or higher
- ROS2 Jazzy Jalisco installed and sourced
- MCP library (version 1.18.0 or higher)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd ros2-mcp-server
   ```

2. Install dependencies using uv:
   ```bash
   uv sync
   ```

3. Ensure ROS2 Jazzy is installed and properly sourced in your environment.

## Usage

Run the MCP server using uv:

```bash
uv run src/ros2-mcp-server/main.py
```

The server communicates via stdio and provides three main tools:

### Tools

1. **get_topics**
   - Lists all active ROS2 topics
   - Returns: String with topic count and list of topics

2. **get_topic_information**
   - Retrieves information about a specific topic
   - Parameters:
     - `topic`: Full topic name with leading slash (e.g., "/chatter")
   - Returns: Topic type, publisher count, and subscriber count

3. **get_topic_data**
   - Fetches the latest data from a topic
   - Parameters:
     - `topic`: Full topic name with leading slash (e.g., "/chatter")
   - Returns: Latest published message data

## Project Structure

```
src/ros2-mcp-server/
├── main.py                 # Main MCP server entry point
├── core/
│   ├── topics/
│   │   ├── topics_controller.py  # ROS2 topic interaction logic
│   │   └── __init__.py
│   └── __init__.py
├── setup/
│   ├── ros2_env.py         # ROS2 environment setup
│   └── __init__.py
└── __init__.py
```

## Development

This project uses:
- **uv** for dependency management
- **Black** for code formatting
- **Ruff** for linting

To run development tools:

```bash
# Format code
uv run black .

# Lint code
uv run ruff check .
```

## License

Copyright 2024 [Mars Rover UdeGSpace]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.