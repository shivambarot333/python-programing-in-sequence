class Solid:
    def _init_(self, shape, **kwargs):
        self.shape = shape
        self.data = kwargs

    def volume(self):
        if self.shape == 'cube':
            return self.data['side'] ** 3
        elif self.shape == 'sphere':
            from math import pi
            return (4/3) * pi * self.data['radius'] ** 3

    def surface_area(self):
        if self.shape == 'cube':
            return 6 * self.data['side'] ** 2
        elif self.shape == 'sphere':
            from math import pi
            return 4 * pi * self.data['radius'] ** 2
