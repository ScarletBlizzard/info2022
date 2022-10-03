class Mother:

    def get_str(self):
        return "Mother"

    def __str__(self):
        return self.get_str()


class Daughter(Mother):

    def get_str(self):
        return "Daughter"


if __name__ == "__main__":
    mother = Mother()
    print(mother)
    daughter = Daughter()
    print(daughter)
