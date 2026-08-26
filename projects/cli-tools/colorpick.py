#!/usr/bin/env python3
"""generates random color palettes"""

import random
import argparse

def generate_hex():
    """generates a random hex color"""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def generate_palette(count=5, style="random"):
    """generates a palette of colors"""
    
    if style == "monochrome":
        # shades of gray
        base = random.randint(0, 255)
        colors = []
        for i in range(count):
            shade = max(0, min(255, base + (i - count//2) * 20))
            colors.append("#{:02x}{:02x}{:02x}".format(shade, shade, shade))
        return colors
    
    elif style == "pastel":
        # soft pastel colors
        colors = []
        for _ in range(count):
            r = random.randint(150, 255)
            g = random.randint(150, 255)
            b = random.randint(150, 255)
            colors.append("#{:02x}{:02x}{:02x}".format(r, g, b))
        return colors
    
    elif style == "neon":
        # bright neon colors
        colors = []
        for _ in range(count):
            # pick one dominant channel
            choice = random.choice(['r', 'g', 'b'])
            if choice == 'r':
                r, g, b = 255, random.randint(0, 100), random.randint(0, 100)
            elif choice == 'g':
                r, g, b = random.randint(0, 100), 255, random.randint(0, 100)
            else:
                r, g, b = random.randint(0, 100), random.randint(0, 100), 255
            colors.append("#{:02x}{:02x}{:02x}".format(r, g, b))
        return colors
    
    else:
        # completely random
        return [generate_hex() for _ in range(count)]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate color palettes")
    parser.add_argument("--count", "-c", type=int, default=5, 
                        help="number of colors to generate")
    parser.add_argument("--style", "-s", type=str, default="random",
                        choices=["random", "monochrome", "pastel", "neon"],
                        help="color style")
    
    args = parser.parse_args()
    
    palette = generate_palette(args.count, args.style)
    
    print(f"\nGenerated {args.count} {args.style} colors:\n")
    for color in palette:
        # print with ANSI color if terminal supports it
        print(f"  {color}")
    
    print()
