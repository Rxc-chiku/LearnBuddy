#!/usr/bin/env python
import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Learnbuddy.settings')
django.setup()

from home.models import Hackathon

def update_hackathon_images():
    """Update hackathon images to use local static files"""
    
    # Map hackathon titles to local image files
    image_mapping = {
        'AI Innovation Challenge 2024': 'images/hackathon-ai.jpg',
        'Web Development Sprint': 'images/hackathon-web.jpg', 
        'Cybersecurity Hackathon': 'images/hackathon-cyber.jpg',
        'Mobile App Innovation': 'images/hackathon-mobile.jpg',
        'Data Science Challenge': 'images/hackathon-data.jpg',
        'Blockchain & Crypto Hackathon': 'images/hackathon-blockchain.jpg'
    }
    
    print("Updating hackathon images to use local files...")
    
    for hackathon in Hackathon.objects.all():
        if hackathon.title in image_mapping:
            old_image = hackathon.image
            hackathon.image = image_mapping[hackathon.title]
            hackathon.save()
            print(f"Updated {hackathon.title}: {old_image} -> {hackathon.image}")
        else:
            print(f"No mapping found for: {hackathon.title}")
    
    print("\nUpdated hackathon images successfully!")
    
    # Verify the updates
    print("\nCurrent hackathon images:")
    for hackathon in Hackathon.objects.all():
        print(f"- {hackathon.title}: {hackathon.image}")

if __name__ == '__main__':
    update_hackathon_images()