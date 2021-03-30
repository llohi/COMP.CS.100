"""
COMP.CS.100 Akronyymin muodostaminen
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def create_an_acronym(str):
    """
    -> create an acronym of a word
    """
    if len(str) == 1:

        acronym = str.upper()

    else:

        str = str.split(" ")

        for word in str:
            word = word.strip()

        for item in str:

            if item.isalpha() == False:
                str.remove(item)

            elif item == "":
                str.remove(item)

            else:
                pass

        letters = []
        for item in str:
            letters.append(item[0].upper())

        acronym = "".join(letters)

    return acronym


def main():

    create_an_acronym("central intelligence agency")


if __name__ == "__main__":
    main()
