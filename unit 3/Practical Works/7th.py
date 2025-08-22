# Write program to create dictionary, add elements in dictionary, remove elements from dictionary and display dictionary items. 

# create dictionary
dictionary = {
    'name': 'Dipisha',
    'age': 12,
    'city': 'Munich'
}

print("The original dictionary: " , dictionary)

# adding elements
dictionary['country'] = 'Germany'
dictionary['hobby'] = 'Coding'
print("After adding elements: " , dictionary)

# removing elements
del dictionary['age']     
print("After removing elements: " , dictionary)
