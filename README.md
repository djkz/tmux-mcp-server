# Tmux MCP Server

A Model Control Protocol (MCP) server that provides tools for interacting with tmux sessions. This server enables AI assistants to read from and write to active terminal sessions without interrupting ongoing processes.

## Features

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

### Tmux Tools
- `list_sessions`: List all available tmux sessions
- `read_buffer`: Read the buffer content from a specified tmux terminal
- `execute_command`: Execute a command in a specific tmux terminal

## Use Cases

### Interactive REPL Sessions

The tmux-mcp-server is particularly useful for working with interactive REPL (Read-Eval-Print Loop) environments such as:

- **Rails Console**: Read output and send commands to a Rails console without blocking execution
- **Python Interactive Shell**: Monitor and interact with a running Python shell
- **Node.js REPL**: Send JavaScript snippets and view results asynchronously

### Long-Running Processes

Monitor and interact with long-running processes:

- **Database Migrations**: Track progress of migrations without interrupting them
- **Build Processes**: Check build status and logs without having to stop the build
- **Server Logs**: Read logs in real-time while maintaining the ability to send commands

### Multi-Session Workflows

Coordinate work across multiple terminal sessions:

- **Database & Application**: Interact with both a database console and application server in parallel
- **Front-end & Back-end**: Monitor both front-end and back-end development servers
- **Testing & Development**: Run tests in one session while continuing development in another

### AI Assistant Integration

Enable AI assistants (like Claude) to:

- Read terminal output without interrupting the active process
- Send commands to terminals when requested
- Monitor multiple terminal sessions simultaneously
- Work with interactive tools that would otherwise be incompatible with standard stdin/stdout interaction

## Development

When extending this server:

1. New tools can be added using the `@mcp.tool()` decorator
2. New resources can be added using the `@mcp.resource()` decorator
3. Follow the existing pattern for type hints and docstrings