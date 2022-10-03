class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Triangle(Shape):
    
    def __init__(self, width, height):
        super().__init__(width, height)
    
    def area(self):
        return 0.5 * self.width * self.height


class Rectangle(Shape):
    
    def __init__(self, width, height):
        super().__init__(width, height)
    
    def area(self):
        return self.width * self.height

if __name__ == "__main__":
    square = Rectangle(3, 3)
    print(square.area())
