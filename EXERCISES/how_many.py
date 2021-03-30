"""
COMP.CS.100 Montako löytyy?
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def input_to_list(x):
    """
    -> create lsit
    -> input data to list
    -> return list
    """

    print("Enter {} numbers:".format(x))

    list = []
    count = 0

    while count < x:

        number = int(input(""))
        list.append(number)

        count += 1

    return list


def main():

    x = int(input("How many numbers do you want to process: "))

    list = input_to_list(x)

    y = int(input("Enter the number to be searched: "))

    if y in list:
        print("{0} shows up {1} times among the numbers you have entered.".format(y, list.count(y)))

    else:
        print("{} is not among the numbers you have entered.".format(y))


if __name__ == "__main__":

    main()
