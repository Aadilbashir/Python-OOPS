"""
MULTILEVEL INHERITANCE = Inherit from a parent which inherits from another parent
C(B)<--B(A)<--A
"""


class Animal:  # Grandparent
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):  # Parent
    def flee(self):
        print(f"{self.name} is fleeing")


class Predataor(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):  # Child
    pass


class Hawk(Predataor):
    pass


class Fish(Prey, Predataor):
    pass


rabbit = Rabbit("Cozy")
hawk = Hawk("Tony")
fish = Fish("Feeni")


rabbit.eat()
rabbit.sleep()

hawk.eat()
hawk.sleep()

fish.eat()
fish.sleep()
