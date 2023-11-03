#!/usr/bin/env python3

# Created by: Joe Rugezo
# Created on: oct 2023
# This program uses a try statement

import random


def main():
    # this function uses a try statement
    random_variable = random.randint(0, 9)

    # user input
    integer_as_string = input("Enter an integer: ")
    print("")

    # Compare and guess
    #  display
    try:
        integer_as_number = int(integer_as_string)

        if integer_as_string == random_variable:
            print(f"{integer_as_string} is correct")
        elif integer_as_string != random_variable:
            print(f"{integer_as_string} is incorrect")

    except:
        print(f"{integer_as_string} is not an integer")
    finally:
        print("Thanks for playing")


if __name__ == " __main__":
    main()
