#!/usr/bin/env python
"""
Create relevant and detailed hackathon images with technology-specific visuals
"""

from PIL import Image, ImageDraw, ImageFont
import os
import math

def create_tech_pattern(draw, width, height, pattern_type):
    """Create technology-specific background patterns"""
    
    if pattern_type == "ai":
        # Neural network pattern
        for i in range(0, width, 40):
            for j in range(0, height, 40):
                # Draw nodes
                draw.ellipse([i-3, j-3, i+3, j+3], fill=(255, 255, 255, 40))
                # Draw connections
                if i < width - 40:
                    draw.line([i, j, i+40, j], fill=(255, 255, 255, 30), width=1)
                if j < height - 40:
                    draw.line([i, j, i, j+40], fill=(255, 255, 255, 30), width=1)
                if i < width - 40 and j < height - 40:
                    draw.line([i, j, i+40, j+40], fill=(255, 255, 255, 20), width=1)
    
    elif pattern_type == "web":
        # Code/HTML pattern
        for i in range(0, width, 60):
            for j in range(0, height, 30):
                draw.text([i, j], "</> ", fill=(255, 255, 255, 30))
    
    elif pattern_type == "cyber":
        # Binary/matrix pattern
        for i in range(0, width, 20):
            for j in range(0, height, 25):
                binary = "01" if (i + j) % 2 == 0 else "10"
                draw.text([i, j], binary, fill=(255, 255, 255, 40))
    
    elif pattern_type == "mobile":
        # Mobile grid pattern
        for i in range(0, width, 50):
            for j in range(0, height, 50):
                draw.rectangle([i, j, i+40, j+40], outline=(255, 255, 255, 50), width=1)
                draw.ellipse([i+15, j+15, i+25, j+25], fill=(255, 255, 255, 30))
    
    elif pattern_type == "data":
        # Chart/graph pattern
        for i in range(0, width, 80):
            for j in range(height//2, height, 40):
                bar_height = 20 + (i % 40)
                draw.rectangle([i, j-bar_height, i+15, j], fill=(255, 255, 255, 40))
    
    elif pattern_type == "blockchain":
        # Block chain pattern
        for i in range(0, width, 60):
            for j in range(0, height, 80):
                # Draw block
                draw.rectangle([i, j, i+40, j+30], outline=(255, 255, 255, 50), width=2)
                draw.rectangle([i+5, j+5, i+35, j+25], fill=(255, 255, 255, 20))
                # Draw chain link
                if i < width - 60:
                    draw.line([i+40, j+15, i+60, j+15], fill=(255, 255, 255, 60), width=3)

def create_relevant_hackathon_image(theme_name, gradient_colors, icons, tech_symbols, output_path, pattern_type):
    """Create a detailed hackathon image with relevant technology elements"""
    
    # Image dimensions
    width, height = 500, 300
    
    # Create image
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Create gradient background
    for i in range(height):
        ratio = i / height
        r = int(gradient_colors[0][0] * (1 - ratio) + gradient_colors[1][0] * ratio)
        g = int(gradient_colors[0][1] * (1 - ratio) + gradient_colors[1][1] * ratio)
        b = int(gradient_colors[0][2] * (1 - ratio) + gradient_colors[1][2] * ratio)
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    # Add tech-specific pattern
    create_tech_pattern(draw, width, height, pattern_type)
    
    # Try to load fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 32)
        subtitle_font = ImageFont.truetype("arial.ttf", 18)
        icon_font = ImageFont.truetype("arial.ttf", 48)
        tech_font = ImageFont.truetype("arial.ttf", 24)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        icon_font = ImageFont.load_default()
        tech_font = ImageFont.load_default()
    
    # Add main title
    title_lines = theme_name.split(' ')
    if len(title_lines) > 3:
        title_text = f"{' '.join(title_lines[:2])}\n{' '.join(title_lines[2:])}"
    else:
        title_text = '\n'.join(title_lines[:2]) + ('\n' + ' '.join(title_lines[2:]) if len(title_lines) > 2 else '')
    
    # Calculate text position
    bbox = draw.textbbox((0, 0), title_text, font=title_font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2 - 20
    
    # Draw title with shadow
    draw.text((text_x + 3, text_y + 3), title_text, fill=(0, 0, 0, 200), font=title_font, align='center')
    draw.text((text_x, text_y), title_text, fill='white', font=title_font, align='center')
    
    # Add main icon (top right)
    main_icon_x = width - 70
    main_icon_y = 20
    draw.text((main_icon_x, main_icon_y), icons[0], fill=(255, 255, 255, 220), font=icon_font)
    
    # Add technology symbols (bottom area)
    tech_y = height - 50
    tech_spacing = width // (len(tech_symbols) + 1)
    
    for i, symbol in enumerate(tech_symbols):
        tech_x = tech_spacing * (i + 1) - 15
        draw.text((tech_x, tech_y), symbol, fill=(255, 255, 255, 180), font=tech_font)
    
    # Add decorative elements
    # Top left corner accent
    draw.arc([10, 10, 50, 50], 0, 90, fill=(255, 255, 255, 100), width=3)
    
    # Bottom right corner accent
    draw.arc([width-50, height-50, width-10, height-10], 180, 270, fill=(255, 255, 255, 100), width=3)
    
    # Save image
    img.save(output_path, 'JPEG', quality=95)
    print(f"Created relevant image: {output_path}")

def main():
    """Create all relevant hackathon images"""
    
    static_images_dir = "static/images"
    
    if not os.path.exists(static_images_dir):
        os.makedirs(static_images_dir)
    
    # Define themes with more relevant details
    themes = [
        {
            'name': 'AI Innovation Challenge 2024',
            'colors': [(74, 144, 226), (80, 39, 116)],  # Deep blue to purple
            'icons': ['🤖'],
            'tech_symbols': ['🧠', '⚡', '🔮', '🎯'],
            'pattern': 'ai',
            'filename': 'hackathon-ai.jpg'
        },
        {
            'name': 'Web Development Sprint',
            'colors': [(255, 94, 77), (255, 154, 0)],  # Orange to red gradient
            'icons': ['💻'],
            'tech_symbols': ['⚛️', '🌐', '📱', '🎨'],
            'pattern': 'web',
            'filename': 'hackathon-web.jpg'
        },
        {
            'name': 'Cybersecurity Hackathon',
            'colors': [(13, 71, 161), (1, 87, 155)],  # Dark blue security theme
            'icons': ['🔒'],
            'tech_symbols': ['🛡️', '🔐', '⚠️', '🔍'],
            'pattern': 'cyber',
            'filename': 'hackathon-cyber.jpg'
        },
        {
            'name': 'Mobile App Innovation',
            'colors': [(76, 175, 80), (139, 195, 74)],  # Green mobile theme
            'icons': ['📱'],
            'tech_symbols': ['📲', '⚡', '🎮', '💫'],
            'pattern': 'mobile',
            'filename': 'hackathon-mobile.jpg'
        },
        {
            'name': 'Data Science Challenge',
            'colors': [(156, 39, 176), (233, 30, 99)],  # Purple to pink
            'icons': ['📊'],
            'tech_symbols': ['📈', '🧮', '🔬', '💡'],
            'pattern': 'data',
            'filename': 'hackathon-data.jpg'
        },
        {
            'name': 'Blockchain Crypto Hackathon',
            'colors': [(0, 150, 136), (76, 175, 80)],  # Teal to green
            'icons': ['⛓️'],
            'tech_symbols': ['₿', '💎', '🏦', '🔗'],
            'pattern': 'blockchain',
            'filename': 'hackathon-blockchain.jpg'
        }
    ]
    
    # Create each themed image
    for theme in themes:
        output_path = os.path.join(static_images_dir, theme['filename'])
        create_relevant_hackathon_image(
            theme['name'],
            theme['colors'], 
            theme['icons'],
            theme['tech_symbols'],
            output_path,
            theme['pattern']
        )
    
    print(f"\n🎨 Created {len(themes)} relevant hackathon images!")
    print("\n🚀 Each image now features:")
    print("   • Technology-specific background patterns")
    print("   • Relevant icons and symbols")
    print("   • Professional color schemes")
    print("   • Detailed visual elements")
    print("   • Industry-appropriate themes")

if __name__ == '__main__':
    main()