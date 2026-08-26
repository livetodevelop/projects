#!/usr/bin/env python3
"""simple 2x2 and 3x3 matrix calculator"""

def determinant_2x2(matrix):
    """calculate determinant of 2x2 matrix"""
    # [[a, b], [c, d]]
    a, b = matrix[0]
    c, d = matrix[1]
    return (a * d) - (b * c)

def determinant_3x3(matrix):
    """calculate determinant of 3x3 matrix using rule of sarrus"""
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    
    return (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)

def inverse_2x2(matrix):
    """calculate inverse of 2x2 matrix"""
    det = determinant_2x2(matrix)
    
    if det == 0:
        return None  # no inverse
    
    a, b = matrix[0]
    c, d = matrix[1]
    
    # swap a and d, negate b and c, divide by det
    inv = [
        [d/det, -b/det],
        [-c/det, a/det]
    ]
    
    return inv

def multiply_matrix_vector(matrix, vector):
    """multiply matrix by vector"""
    result = []
    
    for row in matrix:
        val = sum(row[i] * vector[i] for i in range(len(vector)))
        result.append(val)
    
    return result

def print_matrix(matrix):
    """pretty print a matrix"""
    for row in matrix:
        formatted = [f"{x:8.4f}" if isinstance(x, float) else f"{x:8}" for x in row]
        print("| " + "  ".join(formatted) + " |")

def main():
    print("matrix calculator (2x2 and 3x3 only)")
    print("operations: det, inverse, multiply\n")
    
    try:
        size = int(input("matrix size (2 or 3): "))
        
        if size not in [2, 3]:
            print("only 2x2 and 3x3 supported rn lol")
            return
        
        print(f"\nenter {size}x{size} matrix (row by row):")
        matrix = []
        
        for i in range(size):
            row = input(f"row {i+1} (space separated): ").split()
            row = [float(x) for x in row]
            
            if len(row) != size:
                print(f"need {size} values per row")
                return
            
            matrix.append(row)
        
        print("\nyour matrix:")
        print_matrix(matrix)
        
        print("\noperations: det, inverse, mult-vector, quit")
        
        while True:
            op = input("\noperation: ").lower().strip()
            
            if op == 'quit':
                break
            
            elif op == 'det':
                if size == 2:
                    det = determinant_2x2(matrix)
                else:
                    det = determinant_3x3(matrix)
                print(f"determinant: {det}")
            
            elif op == 'inverse':
                if size == 2:
                    inv = inverse_2x2(matrix)
                else:
                    print("3x3 inverse not implemented yet sorry")
                    continue
                
                if inv is None:
                    print("matrix has no inverse (determinant = 0)")
                else:
                    print("inverse:")
                    print_matrix(inv)
            
            elif op == 'mult-vector':
                vector = input(f"enter {size}-element vector: ").split()
                vector = [float(x) for x in vector]
                
                if len(vector) != size:
                    print(f"need {size} values")
                    continue
                
                result = multiply_matrix_vector(matrix, vector)
                print(f"result: {result}")
            
            else:
                print("unknown operation")
    
    except ValueError:
        print("please enter valid numbers")
    except KeyboardInterrupt:
        print("\nbye!")

if __name__ == "__main__":
    main()
