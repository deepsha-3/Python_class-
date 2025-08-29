# Write program to make use of __init__ method to initialize objects.

# create class 
class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def display_info(self):
        print(f"Car Model: {self.model}")
        print(f"Car Color: {self.color}")
        print(f"Car Year: {self.year}")


        