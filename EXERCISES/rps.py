# COMP.CS.100 Kivi-paperi-sakset
# Tekijä: Joose Lohi
# Opiskelijanumero: 050800360


def main():
    x = input("Player 1, enter your choice (R/P/S): ")
    y = input("Player 2, enter your choice (R/P/S): ")

    if x == y:
        print("It's a tie!")
    elif x == "R" and y == "P":
        print("Player 2 won!")
    elif x == "R" and y == "S":
        print("Player 1 won!")
    elif x == "P" and y == "R":
        print("Player 1 won!")
    elif x == "P" and y == "S":
        print("Player 2 won!")
    elif x == "S" and y == "R":
        print("Player 2 won!")
    elif x == "S" and y == "P":
        print("Player 1 won!")


main()
