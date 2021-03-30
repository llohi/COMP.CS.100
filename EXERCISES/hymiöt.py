# COMP.CS.100 Hymiöt
# Tekijä: Joose Lohi
# Opiskelijanumero: 050800360


def main():

    x = int(input("How do you feel? (1-10) "))

    if x < 1 or x > 10:
        print("Bad input!")

    else:

        if 7 < x < 10:
            smiley = ":-)"

        elif 1 < x < 4:
            smiley = ":-("

        elif x == 10:
            smiley = ":-D"

        elif x == 1:
            smiley = ":'("

        else:
            smiley = ":-|"

        print("A suitable smiley would be {}".format(smiley))


main()
