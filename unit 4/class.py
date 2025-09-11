# class attribute and object instances in python:

class Car:     # create class 
    name =  ""
    color = ""
    model = ""

car1 = Car()    # object
car2 = Car()  # Object 


# details for car1 properties
car1.name = "BMW"
car1.color = "Black"
car1.model = "x6"

# details for car2 properties
car2. name =  "Audi"
car2. color = "Black"
car2. model = " 2025" 

# print the value
print(f"This is the car detils:{car1.name}, {car1.color}, {car1.model}")
print(f"This is the car detils:{car2.name}, {car2.color}, {car2.model}")