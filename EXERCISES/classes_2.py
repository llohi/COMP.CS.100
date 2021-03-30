"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Template for the product assignment.
"""


class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, name, price):
        """
        A product is initialized with a name, price and sale%.
        :param name: str
        :param price: int
        :param pc: float
        """
        self.__name = name
        self.__price = price
        self.__percentage = 0

    def set_sale_percentage(self, x):
        """
        Alter the sale percentage
        """
        self.__percentage = x * 0.01
        return self.__percentage

    def printout(self):
        """
        Prints out data on product
        """
        print("{}".format(self.__name))
        print("  price: {:.2f}".format(self.__price))
        print("  sale%: {:.2f}".format(self.__percentage))

    def get_price(self):
        """
        Get the price of an object
        """
        price = self.__price
        price *= 1 - self.__percentage
        return price


def main():

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
