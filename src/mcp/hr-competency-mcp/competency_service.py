"""
hr competency service - employee lookup utilities.
"""

from typing import Dict, Any, Optional, List
from config import MOCK_EMPLOYEES


def search_employees_data(
    department: Optional[str] = None,
    position: Optional[str] = None,
    competency_id: Optional[str] = None,
) -> Dict[str, Any]:
    """search employees by department, position, and/or competency id."""
    filtered: List[Dict[str, Any]] = list(MOCK_EMPLOYEES)

    if department:
        dept_l = department.lower()
        filtered = [
            e for e in filtered if (e.get("department") or "").lower() == dept_l
        ]

    if position:
        pos_l = position.lower()
        filtered = [
            e for e in filtered if (e.get("position") or "").lower() == pos_l
        ]

    if competency_id:
        cid = str(competency_id)
        filtered = [e for e in filtered if cid in (e.get("competencies") or [])]

    return {
        "total_count": len(filtered),
        "employees": [
            {
                "id": e["id"],
                "name": e["name"],
                "email": e["email"],
                "phone": e["phone"],
                "department": e["department"],
                "position": e["position"],
                "competencies": e.get("competencies", []),
            }
            for e in filtered
        ],
    }
