"""
COMP.CS.100 Zip Boing
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def main():

    num = int(input("How many numbers would you like to have? "))

    for n in range(1, num + 1):

        if n % 3 == 0 and n % 7 != 0:
            print("zip")

        elif n % 7 == 0 and n % 3 != 0:
            print("boing")

        elif n % 3 == 0 and n % 7 == 0:
            print("zip boing")

        else:
            print(n)


if __name__ == "__main__":
    main()
