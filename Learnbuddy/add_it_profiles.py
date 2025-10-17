import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Learnbuddy.settings')
django.setup()

from home.models import ITProfile

# Clear existing profiles
ITProfile.objects.all().delete()

# Create IT profiles
profiles = [
    {
        'name': 'Software Developer',
        'description': 'Designs, builds, and maintains software applications and systems.',
        'skills_required': 'Programming languages (Python, Java, JavaScript), algorithms, data structures, version control, testing',
        'career_path': 'Junior Developer → Mid-level Developer → Senior Developer → Tech Lead → Software Architect',
        'average_salary': '$105,000',
        'job_outlook': 'Excellent growth with 22% increase expected over the next decade'
    },
    {
        'name': 'Data Scientist',
        'description': 'Analyzes and interprets complex data to help organizations make better decisions.',
        'skills_required': 'Statistics, machine learning, Python, R, SQL, data visualization, big data technologies',
        'career_path': 'Data Analyst → Junior Data Scientist → Senior Data Scientist → Lead Data Scientist → Chief Data Officer',
        'average_salary': '$120,000',
        'job_outlook': 'Very strong growth with 36% increase expected over the next decade'
    },
    {
        'name': 'Cybersecurity Analyst',
        'description': 'Protects computer systems and networks from information disclosure, theft, or damage.',
        'skills_required': 'Network security, ethical hacking, security tools, risk assessment, incident response',
        'career_path': 'Security Analyst → Security Consultant → Security Engineer → Security Architect → CISO',
        'average_salary': '$103,000',
        'job_outlook': 'Excellent growth with 33% increase expected over the next decade'
    },
    {
        'name': 'DevOps Engineer',
        'description': 'Combines software development and IT operations to shorten the development lifecycle.',
        'skills_required': 'CI/CD, cloud platforms, containerization, infrastructure as code, scripting',
        'career_path': 'System Administrator → DevOps Engineer → Senior DevOps Engineer → DevOps Architect → VP of Engineering',
        'average_salary': '$115,000',
        'job_outlook': 'Strong growth with 25% increase expected over the next decade'
    },
    {
        'name': 'UX/UI Designer',
        'description': 'Creates user-friendly interfaces and optimizes user experiences for software and websites.',
        'skills_required': 'User research, wireframing, prototyping, visual design, usability testing',
        'career_path': 'Junior Designer → UX/UI Designer → Senior Designer → Design Lead → Design Director',
        'average_salary': '$95,000',
        'job_outlook': 'Good growth with 13% increase expected over the next decade'
    },
    {
        'name': 'Cloud Architect',
        'description': 'Designs and oversees cloud computing strategies and infrastructure.',
        'skills_required': 'AWS/Azure/GCP, cloud security, networking, distributed systems',
        'career_path': 'Cloud Engineer → Cloud Administrator → Cloud Architect → Enterprise Architect → CTO',
        'average_salary': '$135,000',
        'job_outlook': 'Excellent growth with 15% increase expected over the next decade'
    },
    {
        'name': 'Machine Learning Engineer',
        'description': 'Builds and deploys machine learning models and AI systems.',
        'skills_required': 'Deep learning, NLP, computer vision, Python, TensorFlow/PyTorch',
        'career_path': 'ML Developer → ML Engineer → Senior ML Engineer → ML Architect → AI Research Scientist',
        'average_salary': '$130,000',
        'job_outlook': 'Very strong growth with 40% increase expected over the next decade'
    }
]

# Add profiles to database
for profile_data in profiles:
    ITProfile.objects.create(**profile_data)

print(f"Added {len(profiles)} IT profiles to the database.")