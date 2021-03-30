"""
COMP.CS.100 TV-sarjan valitseminen
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    TODO: comment the parameter and the return value.
    """

    data = {}

    try:
        file = open(filename, mode="r")

        for row in file:

            # seperate series and genres from file
            name, genres = row.rstrip().split(";")

            genres = genres.split(",")

            data[name] = genres

        file.close()
        return data

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")

    genre_data = read_file(filename)

    genres = []
    for name in genre_data:
        for genre in genre_data[name]:

            if genre not in genres:
                genres.append(genre)

    print("Available genres are: {}".format(", ".join(sorted(genres))))
    run = True
    while run:
        genre = input("> ")

        if genre == "exit":
            return

        for name in sorted(genre_data):
            if genre in genre_data[name]:

                print(name)


if __name__ == "__main__":
    main()
