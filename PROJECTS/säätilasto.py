"""
COMP.CS.100 Säätilasto
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def calc_mean(list):
    """
    -> list of temperatures as parameter
    -> calculate the mean of list
    -> return mean
    """
    mean = sum(list) / len(list)

    return mean


def calc_median(list):
    """
    -> list of temperatures as parameter
    -> calculate the median of list
    -> return median
    """
    list = sorted(list)

    if len(list) % 2 == 0:

        index = int(len(list) / 2)
        median = (list[index - 1] + list[index]) / 2

    else:

        index = int(len(list) / 2 - 0.5)
        median = list[index]

    return median


def divide_temps(list, median):
    """
    -> divide list based on median
    -> return two lists
    """
    under = []
    over = []

    for temp in list:

        if temp < median:
            under.append(temp)

        else:
            over.append(temp)

    return under, over


def calc_diff(temp, mean):
    """
    -> calculate the difference between the
       given temperature and mean
    """
    diff = round(temp - mean, 1)
    return diff


def main():

    all_temps = []
    dates = {}
    days = int(input("Enter amount of days: "))

    # input temperatures to list
    for i in range(1, days + 1):

        temp = float(input("Enter day {}. temperature in Celcius: ".format(i)))
        all_temps.append(temp)
        dates[temp] = i

    mean = round(calc_mean(all_temps), 1)
    median = round(calc_median(all_temps), 1)

    print("\nTemperature mean: {:.1f}C\nTemperature median: {:.1f}C\n".format(mean, median))

    # define lists for temperatures
    under, over = divide_temps(all_temps, median)

    # print temperatures over or at median
    print("Over or at median were:")

    for temp in over:

        index = dates.get(temp)
        diff = calc_diff(temp, mean)
        print("Day{0:>3}.{1:>6}C difference to mean:{2:>6}C".format(index, temp, diff))

    # print temperatures under median
    print("\nUnder median were:")

    for temp in under:

        index = dates.get(temp)
        diff = calc_diff(temp, mean)
        print("Day{0:>3}.{1:>6}C difference to mean:{2:>6}C".format(index, temp, diff))


if __name__ == "__main__":
    main()
