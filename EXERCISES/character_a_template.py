"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""


class Character:
    """
    A class that represents a character.
    """

    def __init__(self, name):
        """
        Initialize the character with following attributes.
        name: str
        items: list, items added in main function
        """

        self.name = name
        self.items = []

    def get_name(self):
        """
        Getter function to return the name of the object.
        """

        return self.name

    def printout(self):
        """
        Printout information regarding the character.
        Name: -- self.name --
          <amount> item
          <amount> item
        """

        # {'ITEM_NAME': int(HOW_MANY)}
        print_dict = {}

        for item in self.items:

            if item not in print_dict:

                print_dict[item] = self.items.count(item)

            else:

                pass

        # check if character has no items
        if len(print_dict) > 0:

            print(f'Name: {self.name}')

            for i in sorted(print_dict):
                print(f'  {print_dict[i]} {i}')

        else:

            print(f'Name: {self.name}\n  --nothing--')

    def give_item(self, item):
        """
        Add the item given to the characters items list.
        """
        self.items.append(item)

    def remove_item(self, item):
        """
        Remove given item from the list.
        """
        if item in self.items:
            self.items.remove(item)

        else:
            pass

    def has_item(self, item):
        """
        Method to check if item is in list.
        return boolean
        """

        if item in self.items:

            return True

        else:

            return False

    def how_many(self, item):
        """
        Method to count how many instances of the item are included in the list.
        return int
        """

        count = self.items.count(item)
        return count


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
