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

# Multiple Inheritance

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

# Multilevel Inheritance

class Grandprents:
    def info(self):
        print("I am a grandparent.")

class Parents(Grandprents):
    def details(self):
        print("I am a parent.")

class Child(Parents):
    def message(self):
        print("I am a child.")

c = Child()
c.info()
c.details()
c.message()

# Hierarchical Inheritance

