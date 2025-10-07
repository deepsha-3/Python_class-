# Write a program to demostrate different types of operators in python and perform calculations. 

# addition, subtraction, multiplication, division, modulus, exponentiation and floor division

a = 10
b = 5

# 1. Arithmetic Operators

print("Addition:", a + b)          # This is Addition Operator
print("Subtraction:", a - b)       # This is Subtraction Operator   
print("Multiplication:", a * b)    # This is Multiplication Operator
print("Division:", a / b)          # This is Division Operator
print("Modulus:", a % b)           # This is Modulus Operator
print("Exponentiation:", a ** b)   # This is Exponentiation Operator
print("Floor Division:", a // b)   # This is Floor Division Operator
print("")

# 2. Comparison Operators
print("The a and b are equal:", a == b)     # Equal to Operator
print("The a and b are not equal:", a != b)     # Not equal to
print("The a is greater than b:", a > b)      # Greater than
print("The a is less than b:", a < b)      # Less than
print("The a is greater than or equal to b:", a >= b)     # Greater than
print("The a is less than or equal to b:", a <= b)     # Less than or equal to
print("")

# 3. Logical Operators
print("Logical AND:", a > 0 and b > 0)   # Logical AND
print("Logical OR:", a > 0 or b < 0)     # Logical OR
print("Logical NOT:", not (a > 0))       # Logical NOT
print("")


# 4. Assignment Operators
a += 5                        # Add and assign
print("New value of a", a)  
b -= 2                        # Subtract and assign
print("New value of b =", b)  
a *= 2                         # Multiply and assign
print("New value of a =", a) 
b /= 3                         # Divide and assign
print("New value of b =", b)  
