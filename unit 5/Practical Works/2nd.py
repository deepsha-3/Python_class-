# Write different variety of functions: function with arguments, value returning function, function without arguments.

# function with argument

def greet(name):
    print("Hello,",name)

greet("Kartik") 

# value returning function

def add(a,b):
    return a+b
result = add(3,5)
print("Sum is:",result)


# function without argument

def greet1():
    print("Hello, World!")

greet1()  