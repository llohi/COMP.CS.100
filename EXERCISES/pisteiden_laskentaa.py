"""
COMP.CS.100 Pisteiden laskentaa
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def main():

    filename = input("Enter the name of the score file: ")

    # try opening file
    try:
        file = open(filename, mode="r")

    except OSError:
        print("There was an error in reading the file.")
        return

    scores = {}

    # try for erroneous lines
    for line in file:

        line = line.split()
        if len(line) == 2:
            pass
        else:
            print("There was an erroneous line in the file:\n{}".format(line[0]))
            return

        # try for erroneous score
        try:
            line[1] = int(line[1])

        except ValueError:
            print("There was an erroneous score in the file:\n{}".format(line[-1]))
            return

        # add items to dict
        if line[0] in scores:
            scores[line[0]] += line[1]

        else:
            scores[line[0]] = line[1]

    print(scores)
    print("Contestant score:")
    for i in sorted(scores):
        print("{} {}".format(i, scores[i]))


if __name__ == "__main__":
    main()
