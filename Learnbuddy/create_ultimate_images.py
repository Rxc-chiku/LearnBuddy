#!/usr/bin/env python
"""
Create ultimate hackathon images with maximum relevant technology details
"""

from PIL import Image, ImageDraw, ImageFont
import os
import random

def create_advanced_tech_pattern(draw, width, height, pattern_type):
    """Create advanced technology-specific patterns with more detail"""
    
    if pattern_type == "ai":
        # Neural network with nodes and connections
        nodes = []
        for i in range(0, width, 60):
            for j in range(0, height, 50):
                nodes.append((i + random.randint(-10, 10), j + random.randint(-10, 10)))
                draw.ellipse([i-4, j-4, i+4, j+4], fill=(255, 255, 255, 60))
        
        # Connect nearby nodes
        for i, node1 in enumerate(nodes):
            for j, node2 in enumerate(nodes):
                if i != j:
                    distance = ((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2)**0.5
                    if distance < 80:
                        draw.line([node1, node2], fill=(255, 255, 255, 25), width=1)
    
    elif pattern_type == "web":
        # HTML/CSS code structure
        for i in range(0, width, 80):
            for j in range(0, height, 40):
                code_snippets = ["<div>", "</div>", "{ }", "( )", "[ ]", "//", "/**/"]
                snippet = random.choice(code_snippets)
                draw.text([i, j], snippet, fill=(255, 255, 255, 50))
    
    elif pattern_type == "cyber":
        # Matrix-style binary rain
        for i in range(0, width, 25):
            rain_length = random.randint(3, 8)
            start_j = random.randint(0, height//2)
            for k in range(rain_length):
                j = start_j + k * 20
                if j < height:
                    bit = random.choice(["0", "1"])
                    opacity = max(20, 80 - k*15)
                    draw.text([i, j], bit, fill=(255, 255, 255, opacity))
    
    elif pattern_type == "mobile":
        # Mobile interface elements
        for i in range(0, width, 80):
            for j in range(0, height, 60):
                # Draw mobile UI elements
                draw.rectangle([i, j, i+60, j+40], outline=(255, 255, 255, 40), width=1)
                draw.rectangle([i+10, j+5, i+50, j+15], fill=(255, 255, 255, 30))
                draw.ellipse([i+45, j+20, i+55, j+30], fill=(255, 255, 255, 40))
    
    elif pattern_type == "data":
        # Data visualization elements
        for i in range(0, width, 100):
            # Create bar charts
            for k in range(4):
                bar_x = i + k*20
                bar_height = random.randint(20, 80)
                draw.rectangle([bar_x, height-bar_height-50, bar_x+15, height-50], fill=(255, 255, 255, 50))
            
            # Add line chart points
            for j in range(0, height-100, 20):
                draw.ellipse([i+70, j+20, i+75, j+25], fill=(255, 255, 255, 60))
    
    elif pattern_type == "blockchain":
        # Blockchain structure with connected blocks
        block_size = 50
        for i in range(0, width, block_size + 30):
            for j in range(0, height, 90):
                # Draw block
                draw.rectangle([i, j, i+block_size, j+30], outline=(255, 255, 255, 70), width=2)
                draw.rectangle([i+5, j+5, i+45, j+25], fill=(255, 255, 255, 30))
                
                # Add hash representation
                for h in range(3):
                    draw.line([i+10+h*10, j+10, i+15+h*10, j+10], fill=(255, 255, 255, 80), width=2)
                
                # Connect to next block
                if i < width - block_size - 30:
                    draw.line([i+block_size, j+15, i+block_size+30, j+15], fill=(255, 255, 255, 90), width=3)
                    # Add arrow
                    draw.polygon([i+block_size+25, j+12, i+block_size+30, j+15, i+block_size+25, j+18], fill=(255, 255, 255, 90))

def create_ultimate_hackathon_image(theme_data):
    """Create the ultimate hackathon image with all relevant details"""
    
    width, height = 500, 300
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Enhanced gradient with multiple color stops
    colors = theme_data['colors']
    for i in range(height):
        ratio = i / height
        # Add some curve to the gradient
        curved_ratio = ratio * ratio * (3 - 2 * ratio)  # Smooth curve
        
        r = int(colors[0][0] * (1 - curved_ratio) + colors[1][0] * curved_ratio)
        g = int(colors[0][1] * (1 - curved_ratio) + colors[1][1] * curved_ratio)
        b = int(colors[0][2] * (1 - curved_ratio) + colors[1][2] * curved_ratio)
        
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    # Add advanced tech pattern
    create_advanced_tech_pattern(draw, width, height, theme_data['pattern'])
    
    # Load fonts
    try:
        title_font = ImageFont.truetype("arial.ttf", 28)
        subtitle_font = ImageFont.truetype("arial.ttf", 16)
        icon_font = ImageFont.truetype("arial.ttf", 44)
        tech_font = ImageFont.truetype("arial.ttf", 20)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        icon_font = ImageFont.load_default()
        tech_font = ImageFont.load_default()
    
    # Add semi-transparent overlay for text readability
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rectangle([0, height//2-40, width, height//2+60], fill=(0, 0, 0, 80))
    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(img)
    
    # Title with better positioning
    title = theme_data['name']
    words = title.split()
    
    if len(words) > 2:
        line1 = ' '.join(words[:2])
        line2 = ' '.join(words[2:])
        title_text = f"{line1}\n{line2}"
    else:
        title_text = '\n'.join(words)
    
    # Center the text
    bbox = draw.textbbox((0, 0), title_text, font=title_font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (width - text_width) // 2
    text_y = height // 2 - text_height // 2
    
    # Text with glow effect
    for offset in [(2, 2), (1, 1), (0, 0)]:
        color = (0, 0, 0, 200) if offset != (0, 0) else (255, 255, 255, 255)
        draw.text((text_x + offset[0], text_y + offset[1]), title_text, fill=color, font=title_font, align='center')
    
    # Main technology icon (top right with glow)
    main_icon = theme_data['icons'][0]
    icon_x, icon_y = width - 80, 25
    
    # Icon glow
    for glow in range(3, 0, -1):
        glow_opacity = 40 * glow
        draw.text((icon_x + glow, icon_y + glow), main_icon, fill=(255, 255, 255, glow_opacity), font=icon_font)
    draw.text((icon_x, icon_y), main_icon, fill=(255, 255, 255, 255), font=icon_font)
    
    # Technology symbols at bottom with labels
    tech_symbols = theme_data['tech_symbols']
    symbol_y = height - 40
    symbol_spacing = width // (len(tech_symbols) + 1)
    
    for i, symbol in enumerate(tech_symbols):
        symbol_x = symbol_spacing * (i + 1) - 15
        draw.text((symbol_x, symbol_y), symbol, fill=(255, 255, 255, 200), font=tech_font)
    
    # Add corner decorations
    corner_color = (255, 255, 255, 120)
    
    # Top left
    draw.arc([15, 15, 45, 45], 0, 90, fill=corner_color, width=4)
    draw.line([30, 15, 30, 20], fill=corner_color, width=2)
    draw.line([15, 30, 20, 30], fill=corner_color, width=2)
    
    # Bottom right
    draw.arc([width-45, height-45, width-15, height-15], 180, 270, fill=corner_color, width=4)
    draw.line([width-30, height-15, width-30, height-20], fill=corner_color, width=2)
    draw.line([width-15, height-30, width-20, height-30], fill=corner_color, width=2)
    
    # Add theme-specific extra elements
    if theme_data['pattern'] == 'ai':
        # Add brain-like connection in bottom left
        draw.arc([20, height-60, 60, height-20], 0, 180, fill=(255, 255, 255, 80), width=3)
    elif theme_data['pattern'] == 'web':
        # Add code brackets
        draw.text((20, height-60), "{ }", fill=(255, 255, 255, 100), font=tech_font)
    elif theme_data['pattern'] == 'cyber':
        # Add lock symbol
        draw.rectangle([20, height-50, 35, height-35], outline=(255, 255, 255, 100), width=2)
    
    # Save with high quality
    output_path = os.path.join("static/images", theme_data['filename'])
    img.save(output_path, 'JPEG', quality=98, optimize=True)
    print(f"✨ Created ultimate image: {theme_data['filename']}")

def main():
    """Create all ultimate hackathon images"""
    
    static_images_dir = "static/images"
    if not os.path.exists(static_images_dir):
        os.makedirs(static_images_dir)
    
    # Ultimate theme definitions with professional color schemes
    themes = [
        {
            'name': 'AI Innovation Challenge 2024',
            'colors': [(45, 52, 149), (106, 17, 203)],  # Deep indigo to purple
            'icons': ['🤖'],
            'tech_symbols': ['🧠', '⚡', '🔮', '🎯', '🚀'],
            'pattern': 'ai',
            'filename': 'hackathon-ai.jpg'
        },
        {
            'name': 'Web Development Sprint',
            'colors': [(239, 71, 111), (255, 209, 102)],  # Vibrant pink to yellow
            'icons': ['💻'],
            'tech_symbols': ['⚛️', '🌐', '📱', '🎨', '⚡'],
            'pattern': 'web',
            'filename': 'hackathon-web.jpg'
        },
        {
            'name': 'Cybersecurity Hackathon',
            'colors': [(17, 82, 147), (56, 163, 165)],  # Navy to teal
            'icons': ['🔒'],
            'tech_symbols': ['🛡️', '🔐', '⚠️', '🔍', '🛠️'],
            'pattern': 'cyber',
            'filename': 'hackathon-cyber.jpg'
        },
        {
            'name': 'Mobile App Innovation',
            'colors': [(34, 139, 34), (144, 238, 144)],  # Forest to light green
            'icons': ['📱'],
            'tech_symbols': ['📲', '⚡', '🎮', '💫', '🔄'],
            'pattern': 'mobile',
            'filename': 'hackathon-mobile.jpg'
        },
        {
            'name': 'Data Science Challenge',
            'colors': [(138, 43, 226), (255, 20, 147)],  # Blue violet to deep pink
            'icons': ['📊'],
            'tech_symbols': ['📈', '🧮', '🔬', '💡', '📉'],
            'pattern': 'data',
            'filename': 'hackathon-data.jpg'
        },
        {
            'name': 'Blockchain Crypto Hackathon',
            'colors': [(0, 128, 128), (64, 224, 208)],  # Teal to turquoise
            'icons': ['⛓️'],
            'tech_symbols': ['₿', '💎', '🏦', '🔗', '🔐'],
            'pattern': 'blockchain',
            'filename': 'hackathon-blockchain.jpg'
        }
    ]
    
    print("🚀 Creating ultimate hackathon images with maximum relevance...")
    
    for theme in themes:
        create_ultimate_hackathon_image(theme)
    
    print(f"\n🎨 ✅ Created {len(themes)} ULTIMATE hackathon images!")
    print("\n🌟 Each image now features:")
    print("   • 🎨 Advanced gradient backgrounds with curves")
    print("   • 🔧 Technology-specific detailed patterns") 
    print("   • 💫 Glowing icons and text effects")
    print("   • 🎯 Multiple relevant tech symbols")
    print("   • 💎 Professional corner decorations")
    print("   • 🌈 Industry-appropriate color schemes")
    print("   • ⚡ High-quality optimized images")
    print("\n🎯 Your hackathon cards now have MAXIMUM visual impact!")

if __name__ == '__main__':
    main()