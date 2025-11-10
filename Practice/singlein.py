
# single inheritance

class Car:
    def car_info(self):
        print("This is a car.")

class BMW(Car):
    def bmw_info(self):
        print("This is a BMW car.")

bmw = BMW()