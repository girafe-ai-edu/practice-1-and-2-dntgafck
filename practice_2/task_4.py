# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""


def get_valid_input():
    while True:
        try:
            value = int(input("Enter 4-digit integer:"))
            if value < 1000 or value > 9999:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a 4-digit integer number.")


if __name__ == '__main__':
    number = get_valid_input()
    t, rest = divmod(number, 10**3)
    h, rest = divmod(rest, 10**2)
    d, e = divmod(rest, 10)
    s = t + h + d + e
    print(f"{t} + {h} + {d} + {e} = {s}")
