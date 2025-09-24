"""
HR competency data models - Data classes for hr competency objects.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class Competency:
    id: int
    name: str
    description: str
    category: str
    level: str
    required_skills: List[str]
    required_experience: List[str]
    required_education: List[str]
    required_certifications: List[str]
    required_licenses: List[str]
    required_other: List[str]

@dataclass
class Employee:
    id: int
    name: str
    email: str
    phone: str
    department: str
    position: str
    competencies: List[Competency]
