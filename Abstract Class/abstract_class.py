"""
ABSTARCT CLASS = A class that can not be initiated with its own, meant to be subclassed
They contain abstract methods which are declared but not not Implemented
BENEFITS:
Prevents instantiation of the class itself
Requires children to use inherited abstracted methods
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")


class Motorcycle(Vehicle):
    def go(self):
        print("You drive the Motorcycle")

    def stop(self):
        print("You stop the motorcycle")


class Boat(Vehicle):
    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")


boat = Boat()
boat.go()
boat.stop()
