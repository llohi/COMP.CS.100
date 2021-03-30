"""
COMP.CS.100 Liukulukujen (desimaalilukujen) vertaileminen
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def compare_floats(x, y, EPSILON):
    ''' COMPARE TWO FLOAT NUMBERS INCLUDING EPSILON '''
    value = abs(x - y) < EPSILON
    return value


def main():
    x = 0.0001
    y = 0.0002
    eps = 1e-9
    print("{}".format(compare_floats(x, y, eps)))


if __name__ == "__main__":
    main()
