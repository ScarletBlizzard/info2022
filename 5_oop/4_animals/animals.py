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


class FlyerMixin():

    def fly(self):
        for wing in self.wings: wing.flap() 


class Bat(Mammal, FlyerMixin):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.wings = [WebbedWing() for _ in range(2)]


class Bird(Animal, FlyerMixin):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.wings = [FeatheredWing() for _ in range(2)]


class Insect(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)


class Mosquito(Insect, FlyerMixin):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.wings = [Wing() for _ in range(2)]


class Dragonfly(Insect, FlyerMixin):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.wings = [Wing() for _ in range(4)]


if __name__ == "__main__":
    bird = Bird("SomeBird", 3)
    bird.fly()

    bat = Bat("SomeBat", 2)
    bat.fly()

    mosquito = Mosquito("Mosquito", 1)
    mosquito.fly()

    dragonfly = Dragonfly("Dragonfly", 1)
    dragonfly.fly()
