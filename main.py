import math
from exceptions.zero_denominator_error import *


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.sign = 1

        if self.denominator == 0:
            raise ZeroDenominatorError()

        if self.denominator < 0 and self.numerator < 0:
            self.sign = 1
            self.denominator = abs(self.denominator)
            self.numerator = abs(self.numerator)

        elif self.denominator < 0:
            self.sign = -1
            self.denominator = abs(self.denominator)

        elif self.numerator < 0:
            self.sign = -1
            self.numerator = abs(self.numerator)

        self.k = math.gcd(self.numerator, self.denominator)
        if self.k != 1:
            self.numerator = self.numerator // self.k
            self.denominator = self.denominator // self.k

    def __raw__add__(self, sign, numerator, denominator):
        new_denominator = math.lcm(self.denominator, denominator)
        new_numerator = int(self.sign * self.numerator * (new_denominator / self.denominator) \
                            + sign * numerator * (new_denominator /denominator))

        return new_denominator, new_numerator

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_denominator, new_numerator = self.__raw__add__(other.sign, other.numerator, other.denominator)

        elif isinstance(other, int):
            new_denominator, new_numerator = self.__raw__add__(1, other, 1)

        elif isinstance(other, float):
            raise TypeError(other)
        else:
            raise Exception('Not int or Fraction value.')

        return Fraction(new_numerator, new_denominator)

    def __iadd__(self, other):
        return self + other

    def __str__(self):
        if self.sign == 1:
            return f'{self.numerator}/{self.denominator}'
        if self.sign == -1:
            return f'-{self.numerator}/{self.denominator}'

    def __float__(self):
        return self.numerator / self.denominator


class FractionWithInteger(Fraction):
    def __init__(self, integer, numerator, denominator):
        super(FractionWithInteger, self).__init__(numerator, denominator)
        self.integer = integer

        if self.integer < 0:
            self.sign *= -1
            self.integer = abs(self.integer)
        
        if self.denominator < self.numerator:
            self.integer += self.numerator // self.denominator
            self.numerator = self.numerator - self.denominator * (self.numerator // self.denominator)

        if self.denominator == 1:
            self.integer += self.numerator
            self.numerator = 0

    def __add__(self, other):
        if isinstance(other, FractionWithInteger):
            new_integer = self.integer * self.sign + other.integer * other.sign
            new_denominator, new_numerator = self.__raw__add__(other.sign, other.numerator, other.denominator)

        return FractionWithInteger(new_integer, new_numerator, new_denominator)

    def __str__(self):
        prefix = '' if self.sign > 0 else '-'
        if self.numerator == 0:
            return f'{prefix}{self.integer}'
        return f'{prefix}{self.integer} {self.numerator}/{self.denominator}'


# frac1 = Fraction(-1, -4)
# frac2 = Fraction(-3, 4)
# print(frac1)
# print(frac2)

# frac1 += frac2
# print(frac1)


frac3 = FractionWithInteger(0,-4,2)
frac4 = FractionWithInteger(1,4,2)

print(frac3)
print(frac4)

print(frac3 + frac4)


