# Write program to create a different patterns using nested loop.

# 1. This is a simple pattern print(Square pattern):
print("Square pattern:")
row= 6
for i in range(row): 
    for a in range(row):
        print("*", end="")
    print("")


# 2. This is a simple pattern print(Triangle pattern):

print("Triangle pattern:")
for i in range(row, 0, -1):
    for j in range(i):
        print("*" , end="")
    print("")

# 3. Pyramid pattern:
print("Pyramid pattern:")
for p in range(1, row+1):
    print(" " * (row - p), end="")
    print("* " * p)
   