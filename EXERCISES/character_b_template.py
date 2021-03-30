"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game.
"""


class Character:
    """
    This class defines what a character is in the game and what
    he or she can do.
    """

    def __init__(self, name, hitpoints):
        """
        Initialize the character with following attributes.
        name: str
        hitpoints: int
        items: list, items added in main function
        """

        self.name = name
        self.hitpoints = hitpoints
        self.items = {}  # {'ITEM_NAME': ITEM_DAMAGE}
        self.items_count = {}  # {'ITEM_NAME': ITEM_COUNT}

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

        # check if character has no items
        if len(self.items) > 0:

            print(f'Name: {self.name}')
            print(f'Hitpoints: {self.hitpoints}')

            for i in sorted(self.items):

                if self.items_count[i] > 0:
                    print(f'  {self.items_count[i]} {i}')

                else:
                    pass

        else:

            print(f'Name: {self.name}\n  --nothing--')

    def give_item(self, item):
        """
        Add the item given to the characters items dictionary.
        """

        if item not in self.items:

            # check if item is a weapon
            if item in WEAPONS:
                self.items[item] = WEAPONS[item]
                self.items_count[item] = 1

            else:
                self.items[item] = 0
                self.items_count[item] = 1
        else:
            self.items_count[item] += 1

    def remove_item(self, item):
        """
        Remove given item from the dict.
        """

        def remove_item(self, item):
            """
            Remove given item from the list.
            """
            if item in self.items:
                self.items.pop(item)

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

        if item in self.items_count:
            count = self.items_count[item]

        else:
            count = 0

        return count

    def pass_item(self, item, target):
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """

        if item in self.items:

            target.give_item(item)
            self.items_count[item] -= 1
            return True

        else:

            return False

    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """

        # unknown weapon
        if weapon not in WEAPONS:

            print(f'Attack fails: unknown weapon \"{weapon}\".')
            return False

        # weapon not owned
        elif weapon not in self.items:

            print(f'Attack fails: {self.name} doesn\'t have \"{weapon}\".')
            return False

        # weapon cound 0
        elif self.items_count[weapon] == 0:

            print(f'Attack fails: {self.name} doesn\'t have \"{weapon}\".')
            return False

        # tries to attack him/herself
        elif target == self:

            print(f'Attack fails: {self.name} can\'t attack him/herself.')
            return False

        # check if target is already dead
        if target.hitpoints <= 0:
            return False

        # character survives attack
        elif target.hitpoints - self.items[weapon] > 0:
            target.hitpoints -= self.items[weapon]
            print(f'{self.name} attacks {target.name} delivering {self.items[weapon]} damage.')
            return True

        # character drops dead
        elif target.hitpoints - self.items[weapon] <= 0:
            target.hitpoints -= self.items[weapon]
            print(f'{self.name} attacks {target.name} delivering {self.items[weapon]} damage.')
            print(f'{self.name} successfully defeats {target.name}.')
            return True


WEAPONS = {
    # Weapon          Damage
    # --------------   ------
    "elephant gun":     15,
    "gun":               5,
    "light saber":      50,
    "sword":             7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)

    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()

    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword")  # Conan doesn't have a sword.
    conan.attack(conan, "gun")      # A character is not allowed to attack himself.
    conan.attack(conan, "pen")      # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")   # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword")  # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
