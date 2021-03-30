"""
COMP.CS.100 Vokaalit ja konsonantit
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def main():

    str = input("Enter a word: ")

    vowels = ["a", "e", "i", "o", "u", "y"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l",
                  "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

    vow_count = 0
    cons_count = 0

    for chr in str:
        if chr in vowels:
            vow_count += 1
        else:
            cons_count += 1

    print("The word \"{}\" contains {} vowels and {} consonants.".format(str, vow_count, cons_count))


if __name__ == "__main__":
    main()
