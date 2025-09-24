"""
Utility functions for hr competency operations.
"""

from models import Competency, Employee

def get_competency_by_id(id: int) -> Competency:
    """Get a competency by its ID"""
    for competency in MOCK_COMPETENCIES:
        if competency["id"] == id:
            return competency
    return None

def get_employee_by_id(id: int) -> Employee:
    """Get an employee by their ID"""
    for employee in MOCK_EMPLOYEES:
        if employee["id"] == id:
            return employee
    return None
