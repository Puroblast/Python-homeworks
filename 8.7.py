class Complex:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x * other.x


b = Complex(complex(3, 1))
c = Complex(complex(2, -3))
print(b.__add__(c))
print(b.__sub__(c))
