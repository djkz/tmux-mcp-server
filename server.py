# server.py
from mcp.server.fastmcp import FastMCP
import sys
import subprocess
from typing import List, Dict, Optional

# Create an MCP server
server = FastMCP("Tmux MCP")


# Add an addition tool
@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@server.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# Tmux utility functions
def get_tmux_sessions() -> List[Dict[str, str]]:
    """Get a list of all tmux sessions as structured data"""
    try:
        # Run tmux command to list sessions
        result = subprocess.run(
            ["tmux", "list-sessions", "-F", "#{session_name}:#{session_id}:#{session_windows}"], 
            capture_output=True, 
            text=True, 
            check=True
        )
        
        # Parse the output
        sessions = []
        for line in result.stdout.strip().split('\n'):
            if line:  # Skip empty lines
                parts = line.split(':')
                if len(parts) >= 3:
                    sessions.append({
                        "name": parts[0],
                        "id": parts[1],
                        "windows": parts[2]
                    })
        return sessions
    except subprocess.CalledProcessError:
        # This occurs if tmux is not running or there are no sessions
        return []
    except Exception as e:
        # Log other errors but return empty list
        print(f"Error listing tmux sessions: {str(e)}")
        return []


# Add a tool to list tmux sessions
@server.tool()
def list_sessions() -> List[Dict[str, str]]:
    """List all available tmux sessions"""
    return get_tmux_sessions()


# Add a tool to read buffer from a tmux terminal
@server.tool()
def read_buffer(session_name: str, start_line: Optional[int] = None, num_lines: Optional[int] = None) -> str:
    """
    Read the buffer content from a specified tmux terminal
    
    Args:
        session_name: Name of the tmux session to read from
        start_line: Optional starting line number (default is beginning of buffer)
        num_lines: Optional number of lines to read (default is all lines)
    
    Returns:
        The content of the tmux buffer as a string
    """
    try:
        # Check if session exists
        sessions = get_tmux_sessions()
        session_exists = any(session["name"] == session_name for session in sessions)
        
        if not session_exists:
            return f"Error: Session '{session_name}' not found"
        
        # Prepare command to capture buffer
        # By default, tmux capture-pane captures the visible content
        # -p prints the content directly to stdout
        # -S and -E specify start and end lines
        cmd = ["tmux", "capture-pane", "-p"]
        
        if start_line is not None:
            cmd.extend(["-S", str(start_line)])
            
            if num_lines is not None:
                end_line = start_line + num_lines - 1
                cmd.extend(["-E", str(end_line)])
        elif num_lines is not None:
            # If only num_lines is specified, capture from the bottom of the buffer
            cmd.extend(["-S", f"-{num_lines}"])
            
        # Add target session
        cmd.extend(["-t", session_name])
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
        
    except subprocess.CalledProcessError as e:
        return f"Error reading tmux buffer: {e.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"


# Add a tool to execute commands in a tmux terminal
@server.tool()
def execute_command(session_name: str, command: str) -> Dict[str, str]:
    """
    Execute a command in a specific tmux terminal
    
    Args:
        session_name: Name of the tmux session to execute the command in
        command: The command to execute
    
    Returns:
        Dictionary with status and message
    """
    try:
        # Check if session exists
        sessions = get_tmux_sessions()
        session_exists = any(session["name"] == session_name for session in sessions)
        
        if not session_exists:
            return {
                "status": "error",
                "message": f"Session '{session_name}' not found"
            }
        
        # Send the command to the tmux session
        # send-keys sends the command to the specified session
        # "C-m" is the equivalent of pressing Enter at the end
        cmd = ["tmux", "send-keys", "-t", session_name, command, "C-m"]
        subprocess.run(cmd, check=True)
        
        return {
            "status": "success",
            "message": f"Command executed in session '{session_name}'"
        }
        
    except subprocess.CalledProcessError as e:
        return {
            "status": "error",
            "message": f"Error executing command: {e.stderr if e.stderr else str(e)}"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error: {str(e)}"
        }


# Start the server if this file is run directly
if __name__ == "__main__":
    print("Starting MCP server...")
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    
    # Get MCP version for verification
    import mcp
    print(f"MCP version: {getattr(mcp, '__version__', 'unknown')}")
    
    # Run the server
    try:
        print("About to start server...")
        server.run()
        print("Server started successfully!")
    except Exception as e:
        sys.stderr.write(f"Error starting server: {str(e)}\n")
        import traceback
        traceback.print_exc()
