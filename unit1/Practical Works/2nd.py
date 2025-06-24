# Write a program to demostrate different types of operators in python and perform calculations. 

# addition, subtraction, multiplication, division, modulus, exponentiation and floor division

a = 10
b= 5
# Arithmetic Operators
print("Addition:", a + b)          # This is Addition Operator
print("Subtraction:", a - b)       # This is Subtraction Operator   
print("Multiplication:", a * b)    # This is Multiplication Operator
print("Division:", a / b)          # This is Division Operator
print("Modulus:", a % b)           # This is Modulus Operator
print("Exponentiation:", a ** b)   # This is Exponentiation Operator
print("Floor Division:", a // b)   # This is Floor Division Operator


# Comparison Operators
print( a == b)     # Equal to Operator
print( a != b)     # Not equal to
print( a > b)      # Greater than
print( a < b)      # Less than
print( a >= b)     # Greater than
print( a <= b)     # Less than or equal to

# Logical Operators
print("Logical AND:", a > 0 and b > 0)   # Logical AND
print("Logical OR:", a > 0 or b < 0)     # Logical OR
print("Logical NOT:", not (a > 0))       # Logical NOT


# Assignment Operators
a += 5                        # Add and assign
print("New value of a", a)  
b -= 2                        # Subtract and assign
print("New value of b =", b)  
a *= 2                         # Multiply and assign
print("New value of a =", a) 
b /= 3                         # Divide and assign
print("New value of b =", b)  
