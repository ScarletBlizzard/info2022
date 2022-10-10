class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @classmethod
    def from_string(cls, s):
        s = s.replace('i', '')
        if '+' in s:
            s = s.split('+')
        elif '-' in s:
            s = s.split('-')
        return cls(float(s[0]), float(s[1]))

    def __imag_sign(self):
        return '+' if self.imag >= 0 else '-'

    def __str__(self):
        return str(self.real) + self.__imag_sign() + str(abs(self.imag)) + 'i'

    def __repr__(self):
        return "Complex({}, {})".format(self.real, self.imag)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag,
                self.imag*other.real + self.real*other.imag)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        return Complex((self.real*other.real + self.imag*other.imag) /
                denominator, (self.imag*other.real - self.real*other.imag) /
                denominator)

    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5


if __name__ == "__main__":
    print(Complex(2, 3))
    print(Complex(2, -3))
    print(Complex(-2, -3))
    print(eval(repr(Complex(-2, 3))))
    print(Complex.from_string('8+9i'))
    print(Complex(-1.5, -3.3))
    a, b = Complex(1, 2), Complex(-1, -2)
    print(a + b)
    print(a * b)
    print(a / b)
    print(abs(Complex(3, 4)))
    Complex(0, 1).__getattribute__()
