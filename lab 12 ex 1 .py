class Complex:
    def _init_(self, real, imag):
        self.real = real
        self.imag = imag

    def _add_(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def _sub_(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def _mul_(self, other):
        r = self.real * other.real - self.imag * other.imag
        i = self.real * other.imag + self.imag * other.real
        return Complex(r, i)

    def _truediv_(self, other):
        denom = other.real ** 2 + other.imag ** 2
        r = (self.real * other.real + self.imag * other.imag) / denom
        i = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(r, i)

    def _str_(self):
        return f"{self.real} + {self.imag}i"
