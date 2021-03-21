"""
COMP.CS.100 Auto
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""

import math


def menu():
    """
    TEXT BASED MENU FOR THE SIMULATION
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0  # Current X coordinate of the car
    y = 0  # Current Y coordinate of the car

    while True:

        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x, y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tank, request, gas):
    """
    -> amount of gas in the tank AFTER the filling up
    """
    if request <= tank - gas:
        gas += request
        return gas
    else:
        gas = tank
        return gas


def drive(x, y, new_x, new_y, gas, gas_consumption):
    """
    -> The amount of gas in the tank AFTER the driving
    -> The reached (new) x and y coordinates
    """

    # gas after drive = gas before - consumption / distance
    if gas - distance(x, y, new_x, new_y) * gas_consumption / 100 >= 0:
        gas -= distance(x, y, new_x, new_y) * gas_consumption / 100
        x = new_x
        y = new_y
    else:
        gas, x, y = new_distance(
            x, y, new_x, new_y, gas, gas_consumption)

    return gas, x, y


def distance(x, y, new_x, new_y):
    """ THIS FUNCTION CALCULATES THE DISTANCE TRAVELED USING THE PYTHAGOREAN THEOREUM """
    distance = math.sqrt((new_x - x) ** 2 + (new_y - y) ** 2)
    return distance


def new_distance(x, y, new_x, new_y, gas, gas_consumption):
    """
    THIS IS A FUNCTION TO CREATE NEW DISTANCE IF GAS IS N0T SUFFICIENT
    """
    CONSTANT = (gas / gas_consumption * 100) / distance(x, y, new_x, new_y)
    x += CONSTANT * (new_x - x)
    y += CONSTANT * (new_y - y)
    gas = 0
    return gas, x, y


def read_number(prompt, error_message="Incorrect input!"):
    """ THIS IS A FUNCTION TO PROMPT FLOAT NUMBERS FROM THE USER """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
