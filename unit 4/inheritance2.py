# heritance example

class Animal:   # class
    def sound(self):
        print("Animal makes sound.")

class Dog(Animal):  # first child class 
    def bark(self):
        print("Dog barks.")

class Cat(Animal):  # second child class
    def meow(self):
        print("Cat meows.")

# object create from first class 
d = Dog()
d.sound()
d.bark()

# object create from second class 
c = Cat()
c.sound()
c.meow()

