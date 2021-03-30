"""
COMP.CS.100 Pisin järjestetty alimerkkijono
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def longest_substring_in_order(str):
    """
    -> take str as input
    -> return longest substring in alphabetical order
    """

    substr = ""
    strings = []
    i = 0

    length = len(str)
    if length > 1:

        for i in range(0, length - 1):

            if str[i] < str[i + 1]:

                substr += str[i]

                if i + 1 == length - 1:

                    substr += str[i + 1]
                    strings.append(substr)

                else:

                    continue

            else:

                substr += str[i]
                strings.append(substr)
                substr = ""
                continue

        if len(strings) <= 1:

            longest = strings[0]

        else:

            longest = max(strings, key=len)

    elif str == "":

        longest = ""

    else:

        longest = str

    return longest


def main():

    str1 = longest_substring_in_order("abcdefghijk")
    print(str1)
    str2 = longest_substring_in_order("efghijklmnopopqefgabcdeabcdefghijklm")
    print(str2)


if __name__ == "__main__":
    main()
