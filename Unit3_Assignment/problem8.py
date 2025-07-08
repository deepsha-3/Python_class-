# Write a Python program to:
   # • Create two sets
   # • Perform union, intersection, and difference
   # • Add and remove elements from a set 

# Create two sets
A = {1, 2, 3, 4, 5, 6, 7}
B = {4, 6, 7, 8, 9, 10}

print("The original sets:",A)
print("The original sets:",B)

# Union 
U = A|B
print("The union of two sets:", U)

# Intersection
I = A&B
print("The intersection of two sets:",I)

# Difference 
D1 = A-B
print("The difference of A and B:",D1)

D2 = B-A
print("The difference between B and A:",D2)