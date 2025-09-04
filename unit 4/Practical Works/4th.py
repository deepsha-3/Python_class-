# Write a Program to elaborate polymorphism and data hiding concept. 

# Polymorphism
      # create a class 
class Animal: 
    def speak(self): 
        print("Animal speaks.")

class Dog(Animal):
    def speak(self):
        print("The dog barks")

class Cat(Animal):
    def speak(self):
        print("The cat meows")

def animal_sound(animal):
    animal.speak()

animal_sound(Dog())
animal_sound(Cat())

# hiding data 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # private attribute

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.__age}")

person = Person("Sachin", 60)
person.display_info()
# person.__age  # This will raise an AttributeError
