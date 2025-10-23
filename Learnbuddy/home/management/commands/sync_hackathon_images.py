from django.core.management.base import BaseCommand
from django.conf import settings
import os
from home.models import Hackathon

class Command(BaseCommand):
    help = 'Sync hackathon records with available images'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be updated without making changes',
        )
        parser.add_argument(
            '--create-missing',
            action='store_true', 
            help='Create sample hackathons if none exist',
        )
    
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=== Hackathon Image Sync ===\n'))
        
        # Get available images
        static_images_dir = os.path.join(settings.BASE_DIR, 'static', 'images')
        available_images = []
        
        if os.path.exists(static_images_dir):
            for filename in os.listdir(static_images_dir):
                if filename.startswith('hackathon-') and filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                    relative_path = f'images/{filename}'
                    available_images.append(relative_path)
        
        self.stdout.write(f'Found {len(available_images)} hackathon images:')
        for img in available_images:
            self.stdout.write(f'  - {img}')
        self.stdout.write('')
        
        # Get current hackathons
        hackathons = Hackathon.objects.all()
        
        if not hackathons.exists():
            if options['create_missing']:
                self.create_sample_hackathons(available_images, options['dry_run'])
            else:
                self.stdout.write(self.style.WARNING('No hackathons found. Use --create-missing to create sample data.'))
            return
        
        # Update existing hackathons
        self.stdout.write(f'Updating {hackathons.count()} existing hackathons...\n')
        
        # Smart mapping based on title keywords
        keyword_mapping = {
            'ai': 'images/hackathon-ai.jpg',
            'artificial intelligence': 'images/hackathon-ai.jpg',
            'web': 'images/hackathon-web.jpg',
            'website': 'images/hackathon-web.jpg',
            'cyber': 'images/hackathon-cyber.jpg',
            'security': 'images/hackathon-cyber.jpg',
            'mobile': 'images/hackathon-mobile.jpg',
            'app': 'images/hackathon-mobile.jpg',
            'data': 'images/hackathon-data.jpg',
            'analytics': 'images/hackathon-data.jpg',
            'blockchain': 'images/hackathon-blockchain.jpg',
            'crypto': 'images/hackathon-blockchain.jpg'
        }
        
        updated_count = 0
        for i, hackathon in enumerate(hackathons):
            # Find best matching image
            best_image = None
            title_lower = hackathon.title.lower()
            
            # First try keyword matching
            for keyword, image_path in keyword_mapping.items():
                if keyword in title_lower and image_path in available_images:
                    best_image = image_path
                    break
            
            # Fallback to cyclic assignment
            if not best_image and available_images:
                best_image = available_images[i % len(available_images)]
            
            if best_image:
                old_image = hackathon.image
                if old_image != best_image:
                    if not options['dry_run']:
                        hackathon.image = best_image
                        hackathon.save()
                    
                    self.stdout.write(f"{'[DRY RUN] ' if options['dry_run'] else ''}Updated '{hackathon.title}':")
                    self.stdout.write(f"  {old_image} → {best_image}")
                    updated_count += 1
                else:
                    self.stdout.write(f"✓ '{hackathon.title}' already has correct image: {best_image}")
        
        if updated_count > 0:
            self.stdout.write(f'\n{"[DRY RUN] Would update" if options["dry_run"] else "Updated"} {updated_count} hackathon(s)')
        else:
            self.stdout.write('\n✓ All hackathons already have correct images')
        
        self.stdout.write(self.style.SUCCESS('\n=== Sync Complete ==='))
    
    def create_sample_hackathons(self, available_images, dry_run=False):
        from datetime import date, timedelta
        
        sample_data = [
            {
                'title': 'AI Innovation Challenge 2024',
                'description': 'Build innovative AI solutions to solve real-world problems. Teams of 2-4 members welcome!',
                'organizer': 'TechCorp',
                'days_offset': 15,
                'duration': 3,
                'image': 'images/hackathon-ai.jpg'
            },
            {
                'title': 'Web Development Sprint',
                'description': 'Create amazing web applications using modern frameworks. Perfect for all skill levels.',
                'organizer': 'DevHub',
                'days_offset': 30,
                'duration': 2,
                'image': 'images/hackathon-web.jpg'
            },
            {
                'title': 'Cybersecurity Hackathon',
                'description': 'Protect the digital world! Build security tools and defensive solutions.',
                'organizer': 'SecureNet',
                'days_offset': 45,
                'duration': 3,
                'image': 'images/hackathon-cyber.jpg'
            },
            {
                'title': 'Mobile App Innovation',
                'description': 'Design and develop mobile applications that change lives. iOS, Android, or cross-platform.',
                'organizer': 'AppMakers',
                'days_offset': 60,
                'duration': 3,
                'image': 'images/hackathon-mobile.jpg'
            },
            {
                'title': 'Data Science Challenge',
                'description': 'Unlock insights from complex datasets using ML and data visualization.',
                'organizer': 'DataViz Inc',
                'days_offset': 75,
                'duration': 2,
                'image': 'images/hackathon-data.jpg'
            },
            {
                'title': 'Blockchain & Crypto Hackathon',
                'description': 'Build the future of decentralized applications and smart contracts.',
                'organizer': 'CryptoDevs',
                'days_offset': 90,
                'duration': 3,
                'image': 'images/hackathon-blockchain.jpg'
            }
        ]
        
        if not dry_run:
            # Clear existing data
            Hackathon.objects.all().delete()
        
        created_count = 0
        for data in sample_data:
            # Only use images that actually exist
            if data['image'] in available_images or not available_images:
                if not available_images:
                    data['image'] = None  # No images available
                
                hackathon_data = {
                    'title': data['title'],
                    'description': data['description'],
                    'organizer': data['organizer'],
                    'start_date': date.today() + timedelta(days=data['days_offset']),
                    'end_date': date.today() + timedelta(days=data['days_offset'] + data['duration']),
                    'registration_url': f'https://example.com/{data["title"].lower().replace(" ", "-")}-register',
                    'image': data['image']
                }
                
                if not dry_run:
                    hackathon = Hackathon.objects.create(**hackathon_data)
                    self.stdout.write(f"Created: {hackathon.title} → {hackathon.image}")
                else:
                    self.stdout.write(f"[DRY RUN] Would create: {data['title']} → {data['image']}")
                
                created_count += 1
        
        self.stdout.write(f'\n{"[DRY RUN] Would create" if dry_run else "Created"} {created_count} sample hackathons')