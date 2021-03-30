"""
COMP.CS.100 Fibonacci series
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def main():
    num = int(input("How many Fibonacci numbers do you want? "))

    print("1. 1")
    previous_fib = 0
    current_fib = 1

    for i in range(2, num + 1):
        next_fib = previous_fib + current_fib
        print("{}. {}".format(i, next_fib))
        previous_fib = current_fib
        current_fib = next_fib


if __name__ == "__main__":
    main()
