"""
COMP.CS.100 Tulosteen leveyden asettaminen
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def main():
    for i in range(1, 11):
        for j in range(1, 11):
            print("{0:>4}".format(i*j), end="")
        print()


if __name__ == "__main__":
    main()
