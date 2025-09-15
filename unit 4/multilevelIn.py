# multilevel inheritance example in Python:

class Vehicle:  # create class 
    def color(self):
        print("The color of the vehicle is Blue.")


class Car(Vehicle):  # child class
    def model(self):
        print("The model of the vehicle is BMW X5.")

class BMW(Car):
    def speed(self):
        print("The speed of the BMW X5 is 250 km/h.")

v = BMW()
v.color()
v.model()
v.speed()

