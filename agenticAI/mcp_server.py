from fastmcp import FastMCP
import subprocess

mcp = FastMCP("Docker MCP Server") #instance

@mcp.tool()
def show_running_container():
    """tool 1 showing running containers"""
    result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
    return result.stdout

@mcp.tool()
def show_container_logs_by_name(container_name):
    """tool 2 showing running container logs by name"""
    result = subprocess.run(["docker","logs", container_name], capture_output=True, text=True )
    return result.stdout

if __name__ == "__main__":
    mcp.run()