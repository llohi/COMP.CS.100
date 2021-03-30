"""
COMP.CS.100 Arvosanojen korvaus
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def convert_grades(list):
    """
    -> convert grades nonzero to six
    """

    for num in list:

        if num > 0:

            index = list.index(num)
            list.remove(num)
            list.insert(index, 6)

        else:

            pass


def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
