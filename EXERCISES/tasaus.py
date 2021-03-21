"""
COMP.CS.100 Tekstin tasaus
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def read_user():
    """
    read user input
    seperate all words into a list
    return list of words and list of rows
    """

    word_list = []
    org_text = []

    while True:

        row = input("")

        if row != "":

            org_text.append(row)
            row = row.split(" ")

            for word in row:

                # avoid errors with .split(" ")
                if word != "":

                    word = word.strip()
                    word_list.append(word)

                else:

                    pass

        else:

            break

    return word_list, "\n".join(org_text)


def calculate_rows(text, length):
    """
    calculate how many rows needed
    :param text: list, original text in a list of rows
    :param length: int, num given by user
    """

    # length of all characters including spaces
    all_chars = 0

    for row in text:
        all_chars += len(row)

    if all_chars % length == 0:
        rows = all_chars // length

    else:
        rows = (all_chars // length) + 100  # 5, just incase words don't fit

    return rows


def get_rows(words, length, rows):
    """
    :param words: list
    :param length: int, length of row
    :param rows: int, number of rows
    """

    # rows are managed in following format:
    # { ROW X: [ "WORD_1 ", "WORD_2 ", "WORD_3" ] }
    dict_rows = {}

    for i in range(1, rows + 1):

        dict_rows[f"row {i}"] = []

    # length of all characters in row
    row_chars = 0
    i = 1

    for word in words:

        if row_chars + len(word) + 1 <= length:

            dict_rows[f"row {i}"].append(word + " ")
            row_chars += len(word) + 1

        # check if the word fits as last word without space
        elif row_chars + len(word) <= length:

            dict_rows[f"row {i}"].append(word)
            row_chars += len(word)

        else:

            i += 1
            row_chars = 0
            dict_rows[f"row {i}"].append(word + " ")
            row_chars += len(word) + 1

    # check for empty rows  ->  isolate
    dict_rows_clean = {}
    for row in dict_rows:

        if len(dict_rows[row]) != 0:

            dict_rows_clean[row] = dict_rows[row]

    return dict_rows_clean


def even_text(rows, length):
    """
    :param rows: dict, dictionary of all the rows in text
    :param length: int
    return clean text
    """

    spaces = {}
    # loop over rows
    for row in rows:

        # variable for all room that must be filled
        empty_space = 0
        chars = 0

        # get rid of space after last word of the row
        try:
            if rows[row][-1][-1] == " ":

                rows[row][-1] = rows[row][-1].strip()

        except IndexError:
            str = "*"
            print(f"{str * 10}\tINDEX ERROR\t{str * 10}")
            print(f"{row}:", end="\t")
            print(rows[row])
            return

        for word in rows[row]:

            chars += len(word)

        empty_space = length - chars
        spaces[row] = empty_space

    # add spaces to words according to num of empty spaces
    # add joined rows to new list of rows
    rows_new = []

    for row in rows:

        # check if last row of text  ->  pass
        if row == f"row {len(rows)}":
            pass

        else:

            i = 0
            index = 0

            # if there is only one word in the row,
            # we don't want to touch in at all
            if len(rows[row]) > 1:

                while i < spaces[row]:

                    # make sure not the last word of row
                    try:

                        if rows[row][index] != rows[row][-1]:
                            rows[row][index] += " "

                        else:
                            index = 0
                            rows[row][index] += " "

                    except IndexError:

                        str = "*"
                        print(f"{str * 10}\tINDEX ERROR\t{str * 10}")
                        print(f"{row}:", end="\t")
                        print(rows[row])
                        return

                    i += 1
                    index += 1

                else:
                    pass

        rows_new.append("".join(rows[row]))

    # join all rows into a clean text
    text = "\n".join(rows_new)
    return text


def main():

    print("Enter text rows. Quit by entering an empty row.")

    # get list of all words and original text
    words, text = read_user()

    # get length per row and calculate how many rows required
    length = int(input("Enter the number of characters per line: "))
    num_of_rows = calculate_rows(text, length)

    # create text
    rows = get_rows(words, length, num_of_rows)
    text_clean = even_text(rows, length)
    print(text_clean)


if __name__ == "__main__":
    main()
