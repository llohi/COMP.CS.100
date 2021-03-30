"""
COMP.CS.100 A Function for Reviewing a List's Order of Magnitude
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def is_the_list_in_order(list):
    """
    -> check if items in list are in order
    -> return boolean
    """

    check = True

    for i in range(0, len(list) - 1):

        if len(list) == 0:

            check = None
            break

        elif list[i] > list[i + 1]:

            check = False
            break

    return check


def main():

    list = [1, 2, 3, 4]
    bool = is_the_list_in_order(list)

    print(bool)


if __name__ == "__main__":
    main()
