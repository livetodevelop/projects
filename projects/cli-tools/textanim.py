#!/usr/bin/env python3
"""terminal text animation thing"""

import sys
import time

def type_writer(text, delay=0.05):
    """types out text like a typewriter"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def wave(text, repeats=3):
    """makes text wave up and down"""
    offsets = [0, 1, 2, 1, 0, -1, -2, -1]
    
    for _ in range(repeats):
        for offset in offsets:
            print(' ' * offset + text)
            time.sleep(0.1)
            # clear line (works on most terminals)
            print('\033[A\033[2K', end='')

def glitch(text, iterations=20):
    """adds random glitch characters"""
    import random
    glitches = ['`', '~', '^', '_', '.', '*', '#']
    
    for _ in range(iterations):
        glitched = ''.join(
            random.choice(glitches) if random.random() < 0.3 else c
            for c in text
        )
        print(glitched)
        time.sleep(0.05)
        print('\033[A\033[2K', end='')
    
    print(text)

def matrix_rain(duration=5):
    """simulates matrix rain effect"""
    import random
    
    chars = "abcdefghijklmnopqrstuvwxyz0123456789@#$%^&*"
    columns = 40  # assuming 80 char terminal width
    
    start_time = time.time()
    drops = [random.randint(0, 20) for _ in range(columns)]
    
    try:
        while time.time() - start_time < duration:
            line = ""
            for i in range(columns):
                if drops[i] == 0:
                    line += random.choice(chars)
                    drops[i] = random.randint(5, 15)
                else:
                    line += " "
                    drops[i] -= 1
            print(line)
            time.sleep(0.1)
            print('\033[A' * columns, end='')
    except KeyboardInterrupt:
        pass
    
    print('\n' * columns)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python textanim.py \"your text\" [animation_type]")
        print("animations: typewriter, wave, glitch, matrix")
        sys.exit(1)
    
    text = sys.argv[1]
    anim_type = sys.argv[2] if len(sys.argv) > 2 else "typewriter"
    
    if anim_type == "typewriter":
        type_writer(text)
    elif anim_type == "wave":
        wave(text)
    elif anim_type == "glitch":
        glitch(text)
    elif anim_type == "matrix":
        matrix_rain()
    else:
        print(f"unknown animation: {anim_type}")
