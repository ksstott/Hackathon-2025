"""
hr competency mcp server - discover and explore competencies and related employees.

to run this server:
    uv run mcp dev main.py
"""

from typing import Dict, Any, Optional, List
from mcp.server.fastmcp import FastMCP

from competency_service import (
    search_competencies_data,
    get_competency_details_data,
    format_competencies_list,
    get_competency_summary_prompt,
    get_available_categories,
)


# create an mcp server
mcp = FastMCP("hr-competency-mcp", port=8010)


# tools
@mcp.tool()
def search_competencies(
    name: Optional[str] = None,
    category: Optional[str] = None,
    level: Optional[str] = None,
) -> Dict[str, Any]:
    """search for competencies with optional filters"""
    return search_competencies_data(name, category, level)


@mcp.tool()
def get_competency_details(competency_id: int) -> Dict[str, Any]:
    """get detailed information about a specific competency"""
    return get_competency_details_data(competency_id)


@mcp.tool()
def search_and_format_competencies(
    name: Optional[str] = None,
    category: Optional[str] = None,
    level: Optional[str] = None,
) -> str:
    """search for competencies and return formatted results"""
    data = search_competencies_data(name, category, level)
    return format_competencies_list(data)


@mcp.tool()
def get_competency_categories() -> List[str]:
    """get list of available competency categories"""
    return get_available_categories()


# resources
@mcp.resource("competency://{competency_id}")
def competency_resource(competency_id: int) -> str:
    """get competency information as a formatted resource"""
    data = get_competency_details_data(competency_id)
    if "error" in data:
        return data["error"]

    c = data["competency"]
    formatted = f"🧩 {c['name']}\n"
    formatted += f"   id: {c['id']}\n"
    formatted += f"   category: {c['category'].title()}\n"
    formatted += f"   level: {c.get('level', 'not specified').title()}\n"
    formatted += f"   description: {c['description']}\n"
    formatted += "\n"
    employees = data.get("related_employees") or []
    if employees:
        formatted += "related employees:\n"
        for e in employees[:10]:
            formatted += f" - {e['name']} ({e['position']}, {e['department']})\n"
    else:
        formatted += "no related employees found.\n"
    return formatted


@mcp.resource("competencies://category/{category}")
def competencies_by_category_resource(category: str) -> str:
    """get competencies in a category as a formatted resource"""
    data = search_competencies_data(category=category)
    return format_competencies_list(data)


# prompts
@mcp.prompt()
def competency_planning_prompt(category: Optional[str] = None) -> str:
    """generate a prompt for competency planning or exploration"""
    return get_competency_summary_prompt(category)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")