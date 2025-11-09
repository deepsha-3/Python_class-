
# sets 

set1 = {0, 1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union 
u = set1 | set2
print("Union of set1 and set2:", u)

# intersection
i = set1 & set2
print("Intersection of set1 and set2:", i)

# difference 
d1 = set1 - set2
print("Difference of set1 and set2 :", d1)

d2 = set2 - set1
print("Difference of set2 and set1 :", d2)

# adding an element
set1.add(6)
print("Set1 after adding an element:", set1)        

# removing an element
set2.remove(8)
print("Set2 after removing an element:", set2)