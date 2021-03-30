"""
COMP.CS.100 Lukujonoja
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def main():

    print("Give 5 numbers:")
    x = 0
    list = []

    while x < 5:

        num = int(input("Next number: "))

        list.append(num)

        x += 1

    list.reverse()
    print("The numbers you entered, in reverse order: ")

    for i in list:

        print(i)


if __name__ == "__main__":
    main()
