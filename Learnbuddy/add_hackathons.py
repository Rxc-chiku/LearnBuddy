#!/usr/bin/env python
import os
import django
from datetime import date, timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Learnbuddy.settings')
django.setup()

from home.models import Hackathon

def add_sample_hackathons():
    """Add sample hackathon data to the database"""
    
    # Clear existing hackathons
    Hackathon.objects.all().delete()
    print("Cleared existing hackathons...")
    
    # Sample hackathons data
    hackathons_data = [
        {
            'title': 'AI Innovation Challenge 2024',
            'description': 'Build innovative AI solutions to solve real-world problems. Open to teams of 2-4 members. Focus on machine learning, natural language processing, and computer vision.',
            'organizer': 'TechCorp',
            'start_date': date.today() + timedelta(days=15),
            'end_date': date.today() + timedelta(days=17),
            'registration_url': 'https://example.com/ai-challenge-register',
            'image': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=500&h=300&fit=crop'
        },
        {
            'title': 'Web Development Sprint',
            'description': 'Create amazing web applications using modern frameworks. Perfect for beginners and experts alike. Prizes for the most innovative and user-friendly designs.',
            'organizer': 'DevHub',
            'start_date': date.today() + timedelta(days=30),
            'end_date': date.today() + timedelta(days=32),
            'registration_url': 'https://example.com/web-dev-sprint-register',
            'image': 'https://images.unsplash.com/photo-1627398242454-45a1465c2479?w=500&h=300&fit=crop'
        },
        {
            'title': 'Cybersecurity Hackathon',
            'description': 'Protect the digital world! Build security tools, find vulnerabilities, and create defensive solutions. Network with cybersecurity professionals.',
            'organizer': 'SecureNet',
            'start_date': date.today() + timedelta(days=45),
            'end_date': date.today() + timedelta(days=47),
            'registration_url': 'https://example.com/cyber-security-register',
            'image': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=500&h=300&fit=crop'
        },
        {
            'title': 'Mobile App Innovation',
            'description': 'Design and develop mobile applications that change lives. iOS, Android, or cross-platform solutions welcome. Focus on user experience and functionality.',
            'organizer': 'AppMakers',
            'start_date': date.today() + timedelta(days=60),
            'end_date': date.today() + timedelta(days=62),
            'registration_url': 'https://example.com/mobile-app-register',
            'image': 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=500&h=300&fit=crop'
        },
        {
            'title': 'Data Science Challenge',
            'description': 'Unlock insights from complex datasets! Use statistical analysis, machine learning, and data visualization to solve business problems.',
            'organizer': 'DataViz Inc',
            'start_date': date.today() + timedelta(days=75),
            'end_date': date.today() + timedelta(days=77),
            'registration_url': 'https://example.com/data-science-register',
            'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500&h=300&fit=crop'
        },
        {
            'title': 'Blockchain & Crypto Hackathon',
            'description': 'Build the future of decentralized applications! Create smart contracts, DeFi solutions, or innovative blockchain applications.',
            'organizer': 'CryptoDevs',
            'start_date': date.today() + timedelta(days=90),
            'end_date': date.today() + timedelta(days=92),
            'registration_url': 'https://example.com/blockchain-register',
            'image': 'https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=500&h=300&fit=crop'
        }
    ]
    
    # Add hackathons to database
    for hackathon_data in hackathons_data:
        hackathon = Hackathon.objects.create(**hackathon_data)
        print(f"Created hackathon: {hackathon.title}")
    
    print(f"\nSuccessfully added {len(hackathons_data)} hackathons to the database!")
    print("Your hackathon page is now connected to the database!")

if __name__ == '__main__':
    add_sample_hackathons()