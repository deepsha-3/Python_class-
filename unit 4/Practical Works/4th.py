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
