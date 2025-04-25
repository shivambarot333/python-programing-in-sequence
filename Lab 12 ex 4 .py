class Shape:
    def __init__(self, side, sides):
        self.side = side
        self.sides = sides

    def perimeter(self):
        return self.side * self.sides

    def area(self):
        from math import tan, pi
        return (self.sides * self.side ** 2) / (4 * tan(pi / self.sides))
