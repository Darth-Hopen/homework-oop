from source.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, name, a):
        try:
            super().__init__(name, a, a)
        except ValueError:
            pass
