"""
COMP.CS.100 Areas
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""

import math


def result(x, y):
    """ FUNCTION TO PRINT THE RESULT """

    return "The circumference is {:.2f}\nThe surface area is {:.2f}".format(x, y)


def calc_circumference(x, y):
    """ CALCULATE THE CIRCUMFERENCE OF SHAPE """
    circumference = x * y
    return circumference


def calc_area(x, y):
    """ CALCULATE THE AREA OF SHAPE """
    area = x * y
    return area


def square():
    """ GET DATA FOR SQUARE """
    run = True
    while run:

        x = float(input("Enter the length of the square's side: "))

        if x > 0:
            run = False

        else:
            pass

    print(result(calc_circumference(x, 4), calc_area(x, x)))


def rectangle():
    """ GET DATA FOR RECTANGLE """

    run = True
    while run:

        x = float(input("Enter the length of the rectangle's side 1: "))
        if x > 0:
            side_two = True

            while side_two:

                y = float(input("Enter the length of the rectangle's side 2: "))
                if y > 0:
                    side_two = False

                else:
                    pass

            run = False

    print(result(calc_circumference(2, (x + y)), calc_area(x, y)))


def circle():
    """ GET DATA FOR CIRLE USING PI """
    run = True
    while run:

        x = float(input("Enter the circle's radius: "))

        if x > 0:
            run = False

        else:
            pass

    print(result(calc_circumference(2 * math.pi, x), calc_area(math.pi, x ** 2)))


def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        if answer == "s":
            square()

        elif answer == "r":
            rectangle()

        elif answer == "c":
            circle()

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        # Empty row for the sake of readability.
        print()


def main():
    menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()
