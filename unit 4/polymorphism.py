# polymorphism in python:
class Car:  # create class Car
    def ride(self):
        print("Let's go for a ride the car.")

class Bike:
    def ride(self):
        print("Let's go for a ride the bike.")

class Auto:
    def ride(self):
        print("Let's go for a ride the auto.")

def ride_vehicle(vehicle):
    vehicle.ride()

ride_vehicle(Car())
ride_vehicle(Bike())
ride_vehicle(Auto())