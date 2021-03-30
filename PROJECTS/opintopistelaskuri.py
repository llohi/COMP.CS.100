"""
COMP.CS.100 Opintopistelaskuri
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def main():

    months = int(input("Enter the number of months: "))
    x = 1
    credits = []
    # number of months without credits
    breaks = 0

    # append monthly credits to list
    while breaks < 2 and x <= months:

        credit = int(input("Enter the number of credits in month {}: ".format(x)))

        if breaks > 0:
            if credit > 0:
                credits.append(credit)
                breaks = 0
            else:
                breaks += 1

        else:
            if credit > 0:
                credits.append(credit)

            else:
                breaks += 1
                credits.append(credit)

        x += 1

    # 2 study breaks -> end program
    # less than 2 study breaks -> calculate average of list -> print correct outcome
    if breaks == 2:
        print("\nYou did have too many study breaks!")
    else:
        # round to 2 decimal places
        avg_calc = round(sum(credits) / len(credits), 2)
        avg_clean = float("{:.1f}".format(avg_calc))
        if avg_clean >= 5:
            print("\nYou are a full time student and your monthly credit point average is {}.".format(avg_clean))

        else:
            print("\nYour monthly credit point average {} does not classify you as a full time student.".format(
                avg_clean))


if __name__ == "__main__":
    main()
