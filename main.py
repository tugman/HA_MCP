# Imports
from mcp.server.fastmcp import FastMCP




# Instantiate the MCP server client
mcp = FastMCP("Hello, and welcome to HA MCP:-)")



# To Do define MCP tools like :
#@mcp.tool()
#def cos(a: int) -> float:
#    """cos of a number"""
#    return float(math.cos(a))









# Execute and return the sse output
if __name__ == "__main__":
    mcp.run(transport="sse")
