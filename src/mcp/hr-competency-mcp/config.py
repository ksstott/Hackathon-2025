# Mock data
MOCK_COMPETENCIES = [
{
    "id": 1,
    "name": "Python Programming",
    "description": "Ability to write clean, efficient, and maintainable Python code.",
    "category": "programming",
    "level": "advanced",
    "required_skills": ["Python", "OOP", "Debugging", "Unit Testing"],
    "required_experience": ["3+ years of software development", "Experience with APIs"],
    "required_education": ["Bachelor's in Computer Science"],
    "required_certifications": ["PCEP", "PCAP"],
    "required_licenses": [],
    "required_other": ["Portfolio of projects"]
  },
  {
    "id": 2,
    "name": "Project Management",
    "description": "Managing projects using Agile methodologies.",
    "category": "database",
    "level": "intermediate",
    "required_skills": ["Agile", "Scrum", "Kanban", "Leadership"],
    "required_experience": ["2+ years leading teams", "Managed cross-functional projects"],
    "required_education": ["Bachelor's in Business or related field"],
    "required_certifications": ["PMP", "Scrum Master"],
    "required_licenses": [],
    "required_other": []
  },
  {
    "id": 3,
    "name": "Data Analysis",
    "description": "Ability to analyze datasets and extract meaningful insights.",
    "category": "data",
    "level": "intermediate",
    "required_skills": ["SQL", "Excel", "Data Visualization", "Statistics"],
    "required_experience": ["2+ years analyzing business data"],
    "required_education": ["Bachelor’s in Statistics, Mathematics, or similar"],
    "required_certifications": ["Google Data Analytics"],
    "required_licenses": [],
    "required_other": ["Case study presentation"]
  },
  {
    "id": 4,
    "name": "Cloud Computing",
    "description": "Deploying and managing applications in cloud environments.",
    "category": "cloud",
    "level": "advanced",
    "required_skills": ["AWS", "Azure", "Docker", "Kubernetes"],
    "required_experience": ["2+ years working with cloud platforms"],
    "required_education": ["Bachelor's in IT or related field"],
    "required_certifications": ["AWS Certified Solutions Architect"],
    "required_licenses": [],
    "required_other": []
  },
  {
    "id": 5,
    "name": "Cybersecurity",
    "description": "Protecting systems and networks from digital attacks.",
    "category": "security",
    "level": "advanced",
    "required_skills": ["Network Security", "Firewalls", "Encryption", "Penetration Testing"],
    "required_experience": ["3+ years in cybersecurity roles"],
    "required_education": ["Bachelor's in Cybersecurity or related field"],
    "required_certifications": ["CISSP", "CEH"],
    "required_licenses": [],
    "required_other": []
  },
  {
    "id": 6,
    "name": "UI/UX Design",
    "description": "Designing intuitive and engaging user interfaces.",
    "category": "web",
    "level": "intermediate",
    "required_skills": ["Figma", "Sketch", "Prototyping", "Wireframing"],
    "required_experience": ["2+ years as a designer"],
    "required_education": ["Bachelor's in Design or related field"],
    "required_certifications": [],
    "required_licenses": [],
    "required_other": ["Portfolio of design work"]
  },
  {
    "id": 7,
    "name": "Machine Learning",
    "description": "Developing predictive models using machine learning algorithms.",
    "category": "data",
    "level": "advanced",
    "required_skills": ["Python", "TensorFlow", "Scikit-learn", "Model Deployment"],
    "required_experience": ["2+ years in ML projects"],
    "required_education": ["Master’s in Data Science or related field"],
    "required_certifications": ["TensorFlow Developer Certificate"],
    "required_licenses": [],
    "required_other": []
  },
  {
    "id": 8,
    "name": "Technical Writing",
    "description": "Creating clear documentation for products and processes.",
    "category": "web",
    "level": "intermediate",
    "required_skills": ["Writing", "Editing", "Documentation Tools"],
    "required_experience": ["1+ years writing technical content"],
    "required_education": ["Bachelor’s in English, Communication, or related"],
    "required_certifications": [],
    "required_licenses": [],
    "required_other": []
  },
  {
    "id": 9,
    "name": "DevOps",
    "description": "Bridging development and operations for continuous delivery.",
    "category": "devops",
    "level": "advanced",
    "required_skills": ["CI/CD", "Jenkins", "Docker", "Kubernetes"],
    "required_experience": ["2+ years in DevOps roles"],
    "required_education": ["Bachelor's in IT or related field"],
    "required_certifications": ["Docker Certified Associate"],
    "required_licenses": [],
    "required_other": []
  },
  {
    "id": 10,
    "name": "Business Analysis",
    "description": "Analyzing business needs and defining solutions.",
    "category": "database",
    "level": "intermediate",
    "required_skills": ["Requirement Gathering", "Process Modeling", "Stakeholder Communication"],
    "required_experience": ["2+ years in business analysis roles"],
    "required_education": ["Bachelor's in Business or IT"],
    "required_certifications": ["CBAP"],
    "required_licenses": [],
    "required_other": []
  }
]

# Mock Employee Data
MOCK_EMPLOYEES = [
    {
    "id": 101,
    "name": "Alice Johnson",
    "email": "alice.johnson@example.com",
    "phone": "+1-202-555-0123",
    "department": "Software Engineering",
    "position": "Senior Developer",
    "competencies": [1, 3, 9]
  },
  {
    "id": 102,
    "name": "Bob Smith",
    "email": "bob.smith@example.com",
    "phone": "+1-202-555-0456",
    "department": "Project Management",
    "position": "Project Manager",
    "competencies": [2, 10]
  },
  {
    "id": 103,
    "name": "Clara Martinez",
    "email": "clara.martinez@example.com",
    "phone": "+1-202-555-0789",
    "department": "Data Science",
    "position": "Data Analyst",
    "competencies": [3, 7]
  },
  {
    "id": 104,
    "name": "David Lee",
    "email": "david.lee@example.com",
    "phone": "+1-202-555-0114",
    "department": "IT Security",
    "position": "Security Engineer",
    "competencies": [5, 4]
  },
  {
    "id": 105,
    "name": "Emma Wilson",
    "email": "emma.wilson@example.com",
    "phone": "+1-202-555-0168",
    "department": "Design",
    "position": "UI/UX Designer",
    "competencies": [6, 8]
  },
  {
    "id": 106,
    "name": "Frank Adams",
    "email": "frank.adams@example.com",
    "phone": "+1-202-555-0200",
    "department": "Cloud Engineering",
    "position": "Cloud Architect",
    "competencies": [4, 9]
  },
  {
    "id": 107,
    "name": "Grace Chen",
    "email": "grace.chen@example.com",
    "phone": "+1-202-555-0255",
    "department": "Data Science",
    "position": "ML Engineer",
    "competencies": [7, 1]
  },
  {
    "id": 108,
    "name": "Henry Thompson",
    "email": "henry.thompson@example.com",
    "phone": "+1-202-555-0301",
    "department": "Business Analysis",
    "position": "Business Analyst",
    "competencies": [10, 2, 8]
  },
  {
    "id": 109,
    "name": "Isabella Rivera",
    "email": "isabella.rivera@example.com",
    "phone": "+1-202-555-0344",
    "department": "Software Engineering",
    "position": "DevOps Engineer",
    "competencies": [9, 1, 4]
  },
  {
    "id": 110,
    "name": "Jack Patel",
    "email": "jack.patel@example.com",
    "phone": "+1-202-555-0400",
    "department": "Technical Writing",
    "position": "Technical Writer",
    "competencies": [8, 6]
  }
]