"""
COMP.CS.100 Numeroitujen rivien kirjoittaminen tiedostoon
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def main():

    filename = input("Enter the name of the file: ")

    try:

        save_file = open(filename, mode="w")
        print("Enter rows of text. Quit by entering an empty row.")

    except OSError:

        print("Writing the file {} was not successful.".format(filename))
        return

    i = 0
    run = True
    while run:

        row = input()

        if row == "":
            print("File {} has been written.".format(filename))
            run = False

        else:
            i += 1
            print("{} {}".format(i, row), file=save_file)


if __name__ == "__main__":
    main()
