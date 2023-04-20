import math


class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def __str__(self):
        return f"{self.name}, color: {self.color}"


class Rectangle(Shape):
    def __init__(self, name, color, length, width):
        super().__init__(name, color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"{super().__str__()}, length: {self.length}, width: {self.width}"


class Circle(Shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"{super().__str__()}, radius: {self.radius}"


class Square(Shape):
    def __init__(self, name, color, side):
        super().__init__(name, color)
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return f"{super().__str__()}, side: {self.side}"


if __name__ == '__main__':
    r = Rectangle("Rectangle", "blue", 10, 5)
    print(r)
    print(f"Area: {r.area()}, Perimeter: {r.perimeter()}")

    c = Circle("Circle", "red", 5)
    print(c)
    print(f"Area: {c.area()}, Perimeter: {c.perimeter()}")

    s = Square("Square", "green", 8)
    print(s)
    print(f"Area: {s.area()}, Perimeter: {s.perimeter()}")
