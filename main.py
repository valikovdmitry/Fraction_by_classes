import math


def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


class ZeroDenominatorError(Exception):
    def __init__(self):
        super(ZeroDenominatorError, self).__init__('на ноль делить низя')


class Fraction:
    def __init__(self, numerator, denominator):
        self.integer = 0
        self.numerator = numerator
        self.denominator = denominator


        if self.denominator < self.numerator:
            self.integer = self.numerator // self.denominator
            self.numerator = self.numerator - self.denominator * self.integer

        if self.denominator == 0:
            raise ZeroDenominatorError()

        self.k = math.gcd(self.numerator, self.denominator)
        if self.k != 1:
            self.numerator = self.numerator // self.k
            self.denominator = self.denominator // self.k

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_integer = self.integer + other.integer
            new_denominator = lcm(self.denominator, other.denominator)
            new_numerator = int(self.numerator * (new_denominator / self.denominator) \
                                + other.numerator * (new_denominator / other.denominator))
            # new_numerator += new_integer * new_denominator
            # new_integer = 0

        elif isinstance(other, int):
            new_denominator = self.denominator
            new_numerator = int(self.numerator + other.numerator * self.denominator)

        elif isinstance(other, float):
            raise TypeError(other)
        else:
            raise Exception('Not int or Fraction value.')

        return FractionWithInteger(int(new_integer), new_numerator, new_denominator)

    def __iadd__(self, other):
        return self + other

    def __str__(self):
        if self.integer:
            return f'{self.integer} {self.numerator}/{self.denominator}'
        else:
            return f'{self.numerator}/{self.denominator}'

    def __float__(self):
        return self.numerator / self.denominator


class FractionWithInteger(Fraction):
    def __init__(self, integer, numerator, denominator):
        super(FractionWithInteger, self).__init__(numerator, denominator)
        self.integer = integer

    def __str__(self):
        return f'{self.integer} {self.numerator}/{self.denominator}'


frac1 = Fraction(3, 2)
frac2 = Fraction(2, 4)
print(frac1)
print(frac2)

frac1 += frac2
print(frac1)

# frac3 = Fraction(4,36)
# print(frac3)

#
# intfrac = Fraction(5,4)
# print(intfrac)
# intfrac2 = Fraction(1,4)
# print(intfrac2)

