"""
COMP.CS.100 Reverse the Names to Correct Order
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def reverse_name(str):
    """
    -> takes in string
    -> converts names into correct order
    """

    full_name = []
    str_split = str.split(",")

    for item in str_split:

        item = item.strip()
        full_name.append(item)

    if len(full_name) > 1:
        for i in full_name:
            if len(i) > 1:
                name = "{} {}".format(full_name[1], full_name[0])
            else:
                if full_name[0].isalpha() == True and full_name[1].isalpha() == True:
                    name = "{} {}".format(full_name[1], full_name[0])
                else:
                    new_full = []
                    for i in full_name:
                        if i.isalpha():
                            new_full.append(i)
                    if len(new_full) > 0:
                        name = "{}".format(new_full[0])
                    else:
                        name = ""
    else:
        name = "{}".format(full_name[0])

    return name


def main():

    reverse_name("x,y")


if __name__ == "__main__":
    main()
