#!/usr/bin/env python
"""
Create theme-specific hackathon images with different colors and icons
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_hackathon_image(theme_name, gradient_colors, icon_text, output_path):
    """Create a themed hackathon image with gradient background and icon"""
    
    # Image dimensions
    width, height = 500, 300
    
    # Create image
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Create gradient background
    for i in range(height):
        # Calculate color interpolation
        ratio = i / height
        r = int(gradient_colors[0][0] * (1 - ratio) + gradient_colors[1][0] * ratio)
        g = int(gradient_colors[0][1] * (1 - ratio) + gradient_colors[1][1] * ratio)
        b = int(gradient_colors[0][2] * (1 - ratio) + gradient_colors[1][2] * ratio)
        
        # Draw gradient line
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    # Add pattern overlay (dots)
    for x in range(0, width, 30):
        for y in range(0, height, 30):
            draw.ellipse([x, y, x+4, y+4], fill=(255, 255, 255, 30))
    
    # Try to load a font, fallback to default if not available
    try:
        title_font = ImageFont.truetype("arial.ttf", 36)
        icon_font = ImageFont.truetype("arial.ttf", 60)
    except:
        title_font = ImageFont.load_default()
        icon_font = ImageFont.load_default()
    
    # Add title text (center)
    title_lines = theme_name.split(' ')
    if len(title_lines) > 2:
        title_text = f"{' '.join(title_lines[:2])}\n{' '.join(title_lines[2:])}"
    else:
        title_text = '\n'.join(title_lines)
    
    # Calculate text position for center alignment
    bbox = draw.textbbox((0, 0), title_text, font=title_font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    
    # Draw text with shadow
    draw.text((text_x + 2, text_y + 2), title_text, fill=(0, 0, 0, 128), font=title_font, align='center')
    draw.text((text_x, text_y), title_text, fill='white', font=title_font, align='center')
    
    # Add icon in top right
    icon_x = width - 80
    icon_y = 30
    draw.text((icon_x, icon_y), icon_text, fill=(255, 255, 255, 180), font=icon_font)
    
    # Save image
    img.save(output_path, 'JPEG', quality=90)
    print(f"Created: {output_path}")

def main():
    """Create all themed hackathon images"""
    
    static_images_dir = "static/images"
    
    # Ensure directory exists
    if not os.path.exists(static_images_dir):
        os.makedirs(static_images_dir)
    
    # Define themes with gradients and icons
    themes = [
        {
            'name': 'AI Innovation Challenge',
            'colors': [(102, 126, 234), (118, 75, 162)],  # Purple-blue gradient
            'icon': '🤖',
            'filename': 'hackathon-ai.jpg'
        },
        {
            'name': 'Web Development Sprint', 
            'colors': [(240, 147, 251), (245, 87, 108)],  # Pink gradient
            'icon': '💻',
            'filename': 'hackathon-web.jpg'
        },
        {
            'name': 'Cybersecurity Hackathon',
            'colors': [(79, 172, 254), (0, 242, 254)],  # Blue gradient
            'icon': '🔒',
            'filename': 'hackathon-cyber.jpg'
        },
        {
            'name': 'Mobile App Innovation',
            'colors': [(67, 233, 123), (56, 249, 215)],  # Green gradient
            'icon': '📱',
            'filename': 'hackathon-mobile.jpg'
        },
        {
            'name': 'Data Science Challenge',
            'colors': [(250, 112, 154), (254, 225, 64)],  # Pink-yellow gradient
            'icon': '📊',
            'filename': 'hackathon-data.jpg'
        },
        {
            'name': 'Blockchain Crypto Hackathon',
            'colors': [(168, 237, 234), (254, 214, 227)],  # Teal-pink gradient
            'icon': '⛓️',
            'filename': 'hackathon-blockchain.jpg'
        }
    ]
    
    # Create each themed image
    for theme in themes:
        output_path = os.path.join(static_images_dir, theme['filename'])
        create_hackathon_image(
            theme['name'],
            theme['colors'], 
            theme['icon'],
            output_path
        )
    
    print(f"\n✅ Created {len(themes)} unique hackathon theme images!")
    print("Each hackathon now has its own distinct visual identity.")

if __name__ == '__main__':
    main()