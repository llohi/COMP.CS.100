"""
COMP.CS.100 Bussiaikataulu
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def give_time(t):
    """
    -> compare time to timetable
    -> return three next times
    """

    timetable = [630, 1015, 1415, 1620, 1720, 2000]
    print("The next buses leave:")

    for i in range(0, len(timetable)):

        if t > timetable[-1]:

            print("{0}\n{1}\n{2}".format(timetable[0], timetable[1], timetable[2]))
            break

        elif t <= timetable[i]:

            if i < 4:

                print("{0}\n{1}\n{2}".format(timetable[i], timetable[i + 1], timetable[i + 2]))

            elif i == 4:

                print("{0}\n{1}\n{2}".format(timetable[i], timetable[i + 1], timetable[0]))

            elif i == 5:

                print("{0}\n{1}\n{2}".format(timetable[i], timetable[0], timetable[1]))

            break


def main():

    time = int(input("Enter the time (as an integer): "))
    give_time(time)


if __name__ == "__main__":
    main()
