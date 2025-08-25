# Write program to perform set operations. 

# create a set 
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8}

# union 
u = set1 | set2
print("Union of this set:", u)

# intersection 
i =  set1 & set2 
print("Intersection of this set:", i)

# difference 
d1 = set1 - set2
print("The first difference of this set:", d1)

d2 = set2 - set1
print("The second difference of this set:", d2)

# symmetric difference
s = set1 ^ set2
print("Symmetric difference of this set:", s)