# Write a program to apply different types of inheritance.

# Single Inheritance

class Car:
    def drive(self):
        print("Car is driving")

class SportsCar(Car):
    def race(self):
        print("Sports car is racing")

car = SportsCar()
car.drive()
car.race()

# Multiple inheritance 
class Animal:
    def speak(self):
        print("Animal speak")

