"""
COMP.CS.100 Yogi Bear
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def repeat_name(x, y):
    ''' THIS FUNCTION REPEATS THE NAME '''
    for i in range(1, y + 1):
        print("{0}, {0} Bear".format(x))


def verse(str, name):
    ''' THIS FUNCTION PRINTS THE ENTIRE VERSE '''
    print(str)
    print("{0}, {0}".format(name))
    print(str)
    repeat_name(name, 3)
    print(str)
    repeat_name(name, 1)


def main():

    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")


if __name__ == "__main__":
    main()
