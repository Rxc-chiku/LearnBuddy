import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Learnbuddy.settings')
django.setup()

from home.models import CSKnowledgeArea, CSLearningPath, PathAreaRelationship, Hackathon

def add_knowledge_areas():
    areas = [
        {
            'name': 'Programming Fundamentals',
            'description': 'Basic programming concepts including variables, data types, control structures, and functions.'
        },
        {
            'name': 'Data Structures',
            'description': 'Study of arrays, linked lists, stacks, queues, trees, graphs, and hash tables.'
        },
        {
            'name': 'Algorithms',
            'description': 'Study of algorithm design, analysis, and common algorithms for searching, sorting, and graph traversal.'
        },
        {
            'name': 'Object-Oriented Programming',
            'description': 'Concepts of classes, objects, inheritance, polymorphism, encapsulation, and abstraction.'
        },
        {
            'name': 'Web Development',
            'description': 'Technologies and frameworks for building web applications, including HTML, CSS, JavaScript, and backend technologies.'
        }
    ]
    
    for area in areas:
        CSKnowledgeArea.objects.get_or_create(name=area['name'], description=area['description'])
    
    print('Knowledge areas added successfully!')

def add_learning_paths():
    paths = [
        {
            'title': 'Computer Science Fundamentals',
            'description': 'A comprehensive path covering the essential concepts in computer science for beginners.',
            'difficulty_level': 'beginner'
        },
        {
            'title': 'Web Development Track',
            'description': 'Learn to build modern web applications from frontend to backend.',
            'difficulty_level': 'intermediate'
        },
        {
            'title': 'Data Structures and Algorithms',
            'description': 'Master the core data structures and algorithms needed for technical interviews and efficient programming.',
            'difficulty_level': 'intermediate'
        }
    ]
    
    for path in paths:
        CSLearningPath.objects.get_or_create(
            title=path['title'],
            description=path['description'],
            difficulty_level=path['difficulty_level']
        )
    
    print('Learning paths added successfully!')

def add_path_area_relationships():
    # CS Fundamentals Path
    cs_path = CSLearningPath.objects.get(title='Computer Science Fundamentals')
    
    relationships = [
        {'path': cs_path, 'area': CSKnowledgeArea.objects.get(name='Programming Fundamentals'), 'order': 1},
        {'path': cs_path, 'area': CSKnowledgeArea.objects.get(name='Object-Oriented Programming'), 'order': 2},
        {'path': cs_path, 'area': CSKnowledgeArea.objects.get(name='Data Structures'), 'order': 3}
    ]
    
    # Web Dev Path
    web_path = CSLearningPath.objects.get(title='Web Development Track')
    relationships.extend([
        {'path': web_path, 'area': CSKnowledgeArea.objects.get(name='Programming Fundamentals'), 'order': 1},
        {'path': web_path, 'area': CSKnowledgeArea.objects.get(name='Web Development'), 'order': 2}
    ])
    
    # DSA Path
    dsa_path = CSLearningPath.objects.get(title='Data Structures and Algorithms')
    relationships.extend([
        {'path': dsa_path, 'area': CSKnowledgeArea.objects.get(name='Data Structures'), 'order': 1},
        {'path': dsa_path, 'area': CSKnowledgeArea.objects.get(name='Algorithms'), 'order': 2}
    ])
    
    for rel in relationships:
        PathAreaRelationship.objects.get_or_create(
            path=rel['path'],
            area=rel['area'],
            order=rel['order']
        )
    
    print('Path-area relationships added successfully!')

def add_hackathons():
    today = datetime.date.today()
    
    hackathons = [
        {
            'title': 'CodeFest 2025',
            'description': 'A 48-hour hackathon focused on building innovative solutions for education technology.',
            'organizer': 'TechEdu Foundation',
            'start_date': today + datetime.timedelta(days=15),
            'end_date': today + datetime.timedelta(days=17),
            'registration_url': 'https://example.com/codefest2025'
        },
        {
            'title': 'AI Hack Challenge',
            'description': 'Develop AI-powered applications that solve real-world problems in healthcare, education, or sustainability.',
            'organizer': 'AI Research Institute',
            'start_date': today + datetime.timedelta(days=30),
            'end_date': today + datetime.timedelta(days=31),
            'registration_url': 'https://example.com/aihack'
        },
        {
            'title': 'Student Developer Summit',
            'description': 'A hackathon specifically for students to showcase their skills and connect with industry professionals.',
            'organizer': 'Campus Tech Alliance',
            'start_date': today + datetime.timedelta(days=45),
            'end_date': today + datetime.timedelta(days=46),
            'registration_url': 'https://example.com/studentsummit'
        }
    ]
    
    for hackathon in hackathons:
        Hackathon.objects.get_or_create(
            title=hackathon['title'],
            description=hackathon['description'],
            organizer=hackathon['organizer'],
            start_date=hackathon['start_date'],
            end_date=hackathon['end_date'],
            registration_url=hackathon['registration_url']
        )
    
    print('Hackathons added successfully!')

if __name__ == '__main__':
    print('Adding initial data to the database...')
    add_knowledge_areas()
    add_learning_paths()
    add_path_area_relationships()
    add_hackathons()
    print('Initial data added successfully!')