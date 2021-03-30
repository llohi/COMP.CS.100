"""
COMP.CS.100 Vuoden päivämäärät
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def main():

    day = 1
    month = 1

    def thirty(x):
        for days in range(1, 31):
            print("{}.{}.".format(days, x))

    def thirtyone(x):
        for days in range(1, 32):
            print("{}.{}.".format(days, x))

    # increment the month
    for i in range(1, 13):

        # january
        if month == 1:
            thirtyone(month)

        # february
        elif month == 2:
            for days in range(1, 29):
                print("{}.{}.".format(days, month))

        # march
        elif month == 3:
            thirtyone(month)

        # april
        elif month == 4:
            thirty(month)

        # may
        elif month == 5:
            thirtyone(month)

        # june
        elif month == 6:
            thirty(month)

        # july
        elif month == 7:
            thirtyone(month)

        # august
        elif month == 8:
            thirtyone(month)

        # september
        elif month == 9:
            thirty(month)

        # october
        elif month == 10:
            thirtyone(month)

        # november
        elif month == 11:
            thirty(month)

        # december
        elif month == 12:
            thirtyone(month)

        month += 1


if __name__ == "__main__":
    main()
