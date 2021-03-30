"""
COMP.CS.100 Isot alkukirjaimet paikoilleen
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def capitalize_initial_letters(str):
    """
    -> take string as input
    -> capitalize first letter
    -> make other letters lowercase
    """

    # create seperate instance if string is one chr long
    if len(str) == 1:

        str = str.upper()

    else:

        str = str.split(" ")
        letters = []

        if len(str) < 2:

            for word in str:

                for i in range(0, len(word)):

                    if i == 0:
                        x = word[i].upper()
                        letters.append(x)

                    else:
                        x = word[i].lower()
                        letters.append(x)

            str = "".join(letters)

        else:

            words = []
            for word in str:

                for i in range(0, len(word)):

                    if i == 0:
                        x = word[i].upper()
                        letters.append(x)

                    else:
                        x = word[i].lower()
                        letters.append(x)

                words.append("".join(letters))
                letters.clear()

            str = " ".join(words)
    return str


def main():

    print(capitalize_initial_letters("hEllo wOrld"))


if __name__ == "__main__":
    main()
