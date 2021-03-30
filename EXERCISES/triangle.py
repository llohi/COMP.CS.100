"""
COMP.CS.100 Triangle's area
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""
from math import sqrt


def area(x, y, z):
    ''' CALCULATE THE AREA OF A TRIANGLE '''
    s = (x + y + z) / 2
    a = sqrt(s * (s - x) * (s - y) * (s - z))
    return a


def main():

    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))

    print("The triangle's area is {:.1f}".format(area(a, b, c)))


if __name__ == "__main__":
    main()
