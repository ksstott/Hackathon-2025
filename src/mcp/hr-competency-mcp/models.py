"""
HR competency data models - Data classes for hr competency objects.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class Employee:
    id: int
    name: str
    email: str
    phone: str
    department: str
    position: str
    competencies: List[str] # ids of the courses attended
