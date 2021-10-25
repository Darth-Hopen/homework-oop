import math

from source.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__(name='Circle', angles=0)
        self.radius = radius

    def perimeter(self):
        perimeter = self.radius * 2 * math.pi
        return int(perimeter)

    def area(self):
        area = self.radius ** 2 * math.pi
        return int(area)
