# Write a program to illustrate variables, constants, data types and type conversion.

# Variables 
name = "Dipisha" # name is a variable
age = "60"      # age is a variable
print("My name is", name, "and I am", age, "years old.")
print("")

# Constants
PI = 3.14   # PI is a constant 
G = 9.8       # G is a constant
print("The value of PI is", PI)
print("The value of G is", G)
print("")

# Data Types

name = "Dipisha"  # String
print("The data type of name is", type(name))

num = 98000000    #Integer
print("The data type of num is", type(num))

fl = 9.8
print("The data type of float is", type(fl))
print("")

# Type Conversion
num= 10
print(type(num))   # num is an integer

num="10"    # convert num integer to string 
print(type(num))    # this num is a string

num= int(num)  # convert num string to integer
print(type(num))  # this num is an integer again 