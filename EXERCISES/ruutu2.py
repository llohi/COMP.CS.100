"""
COMP.CS.100 Paranneltu ruudun tulostus
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def print_box(width, height, border_mark="#", inner_mark=" "):
    """ THIS FUNCTION PRINTS OUT THE BOX """
    for i in range(1, int(height) + 1):

        if i == 1 or i == int(height):
            print("{}".format(int(width) * border_mark))

        else:
            print("{0}{1}{0}".format(border_mark, (int(width) - 2) * inner_mark))
    print()


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
