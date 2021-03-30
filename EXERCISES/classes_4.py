"""
COMP.CS.100 Auto luokkana
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


class Player:
    """
    Create a type of player
    """

    def __init__(self, name):
        """
        :param name: str
        """

        self.__name = name
        self.__points = 0
        self.__all_points = []
        self.__hits = 0
        self.__accuracy = 0

    def get_name(self):
        """
        return the name of the player
        """
        return self.__name

    def get_points(self):
        """
        return the poitns of the player
        """
        return self.__points

    def get_accuracy(self):
        """
        return the accuracy of the player
        """
        return self.__accuracy

    def add_points(self, pts):
        """
        add points
        check points
        execute proper reaction to points
        """

        self.__points += pts
        self.__all_points.append(pts)
        average = sum(self.__all_points) / len(self.__all_points)

        # if points > 0, append accuracy by one
        # accuracy = throws / hits
        if pts > 0:
            self.__hits += 1
            self.__accuracy = self.__hits / len(self.__all_points)

        else:

            self.__accuracy = self.__hits / len(self.__all_points)

        # > 50 points  ->  points == 25
        if self.__points > 50:

            print(f"{self.__name} gets penalty points!")
            self.__points = 25

        elif 40 <= self.__points <= 49:

            print(f"{self.__name} needs only {50 - self.__points} points. It's better to avoid knocking down the pins with higher points.")

        # execute "Cheers NAME" if points > average of all points
        if pts > average:

            print(f"Cheers {self.__name}!")

    def has_won(self):
        """
        check if points == 50
        return boolean
        """
        if self.__points == 50:
            return True

        else:
            return False


def main():

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, hit percentage {player1.get_accuracy() * 100:.1f}")
        print(f"{player2.get_name()}: {player2.get_points()} p, hit percentage {player2.get_accuracy() * 100:.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
