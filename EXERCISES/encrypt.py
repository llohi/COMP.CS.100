"""
COMP.CS.100 Yhden rivin ROT-13-salaus
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


REGULAR_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ENCRYPTED_CHARS = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                   'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']


def encrypt(chr):
    """
    -> take character as input
    -> encrypt character using list indexes
    """

    if chr.isalpha() == True:

        if chr.islower() == True:

            index = REGULAR_CHARS.index(chr)
            chr = ENCRYPTED_CHARS[index]

        else:

            index = REGULAR_CHARS.index(chr.lower())
            chr = ENCRYPTED_CHARS[index].upper()

    else:
        pass

    return chr


def row_encryption(str):
    """
    -> take string as input
    -> change characters using list indexes
    -> return encrypted string
    """

    chars = []

    for chr in str:

        if chr.isalpha() == True:

            if chr.islower() == True:
                index = REGULAR_CHARS.index(chr)
                chr = ENCRYPTED_CHARS[index]
                chars.append(chr)

            else:
                index = REGULAR_CHARS.index(chr.lower())
                chr = ENCRYPTED_CHARS[index].upper()
                chars.append(chr)
        else:
            chars.append(chr)

    return "".join(chars)


def main():

    encrypt("J")
    row_encryption("Hello World!")


if __name__ == "__main__":
    main()
