# Define a class named Circle which can be constructed by a radius. The Circle
# class has a method which can compute the area.

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return self.radius ** 2 * pi
        
circle = Circle(3)
print(circle.area())
