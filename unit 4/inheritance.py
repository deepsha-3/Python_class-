# Inheritance in Python:

class Person:    # parent class
    def talk(self):
        print("I can talk!")

    def walk(self):
            print("I can walk!")

class Student(Person): # child class 
    def study(self):
        print("I can study!")

s = Student()
s.talk()  # Inherited from Person class
s.walk()  # Inherited from Person class
s.study()  # From Student class 