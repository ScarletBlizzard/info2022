class Vector:

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def __matmul__(self, other):
        return Vector(self.y*other.z - self.z*other.y, self.z*other.x -
                self.x*other.z, self.x*other.y - self.y*other.x)

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    @classmethod
    def from_str(cls, s):
        return cls(*s.split(','))

    def div_coords_by_n(self, n):
        return Vector(self.x / n, self.y / n, self.z / n)


def test():
    print(Vector(1, 2, 3))
    a, b = Vector(1, 1, 1), Vector(2, 3, 4)
    print(a * b)
    a, b = Vector(1, 0, 0), Vector(0, 1, 0)
    print(a @ b)


def main():
    N = int(input())
    mx = 0
    farthest = Vector(0, 0, 0)
    coords_sum = Vector(0, 0, 0)
    for _ in range(N):
        point = Vector.from_str(input())
        coords_sum += point
        distance = abs(point)
        if distance > mx:
            mx = distance
            farthest = point
    print(farthest)
    print(coords_sum.div_coords_by_n(N))


if __name__ == "__main__":
    #test()
    main()
