# Before: Square extends Rectangle but breaks its contract
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width  # Forces equal sides

    def set_height(self, height):
        self.width = height  # Forces equal sides
        self.height = height

# Client code that breaks with Square
def resize(rect):
    rect.set_width(5)
    rect.set_height(10)
    print("Area:", rect.get_area())

resize(Rectangle())  # Area: 50
resize(Square())     # Area: 100 -- LSP violation!

# TODO: Refactor using a Shape interface (ABC) with get_area().
# TODO: Rectangle and Square should be independent implementations of Shape.

from abc import ABC, abstractmethod
class Shape(abstractmethod):

    @abstractmethod
    def getArea(self):
        pass


class Rectangle(Shape):

    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def getArea(self):
        return self.height * self.width


class Square(Shape):

    def __int__(self, length):
        self.length = length
    
    def getArea(self):
        return self.length * self.length


if __name__ == "__main__":
    rectangle: Shape = Rectangle(5, 10)
    square: Shape = Square(5)

    print(f"Rectangle area: {int(rectangle.get_area())}")
    print(f"Square area: {int(square.get_area())}")