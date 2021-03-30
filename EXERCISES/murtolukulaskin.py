"""
COMP.CS.100 Murtolukulaskin
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

    def multiply(self, frac2):
        """
        Return the product of two fractions as an object of the class.
        -15/5 * 3/4 = -45/20
        :param frac2: <object class=Fraction>
        """

        n = self.n * frac2.n
        d = self.d * frac2.d

        return Fraction(n, d)


def main():

    fractions = {}

    # loop the command line
    while True:

        cmd = input("> ")

        # add fractions to dictionary
        if cmd == "add":

            frac = input("Enter a fraction in the form integer/integer: ")
            frac = frac.split("/")  # ['INT1', 'INT2']
            name = input("Enter a name: ")

            # {'NAME': <object class=Fraction>}
            fractions[name] = Fraction(int(frac[0]), int(frac[1]))

        # quit cmd line
        elif cmd == "quit":

            print("Bye bye!")
            break

        # print specific fraction
        elif cmd == "print":

            search = input("Enter a name: ")

            if search in fractions:

                print(f"{search} = {fractions[search]}")

            else:

                print(f"Name {search} was not found")

        # list all fractions
        elif cmd == "list":

            if len(fractions) == 0:
                pass

            else:
                for f in sorted(fractions):

                    print(f"{f} = {fractions[f]}")

        # multiply two fractions
        elif cmd == "*":

            x = input("1st operand: ")

            if x in fractions:
                x = fractions[x]
                y = input("2nd operand: ")

                # BOTH NAMES FOUND IN DICTIONARY
                if y in fractions:

                    y = fractions[y]

                    product = x.multiply(y)

                    print(f"{x} * {y} = {product}")
                    print(f"simplified {product.simplify()}")

                else:
                    print(f"Name {y} was not found")

            else:
                print(f"Name {x} was not found")

        # read file and add to dict
        elif cmd == "file":

            filename = input("Enter the name of the file: ")

            # TRY OPENING FILE
            run = True
            try:
                file = open(filename, mode="r")

            except OSError:
                print("Error: the file cannot be read.")
                run = False

            if run == True:

                # TEST FOR ERRORS WITHIN FILE
                for row in file:

                    if "=" and "/" in row:

                        row = row.split("=")  # ['NAME' 'FRACTION']

                        frac = row[1].split("/")  # ['INT1', 'INT2']

                        # {'NAME': <object class=Fraction>}
                        fractions[row[0]] = Fraction(int(frac[0]), int(frac[1]))

                    else:
                        print("Error: the file cannot be read.")
                        break

            else:
                pass

        else:

            print("Unknown command!")


if __name__ == "__main__":
    main()
