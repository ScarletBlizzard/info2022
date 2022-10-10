class Student:

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __hash__(self):
        return self.number

    def __eq__(self, other):
        return self.number == other.number

    def __repr__(self):
        return f"Student({self.name}, {self.number})"


if __name__ == "__main__":
    petya = Student("Петя", 2383488843288820)
    vasya = Student("Вася", 4304893489043999)
    kolya = Student("Коля", 2383488843288820)
    print(set([petya, vasya, kolya]))
