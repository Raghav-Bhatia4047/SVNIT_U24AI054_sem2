import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

rect = Rectangle(4, 5)
circle = Circle(3)

print(f"Rectangle Area: {rect.area()}, Perimeter: {rect.perimeter()}")
print(f"Circle Area: {circle.area()}, Perimeter: {circle.perimeter()}")

