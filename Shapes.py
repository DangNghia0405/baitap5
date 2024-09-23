import math

class Shape:
    def __init__(self):
        pass
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius 

    def calculate_area(self):
        return math.pi * (self.__radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius
    
class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return (self.__height * self.__width)
                
    def calculate_perimeter(self):
        return (self.__height + self.__width) * 2

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())