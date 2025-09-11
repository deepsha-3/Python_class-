# Write program to elaborate object oritented concept with simple examples. 

# create class
class Car:
    def __init__(self,model, color, year):
        self.model = model
        self.color = color
        self.year = year
    
    def car_info(self):
        print(f"Car Model: {self.model}")
        print(f"Car Color: {self.color}")
        print(f"Car Year: {self.year}")

# create object
my_car = Car("BMW", "Black", 2020)

# call method
my_car.car_info()
