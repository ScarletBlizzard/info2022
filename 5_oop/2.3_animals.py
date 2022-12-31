class Animal():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_description(self):
        return f"Name: {self.name}, age: {self.age}"

    def __str__(self):
        return self.get_description()


class Zebra(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def get_description(self):
        return f"Name: {self.name}, age: {self.age}, species: zebra"


class Dolphin(Animal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def get_description(self):
        return f"Name: {self.name}, age: {self.age}, species: dolphin"


if __name__ == "__main__":
    zebra = Zebra("Zebra", 3)
    print(zebra)
    dolphin = Dolphin("Dolphin", 5)
    print(dolphin.get_description())
