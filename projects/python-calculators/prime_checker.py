#!/usr/bin/env python3
"""check if a number is prime"""

def is_prime(n):
    """check if n is prime using trial division"""
    
    if n < 2:
        return False, None
    
    if n == 2:
        return True, None
    
    if n % 2 == 0:
        return False, 2
    
    # check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False, i
        i += 2
    
    return True, None

def main():
    import sys
    
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            prime, divisor = is_prime(n)
            
            if prime:
                print(f"{n} is prime!")
            else:
                if divisor:
                    print(f"{n} is not prime (divisible by {divisor})")
                else:
                    print(f"{n} is not prime")
            return
        except ValueError:
            print("please enter a valid number")
            return
    
    # interactive mode
    print("prime number checker\n")
    
    try:
        while True:
            user_input = input("enter a number (or 'quit'): ")
            
            if user_input.lower() == 'quit':
                break
            
            n = int(user_input)
            prime, divisor = is_prime(n)
            
            if prime:
                print(f"{n} is prime!\n")
            else:
                if divisor:
                    print(f"{n} is not prime (divisible by {divisor})\n")
                else:
                    print(f"{n} is not prime\n")
    
    except ValueError:
        print("please enter a valid number")
    except KeyboardInterrupt:
        print("\nbye!")

if __name__ == "__main__":
    main()
