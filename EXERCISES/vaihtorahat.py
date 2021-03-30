# COMP.CS.100 Vaihtorahat
# Tekijä: Joose Lohi
# Opiskelijanumero: 050800360


def main():

    price = int(input("Purchase price: "))
    money = int(input("Paid amount of money: "))
    left = money - price

    if price >= money:
        print("No change")

    else:
        print("Offer change:")
        if left // 10 > 0:
            print("{} ten-euro notes".format(left // 10))
            left = left % 10
        else:
            pass

        if left // 5 > 0:
            print("{} five-euro notes".format(left // 5))
            left = left % 5
        else:
            pass

        if left // 2 > 0:
            print("{} two-euro coins".format(left // 2))
            left = left % 2
        else:
            pass

        if left // 1 > 0:
            print("{} one-euro coins".format(left // 1))


main()
