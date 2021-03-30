"""
COMP.CS.100 Murtolukulista
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

    def __str__(self):
        """
        return the fraction as a string
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
        denom = gcd(self.n, self.d)
        n = self.n // denom
        d = self.d // denom

        return Fraction(n, d)


def main():

    print("Enter fractions in the format integer/integer.")
    print("One fraction per line. Stop by entering an empty line.")

    fractions = []

    while True:

        frac = input()

        if frac != "":

            frac = frac.split("/")
            frac = Fraction(int(frac[0]), int(frac[-1]))
            fractions.append(frac)

        else:

            break

    print("The given fractions in their simplified form:")
    for f in fractions:

        print(f"{f} = {f.simplify()}")


if __name__ == "__main__":
    main()
