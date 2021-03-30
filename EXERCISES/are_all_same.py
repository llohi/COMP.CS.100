"""
COMP.CS.100 Funktio listan alkioiden yhtäsuuruusvertailuun
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def are_all_members_same(list):
    """
    -> check if all members of list have the same value
    -> return boolean
    """

    check = True

    for item in list:

        if len(list) == 0:

            check = None

        else:
            first = list[0]

            if first != item:

                check = False
                break

    return check


def main():

    list = []

    print(are_all_members_same(list))


if __name__ == "__main__":
    main()
