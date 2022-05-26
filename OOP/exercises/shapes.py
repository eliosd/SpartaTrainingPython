class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __str__(self):
        return f"({self.width}, {self.height})"

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        self.height = length
        self.width = length
        self.length = length


    def __repr__(self):
        return f"Square(length={self.length}"

    def __str__(self):
        return f"({self.length})"

    def get_area(self):
        area = self.length ** 2
        return area



shape1 = Square(5)
print(shape1.get_area())
print(shape1)

rect = Rectangle(10, 5)
print(rect.get_area())