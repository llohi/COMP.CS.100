"""
COMP.CS.100 Tulostetaan ruutu
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def print_box(x, y, z):
    ''' THIS FUNCTION PRINTS OUT THE BOX '''
    for i in range(1, int(y) + 1):
        print("{}".format(int(x) * z))


def main():
    width = input("Enter the width of a frame: ")
    height = input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")

    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
