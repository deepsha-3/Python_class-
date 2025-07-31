# multiple inheritance example:
class Car:
    def color(self):
        print("The color of the car is Black.")

class Bike:
    def model(self):
        print("The model of the car is BMW x5.")
        
class Vehicle(Car, Bike):
    def type(self):
        print("This is a vehicle that can be a car or a bike.")

v = Vehicle()
v.color()
v.model()
v.type()
