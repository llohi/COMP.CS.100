"""
COMP.CS.100 Triangle's angle
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def calculate_angle(a, b=90):
    """ CALCULATE THE FINAL ANGLE OF THE TRIANGLE """
    c = 180 - a - b
    return c


def main():

    print(calculate_angle(50, 60))
    print(calculate_angle(50))


if __name__ == "__main__":
    main()
