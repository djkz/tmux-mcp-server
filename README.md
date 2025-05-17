# Tmux MCP Server

A Model Control Protocol (MCP) server that provides tools for interacting with tmux sessions.

## Features

- **Add Numbers**: Basic addition tool that adds two integers
- **Tmux Session Management**: List available tmux sessions
- **Tmux Buffer Reading**: Read buffer content from a tmux terminal
- **Tmux Command Execution**: Execute commands in a specific tmux terminal

## Installation

```bash
# Install dependencies using uv
uv pip install -e .
```

## Running the Server

```bash
# Start the MCP server
python server.py
```

## Usage

The server exposes MCP tools that can be used through MCP clients:

### Basic Tools
- `add`: Add two integers together
- `greet`: Get a personalized greeting

### Tmux Tools
- `list_sessions`: List all available tmux sessions
- `read_buffer`: Read the buffer content from a specified tmux terminal
- `execute_command`: Execute a command in a specific tmux terminal

## Development

When extending this server:

1. New tools can be added using the `@mcp.tool()` decorator
2. New resources can be added using the `@mcp.resource()` decorator
3. Follow the existing pattern for type hints and docstrings