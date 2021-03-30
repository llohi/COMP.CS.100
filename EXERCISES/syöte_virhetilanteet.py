"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 050800360
Name: Joose Lohi
Email: joose.lohi01@gmail.com

Syötteenluvun virhetilanteet
"""


def read_input():
    """
    -> test if input is the correct value
    """

    run = True
    while run:

        width_str = input("Enter the width of a frame: ")

        try:
            width = int(width_str)

            try_height = True
            while try_height:
                height_str = input("Enter the height of a frame: ")
                try:
                    height = int(height_str)
                    try_height = False

                except ValueError:
                    pass

            try_mark = True
            while try_mark:
                mark_str = input("Enter a print mark: ")
                if mark_str == "" or mark_str.isspace() == True:
                    pass

                else:
                    mark = mark_str
                    try_mark = False

            run = False

        except ValueError:
            pass

    return width, height, mark


def main():

    width, height, mark = read_input()
    print()

    for i in range(0, height):

        print("{}".format(mark * width))


if __name__ == "__main__":
    main()
