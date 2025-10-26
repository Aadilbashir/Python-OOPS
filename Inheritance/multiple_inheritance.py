"""
MULTIPLE INHERITANC = Inherit from more than one parent class
C(A,B)
"""


class Prey:
    def flee(self):
        print("This animal is fleeing")


class Predataor:
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predataor):
    pass


class Fish(Prey, Predataor):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
