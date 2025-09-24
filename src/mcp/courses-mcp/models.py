"""
IT Courses data models - Data classes for course objects.
"""

from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class Course:
    id: str
    title: str
    duration: str
    start_date: str
    description: str
    category: str
    level: Optional[str] = None
    instructor: Optional[str] = None
    price: Optional[float] = None
    max_students: Optional[int] = None
    prerequisites: Optional[List[str]] = None
    skills_covered: Optional[List[str]] = None
    role: Optional[List[str]] = None


@dataclass
class CourseDetails:
    course: Course
    syllabus: Optional[List[str]] = None
    learning_outcomes: Optional[List[str]] = None
    certification: Optional[str] = None
    enrollment_count: Optional[int] = None
    rating: Optional[float] = None
    reviews_count: Optional[int] = None


@dataclass
class CoursesList:
    category: Optional[str] = None
    total_count: int = 0
    courses: List[Course] = None


@dataclass
class SearchFilters:
    category: Optional[str] = None
    level: Optional[str] = None
    role: Optional[str] = None
    duration_max: Optional[str] = None
    start_date_from: Optional[str] = None
    start_date_to: Optional[str] = None