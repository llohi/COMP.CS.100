"""
COMP.CS.100 Kertotaulu yli sata
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def main():

    num = int(input("Choose a number: "))
    x = 1
    run = True

    while run:
        if (x * num) - num < 100:
            print("{0} * {1} = {2}".format(x, num, x * num))
            x += 1
        else:
            run = False


if __name__ == "__main__":
    main()
