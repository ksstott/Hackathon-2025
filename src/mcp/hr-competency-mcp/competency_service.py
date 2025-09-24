"""
hr competency service - business logic for managing and searching competencies.
"""

from typing import Dict, Any, Optional, List
from models import Competency
from config import MOCK_COMPETENCIES, MOCK_EMPLOYEES
import random


# helpers
def competency_to_dict(competency: Dict[str, Any]) -> Dict[str, Any]:
    """convert competency to dictionary (already dict in mock)."""
    return {
        "id": competency["id"],
        "name": competency["name"],
        "description": competency["description"],
        "category": competency["category"],
        "level": competency["level"],
        "required_skills": competency.get("required_skills", []),
        "required_experience": competency.get("required_experience", []),
        "required_education": competency.get("required_education", []),
        "required_certifications": competency.get("required_certifications", []),
        "required_licenses": competency.get("required_licenses", []),
        "required_other": competency.get("required_other", []),
    }


def get_available_categories() -> List[str]:
    """return list of allowed competency categories."""
    return [
        "programming",
        "cloud",
        "devops",
        "data",
        "security",
        "web",
        "mobile",
        "database",
    ]


# queries
def search_competencies_data(
    name: Optional[str] = None,
    category: Optional[str] = None,
    level: Optional[str] = None,
) -> Dict[str, Any]:
    """
    search for competencies with optional filters.

    args:
        name: free-text search over name
        category: allowed category (or comma-separated list)
        level: beginner, intermediate, advanced

    returns:
        dictionary containing list data
    """

    filtered: List[Dict[str, Any]] = list(MOCK_COMPETENCIES)

    if name:
        name_l = name.lower()
        filtered = [c for c in filtered if name_l in c["name"].lower()]

    if category:
        categories = [cat.strip().lower() for cat in category.split(",")]
        filtered = [c for c in filtered if c.get("category", "").lower() in categories]

    if level:
        level_l = level.lower()
        filtered = [c for c in filtered if c.get("level", "").lower() == level_l]

    return {
        "total_count": len(filtered),
        "competencies": [competency_to_dict(c) for c in filtered],
    }


def get_competency_details_data(competency_id: int) -> Dict[str, Any]:
    """
    get detailed information about a specific competency, including matching employees.

    args:
        competency_id: unique identifier

    returns:
        dictionary with competency, related employees, and meta
    """

    competency = next((c for c in MOCK_COMPETENCIES if c["id"] == competency_id), None)
    if not competency:
        return {"error": f"competency with id '{competency_id}' not found"}

    # employees who have this competency id
    related_employees = [
        e for e in MOCK_EMPLOYEES if competency_id in (e.get("competencies") or [])
    ]

    # simple mocked metrics
    relevance_score = round(random.uniform(0.7, 0.99), 2)
    popularity_rank = random.randint(1, 10)

    return {
        "competency": competency_to_dict(competency),
        "related_employees": [
            {
                "id": e["id"],
                "name": e["name"],
                "email": e["email"],
                "department": e["department"],
                "position": e["position"],
            }
            for e in related_employees
        ],
        "metrics": {
            "relevance_score": relevance_score,
            "popularity_rank": popularity_rank,
        },
    }


# formatting utilities
def format_competencies_list(data: Dict[str, Any]) -> str:
    """format competencies list for display."""
    competencies = data.get("competencies") or []
    if not competencies:
        return "no competencies found matching your criteria."

    formatted = f"found {data.get('total_count', 0)} competence(s)\n\n"
    for c in competencies:
        formatted += f"🧩 {c['name']}\n"
        formatted += f"   id: {c['id']}\n"
        formatted += f"   category: {c['category'].title()}\n"
        formatted += f"   level: {c.get('level', 'not specified').title()}\n"
        formatted += f"   description: {c['description']}\n\n"
    return formatted


def get_competency_summary_prompt(category: Optional[str] = None) -> str:
    """generate a prompt for competency exploration or recommendations."""
    if category:
        return (
            f"please help me explore {category} competencies. i'm interested in:\n"
            f"1. understanding core skills and requirements\n"
            f"2. mapping them to roles and seniority levels\n"
            f"3. identifying learning resources to upskill\n\n"
            f"can you list relevant competencies and suggest next steps?"
        )
    return (
        "please help me review available competency categories and typical requirements. i'm looking to:\n"
        "1. assess current skills against expectations\n"
        "2. find gaps and suggested training\n"
        "3. plan a growth roadmap by level\n\n"
        "can you show the categories and help me explore options?"
    )
