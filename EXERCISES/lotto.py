"""
COMP.CS.100 Lotto pelejä
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def factorial(num):
    ''' RETURN THE FACTORIAL OF A GIVEN NUMBER '''
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f


def calc_chance(x, y):
    ''' CALCULATE THE CHANCE TO WIN THE LOTTERY '''

    numerator = factorial(x)
    denominator = factorial(x - y) * factorial(y)

    print("The probability of guessing all {} balls correctly is 1/{:.0f}".format(y, numerator / denominator))


def main():

    n = int(input("Enter the total number of lottery balls: "))
    p = int(input("Enter the number of the drawn balls: "))

    if n <= 0:
        print("The number of balls must be a positive number.")

    elif p > n:
        print("At most the total number of balls can be drawn.")

    else:
        calc_chance(n, p)


if __name__ == "__main__":
    main()
