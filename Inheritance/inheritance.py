"""
INHERITANCE = Allows a class to inherit attributes and methods from another class
              Helps with code Reusuability and extensibility
              Eg, Grandparent --> Parent --> Son
"""


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Cat(Animal):
    def speak(self):
        print("Meow")


class Dog(Animal):
    def speak(self):
        print("Wouw")


class Mouse(Animal):
    def speak(self):
        print("Chi chi")


cat = Cat("Mikey")
dog = Dog("Pit bull")
mouse = Mouse("Hana")

"""
print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
"""
cat.speak()
dog.speak()
mouse.speak()
