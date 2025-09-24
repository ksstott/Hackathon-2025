"""
IT Courses service - Business logic for managing and searching IT courses.
"""

from typing import Dict, Any, Optional, List
from models import Course, CourseDetails, CoursesList
import random
from datetime import datetime, timedelta


# Mock database of IT courses
MOCK_COURSES = [
    # Programming courses
    Course(
        id="prog_001",
        title="Python Programming Fundamentals",
        duration="8 weeks",
        start_date="2025-02-01",
        description="Learn Python from scratch with hands-on projects covering data structures, OOP, and web development basics.",
        category="programming",
        level="beginner",
        instructor="Dr. Sarah Chen",
        price=299.99,
        max_students=30,
        prerequisites=[],
        skills_covered=["Python basics", "Data structures", "File handling", "APIs", "Testing"]
    ),
    Course(
        id="prog_002",
        title="Advanced JavaScript and TypeScript",
        duration="12 weeks",
        start_date="2025-02-15",
        description="Master modern JavaScript ES6+ and TypeScript for building scalable web applications.",
        category="programming",
        level="intermediate",
        instructor="Michael Rodriguez",
        price=399.99,
        max_students=25,
        prerequisites=["Basic JavaScript knowledge"],
        skills_covered=["ES6+", "TypeScript", "Async programming", "Design patterns"]
    ),
    Course(
        id="prog_003",
        title="Java Spring Boot Microservices",
        duration="10 weeks",
        start_date="2025-03-01",
        description="Build enterprise-grade microservices with Java Spring Boot, Docker, and Kubernetes.",
        category="programming",
        level="advanced",
        instructor="James Wilson",
        price=549.99,
        max_students=20,
        prerequisites=["Java fundamentals", "REST APIs"],
        skills_covered=["Spring Boot", "Microservices", "Docker", "REST APIs", "Testing"]
    ),
    
    # Cloud courses
    Course(
        id="cloud_001",
        title="AWS Solutions Architect Associate",
        duration="12 weeks",
        start_date="2025-02-10",
        description="Comprehensive preparation for AWS Solutions Architect Associate certification with hands-on labs.",
        category="cloud",
        level="intermediate",
        instructor="Lisa Thompson",
        price=599.99,
        max_students=35,
        prerequisites=["Basic cloud concepts"],
        skills_covered=["EC2", "S3", "VPC", "Lambda", "RDS", "IAM"]
    ),
    Course(
        id="cloud_002",
        title="Azure Fundamentals AZ-900",
        duration="6 weeks",
        start_date="2025-02-20",
        description="Introduction to Microsoft Azure cloud services and preparation for AZ-900 certification.",
        category="cloud",
        level="beginner",
        instructor="David Park",
        price=349.99,
        max_students=40,
        prerequisites=[],
        skills_covered=["Azure services", "Cloud concepts", "Security", "Compliance"]
    ),
    Course(
        id="cloud_003",
        title="Google Cloud Platform Professional",
        duration="14 weeks",
        start_date="2025-03-15",
        description="Advanced GCP architecture, deployment, and optimization strategies for enterprise solutions.",
        category="cloud",
        level="advanced",
        instructor="Maria Garcia",
        price=699.99,
        max_students=25,
        prerequisites=["Cloud architecture basics", "Networking fundamentals"],
        skills_covered=["GCP services", "BigQuery", "Kubernetes Engine", "Cloud Functions"]
    ),
    
    # DevOps courses
    Course(
        id="devops_001",
        title="Docker and Kubernetes Mastery",
        duration="10 weeks",
        start_date="2025-02-05",
        description="Complete containerization and orchestration with Docker and Kubernetes for production environments.",
        category="devops",
        level="intermediate",
        instructor="Alex Kumar",
        price=449.99,
        max_students=30,
        prerequisites=["Linux basics", "Basic networking"],
        skills_covered=["Docker", "Kubernetes", "Helm", "CI/CD", "Monitoring"]
    ),
    Course(
        id="devops_002",
        title="CI/CD Pipeline with Jenkins and GitLab",
        duration="8 weeks",
        start_date="2025-02-25",
        description="Build robust CI/CD pipelines using Jenkins, GitLab CI, and infrastructure as code.",
        category="devops",
        level="intermediate",
        instructor="Tom Anderson",
        price=399.99,
        max_students=25,
        prerequisites=["Git", "Basic scripting"],
        skills_covered=["Jenkins", "GitLab CI", "Pipeline as Code", "Testing automation"]
    ),
    
    # Data courses
    Course(
        id="data_001",
        title="Data Science with Python",
        duration="16 weeks",
        start_date="2025-02-01",
        description="Comprehensive data science bootcamp covering statistics, ML, and deep learning with Python.",
        category="data",
        level="intermediate",
        instructor="Dr. Emily Watson",
        price=799.99,
        max_students=30,
        prerequisites=["Python basics", "Basic statistics"],
        skills_covered=["Pandas", "NumPy", "Scikit-learn", "TensorFlow", "Data visualization"]
    ),
    Course(
        id="data_002",
        title="Machine Learning Engineering",
        duration="12 weeks",
        start_date="2025-03-01",
        description="Build and deploy ML models at scale with MLOps best practices.",
        category="data",
        level="advanced",
        instructor="Dr. Robert Lee",
        price=899.99,
        max_students=20,
        prerequisites=["ML fundamentals", "Python", "Cloud basics"],
        skills_covered=["MLOps", "Model deployment", "A/B testing", "Feature engineering"]
    ),
    
    # Security courses
    Course(
        id="sec_001",
        title="Cybersecurity Fundamentals",
        duration="10 weeks",
        start_date="2025-02-15",
        description="Essential cybersecurity concepts, threat analysis, and defensive strategies.",
        category="security",
        level="beginner",
        instructor="Kevin Miller",
        price=449.99,
        max_students=35,
        prerequisites=[],
        skills_covered=["Network security", "Cryptography", "Risk assessment", "Incident response"]
    ),
    Course(
        id="sec_002",
        title="Ethical Hacking and Penetration Testing",
        duration="14 weeks",
        start_date="2025-03-10",
        description="Hands-on ethical hacking techniques and penetration testing methodologies.",
        category="security",
        level="advanced",
        instructor="Hannah Black",
        price=749.99,
        max_students=25,
        prerequisites=["Networking", "Linux", "Basic security concepts"],
        skills_covered=["Penetration testing", "Vulnerability assessment", "Metasploit", "Web app security"]
    ),
    
    # Web development courses
    Course(
        id="web_001",
        title="Full-Stack Web Development with React and Node",
        duration="20 weeks",
        start_date="2025-02-01",
        description="Build modern full-stack applications with React, Node.js, Express, and MongoDB.",
        category="web",
        level="intermediate",
        instructor="Jennifer Adams",
        price=899.99,
        max_students=30,
        prerequisites=["HTML/CSS", "JavaScript basics"],
        skills_covered=["React", "Node.js", "Express", "MongoDB", "REST APIs", "Authentication"]
    ),
    Course(
        id="web_002",
        title="Frontend Development with Vue.js",
        duration="8 weeks",
        start_date="2025-02-20",
        description="Master Vue.js framework for building reactive and performant web applications.",
        category="web",
        level="intermediate",
        instructor="Chris Taylor",
        price=399.99,
        max_students=25,
        prerequisites=["JavaScript", "HTML/CSS"],
        skills_covered=["Vue 3", "Vuex", "Vue Router", "Composition API", "Testing"]
    ),
    
    # Mobile courses
    Course(
        id="mobile_001",
        title="iOS Development with Swift",
        duration="12 weeks",
        start_date="2025-02-10",
        description="Build native iOS applications with Swift and SwiftUI for iPhone and iPad.",
        category="mobile",
        level="intermediate",
        instructor="Daniel White",
        price=599.99,
        max_students=25,
        prerequisites=["Programming basics"],
        skills_covered=["Swift", "SwiftUI", "UIKit", "Core Data", "App Store deployment"]
    ),
    Course(
        id="mobile_002",
        title="React Native Cross-Platform Development",
        duration="10 weeks",
        start_date="2025-03-05",
        description="Build cross-platform mobile apps for iOS and Android with React Native.",
        category="mobile",
        level="intermediate",
        instructor="Sophie Brown",
        price=499.99,
        max_students=30,
        prerequisites=["React", "JavaScript"],
        skills_covered=["React Native", "Expo", "Navigation", "Native modules", "Publishing"]
    ),
    
    # Database courses
    Course(
        id="db_001",
        title="SQL and Database Design",
        duration="8 weeks",
        start_date="2025-02-01",
        description="Master SQL querying and relational database design principles.",
        category="database",
        level="beginner",
        instructor="Patricia Martinez",
        price=349.99,
        max_students=35,
        prerequisites=[],
        skills_covered=["SQL", "Database design", "Normalization", "Indexing", "Transactions"]
    ),
    Course(
        id="db_002",
        title="NoSQL Databases: MongoDB and Redis",
        duration="6 weeks",
        start_date="2025-02-25",
        description="Learn NoSQL database technologies with focus on MongoDB and Redis.",
        category="database",
        level="intermediate",
        instructor="Ryan Johnson",
        price=399.99,
        max_students=30,
        prerequisites=["Basic database concepts"],
        skills_covered=["MongoDB", "Redis", "Data modeling", "Caching strategies", "Scaling"]
    )
]


def search_courses_data(category: Optional[str] = None, level: Optional[str] = None) -> Dict[str, Any]:
    """
    Search for IT courses with optional filters.
    
    Args:
        category: Course category to filter by (programming, cloud, devops, data, security, web, mobile, database)
        level: Difficulty level (beginner, intermediate, advanced)
        
    Returns:
        Dictionary containing CoursesList data
    """
    
    filtered_courses = MOCK_COURSES.copy()
    
    # Filter by category if provided
    if category:
        # Support both single category and comma-separated categories
        categories = [cat.strip().lower() for cat in category.split(',')]
        filtered_courses = [
            course for course in filtered_courses 
            if course.category.lower() in categories
        ]
    
    # Filter by level if provided
    if level:
        filtered_courses = [
            course for course in filtered_courses 
            if course.level and course.level.lower() == level.lower()
        ]
    
    # Create CoursesList object
    courses_list = CoursesList(
        category=category,
        total_count=len(filtered_courses),
        courses=filtered_courses
    )
    
    # Convert to dictionary for JSON serialization
    return {
        "category": courses_list.category,
        "total_count": courses_list.total_count,
        "courses": [course_to_dict(course) for course in courses_list.courses] if courses_list.courses else []
    }


def get_course_details_data(course_id: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific course.
    
    Args:
        course_id: Unique identifier of the course
        
    Returns:
        Dictionary containing CourseDetails data or error
    """
    
    # Find the course
    course = next((c for c in MOCK_COURSES if c.id == course_id), None)
    
    if not course:
        return {"error": f"Course with ID '{course_id}' not found"}
    
    # Create CourseDetails with additional information
    course_details = CourseDetails(
        course=course,
        syllabus=generate_syllabus(course),
        learning_outcomes=generate_learning_outcomes(course),
        certification=f"Certificate of Completion for {course.title}",
        enrollment_count=random.randint(50, 200),
        rating=round(random.uniform(4.0, 5.0), 1),
        reviews_count=random.randint(20, 100)
    )
    
    # Convert to dictionary
    return {
        "course": course_to_dict(course_details.course),
        "syllabus": course_details.syllabus,
        "learning_outcomes": course_details.learning_outcomes,
        "certification": course_details.certification,
        "enrollment_count": course_details.enrollment_count,
        "rating": course_details.rating,
        "reviews_count": course_details.reviews_count
    }


def course_to_dict(course: Course) -> Dict[str, Any]:
    """Convert Course object to dictionary."""
    return {
        "id": course.id,
        "title": course.title,
        "duration": course.duration,
        "start_date": course.start_date,
        "description": course.description,
        "category": course.category,
        "level": course.level,
        "instructor": course.instructor,
        "price": course.price,
        "max_students": course.max_students,
        "prerequisites": course.prerequisites,
        "skills_covered": course.skills_covered
    }


def generate_syllabus(course: Course) -> List[str]:
    """Generate a sample syllabus based on course duration."""
    weeks = int(course.duration.split()[0]) if "week" in course.duration else 4
    syllabus = []
    
    for i in range(1, min(weeks + 1, 9)):
        if i == 1:
            syllabus.append(f"Week {i}: Introduction and Setup")
        elif i == weeks:
            syllabus.append(f"Week {i}: Final Project and Assessment")
        else:
            skill_index = (i - 2) % len(course.skills_covered) if course.skills_covered else 0
            if course.skills_covered and skill_index < len(course.skills_covered):
                syllabus.append(f"Week {i}: {course.skills_covered[skill_index]}")
            else:
                syllabus.append(f"Week {i}: Advanced Topics")
    
    return syllabus


def generate_learning_outcomes(course: Course) -> List[str]:
    """Generate learning outcomes based on course skills."""
    outcomes = [
        f"Understand the fundamentals of {course.category}",
        f"Apply best practices in real-world projects"
    ]
    
    if course.skills_covered:
        for skill in course.skills_covered[:3]:
            outcomes.append(f"Master {skill}")
    
    outcomes.append(f"Complete hands-on projects demonstrating proficiency")
    
    return outcomes


def format_courses_list(courses_data: Dict[str, Any]) -> str:
    """Format courses list for display."""
    if not courses_data.get("courses"):
        return "No courses found matching your criteria."
    
    formatted = f"Found {courses_data['total_count']} course(s)"
    if courses_data.get("category"):
        formatted += f" in category: {courses_data['category']}"
    formatted += "\n\n"
    
    for course in courses_data["courses"]:
        formatted += f"📚 {course['title']}\n"
        formatted += f"   ID: {course['id']}\n"
        formatted += f"   Category: {course['category'].title()}\n"
        formatted += f"   Level: {course.get('level', 'Not specified').title()}\n"
        formatted += f"   Duration: {course['duration']}\n"
        formatted += f"   Start Date: {course['start_date']}\n"
        formatted += f"   Instructor: {course.get('instructor', 'TBD')}\n"
        formatted += f"   Price: ${course.get('price', 0):.2f}\n"
        formatted += f"   Description: {course['description']}\n\n"
    
    return formatted


def get_available_categories() -> List[str]:
    """Return list of available course categories."""
    return ["programming", "cloud", "devops", "data", "security", "web", "mobile", "database"]


def get_course_summary_prompt(category: Optional[str] = None) -> str:
    """Generate a prompt for course recommendations."""
    if category:
        return f"""Please help me find the best {category} courses available. I'm looking for courses that:
1. Match my skill level (please ask about my experience)
2. Fit my schedule and timeline
3. Provide practical, hands-on experience
4. Offer good value for money

Can you search for {category} courses and provide recommendations based on my needs?"""
    else:
        return """Please help me choose the right IT course for my career goals. I'm interested in:
1. Understanding what courses are available
2. Finding courses that match my current skill level
3. Identifying which skills are most in-demand
4. Planning a learning path for career advancement

Can you show me the available course categories and help me explore options?"""