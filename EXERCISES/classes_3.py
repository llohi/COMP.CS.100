"""
COMP.CS.100 Auto luokkana
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


class Car:
    """
    Class Car: Implements a car that moves a certain distance and
                whose gas tank can be filled.
    """

    def __init__(self, tank_size, gas_consumption):
        """
        :param tank_size: float
        :param gas_consumption: float
        """

        self.__tank_volume = tank_size
        self.__consumption = gas_consumption
        self.__gas = 0
        self.__distance = 0
        # calculate the range of car
        self.__range = 0

    def print_information(self):
        """
        Print the state of the car
        """
        print(
            f"The tank contains {self.__gas:.1f} liters of gas and the odometer shows {self.__distance:.1f} kilometers.")

    def fill(self, amount):
        """
        Fill the gas tank
        :param amount: float
        """

        # check for erroneous data
        if amount < 0:

            print("You cannot remove gas from the tank")
            return

        else:

            if self.__gas + amount <= self.__tank_volume:
                self.__gas += amount

            else:
                self.__gas = self.__tank_volume

            self.__range = self.__gas / (self.__consumption / 100)

    def drive(self, distance):
        """
        Drive the car to a certain distance
        :param distance: float
        """

        # check for erroneous data
        if distance < 0:

            print("You cannot trave a negative distance")
            return

        elif distance == 0:

            pass

        else:

            if distance < self.__range:

                self.__distance += distance
                self.__gas -= distance * (self.__consumption / 100)

            else:

                self.__distance += self.__range
                self.__gas = 0

        self.__range = self.__gas / (self.__consumption / 100)


def main():
    tank_size = read_number("How much does the vehicle's gas tank hold?")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers?")

    car = Car(tank_size, gas_consumption)

    while True:
        car.print_information()

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up?")
            car.fill(to_fill)

        elif choice == "2":
            distance = read_number("How many kilometers to drive?")
            car.drive(distance)

        elif choice == "3":
            print("Thank you and bye!")
            break


def read_number(prompt, error_message="Incorrect input!"):
    """
    :param prompt: str, prompt to be used when asking user input.
    :param error_message: str, what error message to print
        if the entered value is not a float.
    """

    while True:
        try:
            return float(input(prompt + " "))

        except ValueError:
            print(error_message)


if __name__ == "__main__":
    main()
