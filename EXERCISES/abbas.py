"""
COMP.CS.100 How many abbas?
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def count_abbas(str):
    """
    -> count occurences of str "abba" in input str
    """

    count = 0

    for i in range(0, len(str)):

        if str[i: i + 4] == "abba":

            count += 1

        else:
            pass

    return count


def main():

    count = count_abbas("abbabbabba")
    print(count)


if __name__ == "__main__":
    main()
