from wings import *


class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def get_description(self):
        return f"Name: {self.name}, age: {self.age}"

    def __str__(self):
        return self.get_description()


class Mammal(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)


class Zebra(Mammal):

    def __init__(self, name, age):
        super().__init__(name, age)


class Dolphin(Mammal):

    def __init__(self, name, age):
        super().__init__(name, age)


class WingedMixin():

    def fly(self):
        for wing in self.wings: wing.flap() 


class Bat(Mammal, WingedMixin):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.wings = [WebbedWing() for _ in range(2)]


class Bird(Animal, WingedMixin):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.wings = [FeatheredWing() for _ in range(2)]


class Insect(Animal, WingedMixin):
    def __init__(self, name, age, wings_count=0):
        super().__init__(name, age)
        self.wings = [Wing() for _ in range(wings_count)]


if __name__ == "__main__":
    bird = Bird("SomeBird", 3)
    bird.fly()

    bat = Bat("SomeBat", 2)
    bat.fly()

    insect = Insect("SomeBug", 1, 2)
    insect.fly()
