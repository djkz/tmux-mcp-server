# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a tmux-mcp-server project that uses the Model Control Protocol (MCP) library to create a FastMCP server. The server provides simple tools and resources through the MCP interface.

## Environment Setup

- Python 3.12+ is required
- The project uses uv for dependency management

## Commands

### Installation

```bash
# Install dependencies using uv
uv pip install -e .
```

### Running the Server

```bash
# Start the MCP server
python server.py
```

## Code Structure

- `server.py` - Main server file that defines the FastMCP server with:
  - A simple addition tool that adds two integers
  - A greeting resource that returns a personalized greeting

## Development Guidelines

When extending this server:

1. New tools can be added using the `@mcp.tool()` decorator
2. New resources can be added using the `@mcp.resource()` decorator
3. Follow the existing pattern for type hints and docstrings