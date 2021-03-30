"""
COMP.CS.100 TGIF
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def main():

    def fridays():

        day = 1
        month = 1
        # list of all dates in the year
        dates = []

        # months with thirty days in them
        def thirty(x):
            for days in range(1, 31):
                date = "{}.{}.".format(days, x)
                dates.append(date)
        # months with thirtyone days in them

        def thirtyone(x):
            for days in range(1, 32):
                date = "{}.{}.".format(days, x)
                dates.append(date)

        # increment the month
        for i in range(1, 13):

            # january
            if month == 1:
                thirtyone(month)

            # february
            elif month == 2:
                for days in range(1, 29):
                    date = "{}.{}.".format(days, month)
                    dates.append(date)

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

        # print the dates of all fridays starting with 3.1.
        print(dates[2])
        for i in range(1, 365 // 7):
            print(dates[2 + 7 * i])

    fridays()


if __name__ == "__main__":
    main()
