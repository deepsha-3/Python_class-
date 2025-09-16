# multiple inheritance example:
class Car: # create class
    def color(self):
        print("The color of the car is Black.")

class Bike: # create class
    def model(self):
        print("The model of the car is BMW x5.")
        
class Vehicle(Car, Bike): # child class
    def type(self):
        print("This is a vehicle that can be a car or a bike.")

v = Vehicle()
v.color()
v.model()
v.type()
