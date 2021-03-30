"""
COMP.CS.100 Bored (Error testing)
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def main():

    run = True

    while run:

        answer = input("Bored? (y/n) ")

        if answer == "y":
            print("Well, let's stop this, then.")
            run = False
        elif answer == "Y":
            print("Well, let's stop this, then.")
            run = False
        elif answer == "n":
            pass
        elif answer == "N":
            pass

        else:
            print("Incorrect entry.")


if __name__ == "__main__":
    main()
