class Figure:
    name = None
    angles = None
    perimeter = None
    area = None

    def __init__(self, name, angles):
        self.name = name
        self.angles = angles

    def get_name_and_angles(self):
        if self.angles > 0:
            return f'{self.name} with {self.angles} angles'
        else:
            return f'{self.name}'

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            sum_figures = self.area() + other_figure.area()
            return int(sum_figures)
        else:
            raise AttributeError('Function got unknown class')
