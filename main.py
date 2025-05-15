# Import
from mcp.server.fastmcp import FastMCP

# Instantiate the MCP server client
mcp = FastMCP("Hello, and welcome to HA MCP :-)")


# execute and return the sse output
if __name__ == "__main__":
    mcp.run(transport="sse")


# To Do


