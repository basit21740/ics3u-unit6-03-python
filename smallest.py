#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Jan 2022
# This program shows the user the smallest number between 10 random numbers

import random


def smallest_number(list_of_numbers):
    # this functions figures out the smallest number

    smallest = list_of_numbers[0]

    for counter in list_of_numbers:
        if counter < smallest:
            smallest = counter

    return smallest


def main():
    # this function uses a list

    random_numbers = []

    # input
    for loop_counter in range(0, 10):
        single_random_number = random.randint(1, 100)
        random_numbers.append(single_random_number)
        print(
            "The random number {0} is {1} ".format(loop_counter, single_random_number)
        )
    print("")

    # call functions
    minimum = smallest_number(random_numbers)
    # output
    print("The smallest number is: {} ".format(minimum))
    print("\nDone.")


if __name__ == "__main__":
    main()
