"""
COMP.CS.100 Yhteystiedot
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def read_file(filename):
    """
    -> correctly read information from given file
    """

    try:
        file = open(filename, mode="r")

    except OSError:
        print("Error opening {}".format(filename))

    data = {}

    first_line = file.readline()
    first_line = first_line.rstrip().split(";")
    first_line.remove("key")  # ['name', 'phone', 'email', 'skype']

    i = 0

    for line in file:

        line = line.rstrip().split(";")

        i += 1

        info = {}
        j = 1
        for key in first_line:

            info[key] = line[j]
            j += 1

        data[line[0]] = info

    return data


def main():

    info = read_file("/Users/jooselohi/github/COMP.CS.100/EXERCISES/ASSETS/contacts.csv")
    print(info["Tom"]["phone"])


if __name__ == "__main__":
    main()
