# Write program to apply if, match, break, continue statements for decision making

# 1. If statement 
print("If statement:")
age = 18
if age >= 18:
    print("You are eligible for voting.")
print("")

# 2. Match statement 
print("Match statement:")
score = 85
match score:
    case 90 | 100:
        print("You got an A+")
    case 80 | 89:
        print("You got an A")
    case _:
        print("You got a B")
print("")

# 3. Break statement
print("Break statement:")
for i in range(20):
    if i == 10:
        break
    print(i)
print("")

# 4. Continue statement
print("Continue statement:")
for i in range(20):
    if i == 10:
        continue
    print(i)