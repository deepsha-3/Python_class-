# write a program apply inheritance where Vehicle class. 

class Vehicle:  #parent class
    def drive(self):
        print("Drive your vehicle.")

    def honk(self):
        print("honk !")

class Car(Vehicle):  
    def color(self):
        print("Explain your car color.")
        
car = Car()
car.drive()
car.honk()
car.color()
