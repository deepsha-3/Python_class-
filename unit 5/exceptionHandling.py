# Exception Handling in Python
try:
    num =int(input("Enter a number:"))
    result = 10/ num
    print("This is the result:", result)

except ZeroDivisionError:
    print("You can't divide by zero.")

except ValueError:
    print("That's not a valid number.")