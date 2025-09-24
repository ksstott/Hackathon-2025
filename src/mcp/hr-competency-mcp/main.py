"""
hr competency mcp server - discover and explore competencies and related employees.

to run this server:
    uv run mcp dev main.py
"""

from typing import Dict, Any, Optional
from mcp.server.fastmcp import FastMCP

from competency_service import search_employees_data


# create an mcp server
mcp = FastMCP("hr-competency-mcp", port=8010)


# tools
@mcp.tool()
def search_employees(
    department: Optional[str] = None,
    position: Optional[str] = None,
    competency_id: Optional[str] = None,
) -> Dict[str, Any]:
    """search employees by department, position, and/or competency id"""
    return search_employees_data(department, position, competency_id)

@mcp.resource("employees://search/{department}/{position}/{competency_id}")
def employees_resource(department: str, position: str, competency_id: str) -> str:
    data = search_employees_data(department, position, competency_id)
    formatted = f"found {data.get('total_count', 0)} employee(s)\n\n"
    for e in data["employees"][:50]:
        formatted += f"👤 {e['name']}\n"
        formatted += f"   id: {e['id']}\n"
        formatted += f"   email: {e['email']}\n"
        formatted += f"   phone: {e['phone']}\n"
        formatted += f"   department: {e['department']}\n"
        formatted += f"   position: {e['position']}\n"
        formatted += f"   competencies: {', '.join(e.get('competencies') or [])}\n\n"
    return formatted

# no resources are defined; use the tool-only api
if __name__ == "__main__":
    mcp.run(transport="streamable-http")