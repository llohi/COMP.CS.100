"""
COMP.CS.100 Murtolukujen laskutoimitukset
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""

from math import gcd


class Fraction:
    """
    A class that represents a fraction.
    """

    def __init__(self, n, d):
        """
        :param n: int, numerator
        :param d: int, denominator
        """

        self.n = n
        self.d = d

    def return_string(self):
        """
        Return a string of the fraction.
        -n/-d  ->  n/d
        n/-d   ->  -n/d
        """

        if self.n and self.d < 0:

            self.n *= -1
            self.d *= -1

            str = f"{self.n}/{self.d}"  # n/d

        elif self.d < 0:

            self.n *= -1
            self.d *= -1

            str = f"{self.n}/{self.d}"  # -n/d

        else:
            str = f"{self.n}/{self.d}"

        return str

    def simplify(self):
        """
        Return a simplified string.
        2/4    ->  1/2
        7/21   ->  1/3
        """

        # greatest common denominator
        d = gcd(self.n, self.d)
        self.n = self.n // d
        self.d = self.d // d

    def complement(self):
        """
        Return the complement of the given fraction as an object of the class.
        -2/4  ->  2/4
        """

        # create numerator and denominator for complement
        n = self.n * -1
        d = self.d

        return Fraction(n, d)

    def reciprocal(self):
        """
        Return the reciprocal of the given fraction as an object of the class.
        2/4  ->  4/2
        """

        # create numerator and denominator for reciprocal
        n = self.d
        d = self.n

        return Fraction(n, d)

    def multiply(self, frac2):
        """
        Return the product of two fractions as an object of the class.
        -15/5 * 3/4 = -45/20
        :param frac2: object of the class
        """

        n = self.n * frac2.n
        d = self.d * frac2.d

        return Fraction(n, d)

    def divide(self, frac2):
        """
        Return the quotient of two fractions as an object of the class.
        -15/5 / 3/4 = -60/15
        :param frac2: object of the class
        """

        n = self.n * frac2.d
        d = self.d * frac2.n

        return Fraction(n, d)

    def add(self, frac2):
        """
        Return the sum of two functions.
        :param frac2: object of the class
        """

        n = self.n * frac2.d + frac2.n * self.d
        d = self.d * frac2.d

        return Fraction(n, d)

    def deduct(self, frac2):
        """
        Return the difference of two functions.
        :param frac2: object of the class
        """

        n = self.n * frac2.d - frac2.n * self.d
        d = self.d * frac2.d

        return Fraction(n, d)

    def __lt__(self, other):
        """
        frac1 < frac2
        return boolean
        """
        frac1 = self.n / self.d
        frac2 = other.n / other.d

        return frac1.__lt__(frac2)

    def __gt__(self, other):
        """
        frac1 > frac2
        return boolean
        """
        frac1 = self.n / self.d
        frac2 = other.n / other.d

        return frac1.__gt__(frac2)

    def __str__(self):
        """
        return the fraction as a string
        """
        return f"{self.n}/{self.d}"


def main():

    frac1 = Fraction(9, 4)
    frac2 = Fraction(12, 6)

    complement = frac1.complement()

    reciprocal = frac1.reciprocal()

    product = frac1.multiply(frac2)

    quotient = frac1.divide(frac2)

    sum = frac1.add(frac2)

    difference = frac1.deduct(frac2)
    difference.simplify()

    frac1 < frac2
    frac1 > frac2

    print(sum)


if __name__ == "__main__":
    main()
