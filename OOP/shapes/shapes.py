class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def __str__(self):
        return f"({self.width}, {self.height})"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length)
        self.length = length

    def __repr__(self):
        return f"Square(length={self.length}"

    def __str__(self):
        return f"({self.length})"



shape1 = Square("10")
print(shape1)