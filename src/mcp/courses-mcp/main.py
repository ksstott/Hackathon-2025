from mcp.server.fastmcp import FastMCP
    # Create an MCP server
    # you can add the port here so that it doesnt clash with other mcp servers
mcp = FastMCP("courses")
   
    # Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

    
if __name__ == "__main__":
    mcp.run("streamable-http")