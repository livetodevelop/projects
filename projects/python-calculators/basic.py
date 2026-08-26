#!/usr/bin/env python3
"""basic calculator - made when i was bored in math class"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error: cant divide by zero lol"
    return a / b

def main():
    print("basic calculator")
    print("operations: +, -, *, /")
    print("type 'quit' to exit\n")
    
    while True:
        try:
            expr = input("enter expression (e.g., 5 + 3): ")
            
            if expr.lower() == 'quit':
                break
            
            # simple parsing
            parts = expr.split()
            if len(parts) != 3:
                print("format: number operator number")
                continue
            
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
            
            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)
            else:
                print("unknown operator")
                continue
            
            print(f"result: {result}\n")
            
        except ValueError:
            print("please enter valid numbers\n")
        except KeyboardInterrupt:
            print("\nbye!")
            break

if __name__ == "__main__":
    main()
