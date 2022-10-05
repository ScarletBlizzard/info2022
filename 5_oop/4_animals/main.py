from mixins import *


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

    def get_description(self):
        return f"Name: {self.name}, age: {self.age}, biological class: Mammalia"


class Zebra(Mammal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def get_description(self):
        return f"Name: {self.name}, age: {self.age}, biological class: Mammalia, species: Zebra"


class Dolphin(Mammal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def get_description(self):
        return f"Name: {self.name}, age: {self.age}, biological class: Mammalia, species: Dolphin"


class Bat(Mammal, WebbedWingsMixin):

    def __init__(self, name, age):
        super().__init__(name, age)

    def get_description(self):
        return f"Name: {self.name}, age: {self.age}, biological class: Mammalia, order: Bat"


class Bird(Animal, FeatheredWingsMixin):

    def __init__(self, name, age):
        super().__init__(name, age)

    def get_description(self):
        return f"Name: {self.name}, age: {self.age}, biological class: Aves"


class Insect(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def get_description(self):
        return f"Name: {self.name}, age: {self.age}, biological class: Insecta"


class WingedInsect(Insect, WingsMixin):

    def __init__(self, name, age):
        super().__init__(name, age)


class DipterousInsect(WingedInsect, TwoWingsMixin):

    def __init__(self, name, age):
        super().__init__(name, age)


class MultiwingedInsect(WingedInsect, ManyWingsMixin):

    def __init__(self, name, age):
        super().__init__(name, age)


if __name__ == "__main__":
    zebra = Zebra("Zebra", 3)
    print(zebra)

    dolphin = Dolphin("Dolphin", 5)
    print(dolphin.get_description())

    bird = Bird("Bird", 5)
    print(bird)
    bird.fly()

    bat = Bat("Bat", 5)
    print(bat)
    bat.fly()

    insect = Insect("Bug", 5)
    print(insect)

    wingedInsect = WingedInsect("Flying bug", 1)
    wingedInsect.fly()

    dipterousInsect = DipterousInsect("Two-winged bug", 1)
    dipterousInsect.fly()

    multiwingedInsect = MultiwingedInsect("Multiwinged bug", 1)
    multiwingedInsect.fly()
