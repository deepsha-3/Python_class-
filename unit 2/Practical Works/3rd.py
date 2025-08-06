# Write a program to demonstrate input validation using loop. 


while True:
    try:
        num = int(input("Enter a positive number:"))
        if num > 0:
            print("You entered a valid number:", num)
            break
        else:
           print("Please enter a positive number.")
    except ValueError:
        print("Invalid input.")