#!/usr/bin/env python3
"""fibonacci sequence generator"""

def fibonacci(n):
    """generate first n fibonacci numbers"""
    if n <= 0:
        return []
    
    fib = [0, 1]
    
    while len(fib) < n:
        next_num = fib[-1] + fib[-2]
        fib.append(next_num)
    
    return fib[:n]

def main():
    import sys
    
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            result = fibonacci(n)
            print(result)
            return
        except ValueError:
            print("please enter a valid number")
            return
    
    # interactive mode
    print("fibonacci sequence generator\n")
    
    try:
        n = int(input("how many numbers? "))
        
        if n <= 0:
            print("enter a positive number lol")
            return
        
        result = fibonacci(n)
        print(f"\n{result}")
        
        # show ratio (golden ratio approx)
        if len(result) > 1:
            ratio = result[-1] / result[-2] if result[-2] != 0 else 0
            print(f"ratio of last two: {ratio:.5f} (golden ratio is ~1.61803)")
    
    except ValueError:
        print("please enter a valid number")
    except KeyboardInterrupt:
        print("\nbye!")

if __name__ == "__main__":
    main()
