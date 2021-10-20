#!/usr/bin/env python3
# coding: utf-8

'''
This code is contributed
by Anubhav Raj Singh
https://www.geeksforgeeks.org/greedy-algorithm-egyptian-fraction/

Python3 program to print a fraction
in Egyptian Form using Greedy Algorithm
'''


# import math package to use ceiling function
import math

# pylint: disable=invalid-name

# define a function egyptianFraction
# which receive parameter nr as
# numerator and dr as denominator
def egyptianFraction(nr: int, dr: int):
    ''' egyptian fraction '''
    print("The Egyptian Fraction " +
          f"Representation of {nr}/{dr} is", end="\n")

    # empty list ef to store
    # denominator
    ef = []

    # while loop runs until
    # fraction becomes 0 i.e,
    # numerator becomes 0
    while nr != 0:

        # taking ceiling
        x = math.ceil(dr / nr)

        # storing value in ef list
        ef.append(x)

        # updating new nr and dr
        nr = x * nr - dr
        dr = dr * x

    # printing the values
    for i, m in enumerate(ef):
        if i != len(ef) - 1:
            print(f" 1/{m} +", end='')
        else:
            print(f" 1/{m}", end='')
    print()

def main():
    ''' main '''
    # calling the function
    egyptianFraction(14, 15)
    egyptianFraction(24, 25)
    egyptianFraction(39, 40)

    # raise OverflowError
    #egyptianFraction(5, 121)

if __name__ == '__main__':
    main()
