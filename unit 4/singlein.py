# single inheritance python:

class Car:
    def color(self):
        print("The color of the car is Black.")

class BMW(Car):
    def model(self):
        print("The model of the car is BMW x5.")

car = BMW()
car.color()
car.model()