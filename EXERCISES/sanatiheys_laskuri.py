"""
COMP.CS.100 Sanatiheys laskuri
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def main():

    print("Enter rows of text for word counting. Empty row to quit.")
    rows = []
    keys_dict = {}

    run = True
    while run:

        row = input("")

        if row == "":
            run = False

        else:
            rows.append(row.split())

    for row in rows:
        for key in row:

            key = key.lower()
            if key in keys_dict:
                keys_dict[key] += 1

            else:
                keys_dict[key] = 1

    for key in sorted(keys_dict):
        print("{} : {} times".format(key, keys_dict[key]))


if __name__ == "__main__":
    main()
