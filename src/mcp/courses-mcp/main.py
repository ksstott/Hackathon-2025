"""
IT Courses MCP Server - Search and discover IT training courses.

To run this server:
    uv run mcp dev main.py

Provides tools for searching IT courses by category and getting course details.
"""

from typing import Dict, Any, Optional
from mcp.server.fastmcp import FastMCP

from courses_service import (
    search_courses_data,
    get_course_details_data,
    format_courses_list,
    get_available_categories,
    get_course_summary_prompt
)

# Create an MCP server on port 8011 to avoid conflicts
mcp = FastMCP("IT Courses", port=8011)

# Tools
@mcp.tool()
def search_courses(category: Optional[str] = None, level: Optional[str] = None) -> Dict[str, Any]:
    """Search for IT training courses with optional filters
    
    Args:
        category: Course category to filter by. Available categories:
                  - programming (Python, Java, JavaScript, etc.)
                  - cloud (AWS, Azure, GCP)
                  - devops (Docker, Kubernetes, CI/CD)
                  - data (Data Science, Machine Learning)
                  - security (Cybersecurity, Ethical Hacking)
                  - web (Frontend, Backend, Full-stack)
                  - mobile (iOS, Android, React Native)
                  - database (SQL, NoSQL)
                  You can search multiple categories by separating with commas (e.g., "programming,web")
        level: Difficulty level - "beginner", "intermediate", or "advanced"
        
    Returns:
        CoursesList object as dictionary with matching courses
    """
    return search_courses_data(category, level)

@mcp.tool()
def get_course_details(course_id: str) -> Dict[str, Any]:
    """Get detailed information about a specific IT course
    
    Args:
        course_id: Unique identifier of the course (e.g., "prog_001", "cloud_002")
        
    Returns:
        CourseDetails object as dictionary with full course information,
        syllabus, learning outcomes, and enrollment details
    """
    return get_course_details_data(course_id)

@mcp.tool()
def search_and_format_courses(category: Optional[str] = None, level: Optional[str] = None) -> str:
    """Search for courses and return formatted results for easy reading
    
    Args:
        category: Course category to filter by (see search_courses for full list)
        level: Difficulty level - "beginner", "intermediate", or "advanced"
        
    Returns:
        Formatted string with course search results
    """
    courses_data = search_courses_data(category, level)
    return format_courses_list(courses_data)

@mcp.tool()
def get_course_categories() -> Dict[str, Any]:
    """Get list of all available course categories
    
    Returns:
        Dictionary with list of available categories and their descriptions
    """
    categories = get_available_categories()
    return {
        "categories": categories,
        "descriptions": {
            "programming": "Programming languages and software development",
            "cloud": "Cloud platforms (AWS, Azure, GCP)",
            "devops": "DevOps tools and practices",
            "data": "Data Science, ML, and Analytics",
            "security": "Cybersecurity and Information Security",
            "web": "Web development (Frontend, Backend, Full-stack)",
            "mobile": "Mobile app development",
            "database": "Database design and management"
        }
    }

# Resources
@mcp.resource("courses://category/{category}")
def get_courses_by_category_resource(category: str) -> str:
    """Get courses by category as a formatted resource"""
    courses_data = search_courses_data(category=category)
    return format_courses_list(courses_data)

@mcp.resource("courses://level/{level}")
def get_courses_by_level_resource(level: str) -> str:
    """Get courses by difficulty level as a formatted resource"""
    courses_data = search_courses_data(level=level)
    return format_courses_list(courses_data)

@mcp.resource("course://{course_id}")
def get_course_resource(course_id: str) -> str:
    """Get detailed course information as a formatted resource"""
    course_data = get_course_details_data(course_id)
    
    if "error" in course_data:
        return course_data["error"]
    
    course = course_data["course"]
    formatted = f"📚 {course['title']}\n"
    formatted += f"{'='*50}\n\n"
    formatted += f"Course ID: {course['id']}\n"
    formatted += f"Category: {course['category'].title()}\n"
    formatted += f"Level: {course.get('level', 'Not specified').title()}\n"
    formatted += f"Duration: {course['duration']}\n"
    formatted += f"Start Date: {course['start_date']}\n"
    formatted += f"Instructor: {course.get('instructor', 'TBD')}\n"
    formatted += f"Price: ${course.get('price', 0):.2f}\n"
    formatted += f"Max Students: {course.get('max_students', 'Unlimited')}\n\n"
    formatted += f"Description:\n{course['description']}\n\n"
    
    if course.get('prerequisites'):
        formatted += f"Prerequisites:\n"
        for prereq in course['prerequisites']:
            formatted += f"  • {prereq}\n"
        formatted += "\n"
    
    if course.get('skills_covered'):
        formatted += f"Skills Covered:\n"
        for skill in course['skills_covered']:
            formatted += f"  • {skill}\n"
        formatted += "\n"
    
    if course_data.get('syllabus'):
        formatted += f"Syllabus:\n"
        for week in course_data['syllabus']:
            formatted += f"  • {week}\n"
        formatted += "\n"
    
    if course_data.get('learning_outcomes'):
        formatted += f"Learning Outcomes:\n"
        for outcome in course_data['learning_outcomes']:
            formatted += f"  • {outcome}\n"
        formatted += "\n"
    
    formatted += f"📊 Course Stats:\n"
    formatted += f"  • Enrolled Students: {course_data.get('enrollment_count', 0)}\n"
    formatted += f"  • Rating: {course_data.get('rating', 0)}/5.0 ({course_data.get('reviews_count', 0)} reviews)\n"
    formatted += f"  • Certification: {course_data.get('certification', 'Certificate of Completion')}\n"
    
    return formatted

@mcp.resource("courses://all")
def get_all_courses_resource() -> str:
    """Get all available courses as a formatted resource"""
    courses_data = search_courses_data()
    return format_courses_list(courses_data)

# Prompts
@mcp.prompt()
def course_recommendation_prompt(category: Optional[str] = None) -> str:
    """Generate a prompt for course recommendations"""
    return get_course_summary_prompt(category)

@mcp.prompt()
def learning_path_prompt(target_role: str) -> str:
    """Generate a prompt for creating a learning path"""
    return f"""Please help me create a learning path to become a {target_role}. I need:
1. A sequence of courses to take in order
2. Estimated timeline for completing the path
3. Key skills I'll develop at each stage
4. Prerequisites I should have before starting
5. Career opportunities after completion

Search for relevant courses and create a structured learning plan that will prepare me for a {target_role} role."""

@mcp.prompt()
def course_comparison_prompt(course_ids: str) -> str:
    """Generate a prompt for comparing multiple courses"""
    return f"""Please compare these courses (IDs: {course_ids}) and help me decide which one to take. Consider:
1. Content depth and breadth
2. Difficulty level and prerequisites
3. Time commitment and schedule
4. Instructor expertise
5. Price and value for money
6. Skills gained and career relevance
7. Student reviews and ratings

Provide a detailed comparison and recommendation based on my goals."""

if __name__ == "__main__":
    mcp.run("streamable-http")