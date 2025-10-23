#!/usr/bin/env python
"""
Utility functions for managing hackathon images
Usage: python hackathon_utils.py
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Learnbuddy.settings')
django.setup()

from home.models import Hackathon

def list_hackathon_images():
    """List all available hackathon images"""
    print("=== Available Hackathon Images ===")
    
    images_dir = "static/images"
    if not os.path.exists(images_dir):
        print("❌ Static images directory not found!")
        return []
    
    hackathon_images = []
    for filename in os.listdir(images_dir):
        if filename.startswith('hackathon-') and filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            hackathon_images.append(f'images/{filename}')
    
    if hackathon_images:
        for img in sorted(hackathon_images):
            print(f"✅ {img}")
    else:
        print("❌ No hackathon images found!")
    
    return hackathon_images

def list_hackathon_data():
    """List all hackathons with their current images"""
    print("\n=== Hackathon Database Records ===")
    
    hackathons = Hackathon.objects.all().order_by('start_date')
    
    if not hackathons.exists():
        print("❌ No hackathons found in database!")
        return
    
    for hackathon in hackathons:
        status = "✅" if hackathon.image and hackathon.image.startswith('images/') else "⚠️"
        print(f"{status} {hackathon.title}")
        print(f"   Image: {hackathon.image or 'None'}")
        print(f"   Organizer: {hackathon.organizer}")
        print(f"   Date: {hackathon.start_date} to {hackathon.end_date}")
        print()

def check_image_accessibility():
    """Check if all hackathon images are accessible"""
    print("=== Image Accessibility Check ===")
    
    from django.test import Client
    client = Client()
    
    hackathons = Hackathon.objects.all()
    issues = []
    
    for hackathon in hackathons:
        if hackathon.image:
            # Check if file exists physically
            file_path = os.path.join('static', hackathon.image)
            if os.path.exists(file_path):
                print(f"✅ {hackathon.title}: {hackathon.image}")
            else:
                print(f"❌ {hackathon.title}: {hackathon.image} (FILE NOT FOUND)")
                issues.append(f"{hackathon.title} - missing file: {hackathon.image}")
        else:
            print(f"⚠️  {hackathon.title}: No image assigned")
            issues.append(f"{hackathon.title} - no image assigned")
    
    if issues:
        print(f"\n🔧 Found {len(issues)} issues:")
        for issue in issues:
            print(f"   - {issue}")
        print("\n💡 Run: python manage.py sync_hackathon_images")
    else:
        print("\n🎉 All hackathon images are properly configured!")

def get_image_suggestions():
    """Get suggestions for assigning images to hackathons"""
    print("\n=== Image Assignment Suggestions ===")
    
    available_images = list_hackathon_images()
    hackathons = Hackathon.objects.all()
    
    suggestions = {
        'ai': 'images/hackathon-ai.jpg',
        'artificial intelligence': 'images/hackathon-ai.jpg',
        'machine learning': 'images/hackathon-ai.jpg',
        'web': 'images/hackathon-web.jpg',
        'website': 'images/hackathon-web.jpg',
        'frontend': 'images/hackathon-web.jpg',
        'backend': 'images/hackathon-web.jpg',
        'cyber': 'images/hackathon-cyber.jpg',
        'security': 'images/hackathon-cyber.jpg',
        'mobile': 'images/hackathon-mobile.jpg',
        'app': 'images/hackathon-mobile.jpg',
        'android': 'images/hackathon-mobile.jpg',
        'ios': 'images/hackathon-mobile.jpg',
        'data': 'images/hackathon-data.jpg',
        'analytics': 'images/hackathon-data.jpg',
        'science': 'images/hackathon-data.jpg',
        'blockchain': 'images/hackathon-blockchain.jpg',
        'crypto': 'images/hackathon-blockchain.jpg',
        'decentralized': 'images/hackathon-blockchain.jpg'
    }
    
    print("💡 Suggested mappings based on hackathon titles:\n")
    for hackathon in hackathons:
        title_lower = hackathon.title.lower()
        suggested_image = None
        
        for keyword, image_path in suggestions.items():
            if keyword in title_lower and image_path in available_images:
                suggested_image = image_path
                break
        
        current = hackathon.image or "None"
        suggested = suggested_image or "No suggestion"
        
        if current != suggested:
            print(f"📝 {hackathon.title}")
            print(f"   Current: {current}")
            print(f"   Suggest: {suggested}")
            print()

def main():
    """Main function to run all checks"""
    print("🎯 Hackathon Image Management Utility\n")
    
    # List available images
    available_images = list_hackathon_images()
    
    # List database records  
    list_hackathon_data()
    
    # Check accessibility
    check_image_accessibility()
    
    # Get suggestions
    get_image_suggestions()
    
    print("\n" + "="*50)
    print("🛠️  Management Commands:")
    print("   python manage.py sync_hackathon_images           # Sync all images")
    print("   python manage.py sync_hackathon_images --dry-run # Preview changes")
    print("   python hackathon_utils.py                        # Run this utility")

if __name__ == '__main__':
    main()