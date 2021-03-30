"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 050800360
Name: Joose Lohi
Email: joose.lohi01@gmail.com

Tiedoston rivien numerointi
"""


def main():

    filename = input("Enter the name of the file: ")

    try:

        file = open(filename, mode="r")

    except OSError:

        print("There was an error in reading the file.")
        return

    i = 1

    for file_line in file:

        file_line = file_line.rstrip()
        print("{} {}".format(i, file_line))
        i += 1


if __name__ == "__main__":
    main()
