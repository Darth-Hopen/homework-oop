from source.Figure import Figure


class Rectangle(Figure):
    def __init__(self, name, a, b):
        super().__init__(name, 4)
        self.a = a
        self.b = b
        if a == b:
            raise ValueError('The output figure is a square')

    def perimeter(self):
        perimeter = (self.a + self.b) * 2
        return int(perimeter)

    def area(self):
        area = self.a * self.b
        return int(area)
