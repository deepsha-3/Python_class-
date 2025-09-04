# Write program to divide work in functions.

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a,b):
    if b != 0:
        return a/b
    else:
        return "Cannot divide by zero"
    
def main():
   a = 20
   b= 10

   print("Addition value is:", add(a,b))

   print("Subtraction value is:", subtract(a,b))

   print("Multiplication value is:", multiply(a,b))