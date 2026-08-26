#!/usr/bin/env python3
"""quadratic equation solver: ax² + bx + c = 0"""

import cmath  # for complex numbers

def solve_quadratic(a, b, c):
    """solve quadratic equation using quadratic formula"""
    
    discriminant = (b ** 2) - (4 * a * c)
    
    # two solutions
    x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    return x1, x2

def main():
    print("quadratic equation solver")
    print("solves: ax² + bx + c = 0\n")
    
    try:
        a = float(input("enter a: "))
        b = float(input("enter b: "))
        c = float(input("enter c: "))
        
        if a == 0:
            print("if a=0, this isnt a quadratic equation lol")
            return
        
        x1, x2 = solve_quadratic(a, b, c)
        
        print(f"\nroots: x = {x1}, x = {x2}")
        
        # show if complex
        if x1.imag != 0 or x2.imag != 0:
            print("(complex roots)")
        
    except ValueError:
        print("please enter valid numbers")
    except KeyboardInterrupt:
        print("\nbye!")

if __name__ == "__main__":
    main()
