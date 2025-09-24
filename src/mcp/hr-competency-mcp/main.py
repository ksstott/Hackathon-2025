from mcp.server.fastmcp import FastMCP

# Create an MCP server
# you can add the port here so that it doesnt clash with other mcp servers
mcp = FastMCP("hr-competency-mcp")

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

def main():
    print("Hello from hr-competency-mcp!")
    mcp.run("streamable-http")

if __name__ == "__main__":
   main()