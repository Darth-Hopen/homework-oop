import math
from source.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__(name='Triangle', angles=3)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        perimeter = self.a + self.b + self.c
        return int(perimeter)

    def area(self):
        area = self.perimeter() / 2
        return int(area)
