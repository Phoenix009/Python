class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        num = (self.num * other.den) + (other.num * self.den)
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = (self.num * other.den) - (other.num * self.den)
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def __float__(self):
        return self.num / self.den
    

f1 = Fraction(1, 2)
f2 = Fraction(1, 2)
print(f1)
print(f2)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)
print(float(f1))
