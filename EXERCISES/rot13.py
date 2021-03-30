"""
COMP.CS.100 Kokonaisen viestin ROT-13-salaus
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""

REGULAR_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ENCRYPTED_CHARS = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                   'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']


def read_message():
    """
    -> read user input and turn into uppercase
    """

    run = True
    msg = []

    while run:

        line = input("")

        if len(line) > 0:

            msg.append(line)

        else:

            run = False

    return msg


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

    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()
    msg_encrypt = []

    for line in msg:

        if len(line) > 1:

            line = row_encryption(line)
            msg_encrypt.append(line)

        else:

            line = encrypt(line)
            msg_encrypt.append(line)

    print("ROT13:")
    print("\n".join(msg_encrypt))


if __name__ == "__main__":
    main()
