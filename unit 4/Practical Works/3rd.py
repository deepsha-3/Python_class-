# Write a program to apply different types of inheritance.

# Single Inheritance

class Car:
    def drive(self):
        print("Car is driving.")

class SportsCar(Car):
    def race(self):
        print("Sports car is racing.")

car = SportsCar()
car.drive()
car.race()

# Multiple inheritance 
class Cat:
    def meow(self):
        print("Cat meows.")

class Dog:
    def bark(self):
        print("Dog barks.")

class Animal(Cat, Dog):
    def speak(self):
        print("Animal speaks.")

a = Animal()
a.meow()
a.bark()
a.speak()
