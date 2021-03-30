"""
COMP.CS.100 Rubikin kuutio -kilpailut
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def calculate(list):
    """
    -> remove best and worst time
    -> calculate average
    -> return average
    """

    list = sorted(list)
    list.remove(list[0])
    list.remove(list[-1])

    average = sum(list) / len(list)
    return average


def main():

    list = []

    for i in range(1, 6):

        score = float(input("Enter the time for performance {}: ".format(i)))
        list.append(score)

    final_score = round(calculate(list), 3)

    print("The official competition score is {:.2f} seconds.".format(final_score))


if __name__ == "__main__":
    main()
