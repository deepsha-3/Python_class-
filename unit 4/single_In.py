# single inheritance python:

class Car:  # create class
    def color(self):
        print("The color of the car is Black.")

class BMW(Car): # create class BMW / drive class 
    def model(self): 
        print("The model of the car is BMW x5.")

car = BMW() # create object
car.color() 
car.model()