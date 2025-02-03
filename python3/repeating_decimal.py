#!/usr/bin/env python3
# coding: utf-8
#

'''
reciprocal
try to get Repeating decimal

If 1/m is a repeating decimal and 1/n is a terminating decimal,
them 1/(mn) has a nonperiodic part whose length is that of 1/n
and a repeating part whose length is that of 1/m (Wells 1986, p. 60).

recip.py is buggy, and not working as expected.

reference:
- http://mathworld.wolfram.com/RepeatingDecimal.html
- https://en.wikipedia.org/wiki/Repeating_decimal

'''
#from random import randint

def find_repeating_decimal(numerator, denominator):
    """
    Finds the repeating part of a decimal fraction.
    :param numerator: The numerator of the fraction.
    :param denominator: The denominator of the fraction.
    :return: A tuple containing the non-repeating and repeating parts of the decimal.
    """
    # Dictionary to store remainders and their positions
    remainder_dict = {}
    result = ""
    non_repeating = ""

    # Perform division
    quotient, remainder = divmod(numerator, denominator)
    result += str(quotient) + "."

    # Position in the decimal part
    position = 0
    repeating_start = -1

    while remainder != 0:
        # If the remainder is already seen, we found the repeating part
        if remainder in remainder_dict:
            repeating_start = remainder_dict[remainder]
            break

        # Store the position of this remainder
        remainder_dict[remainder] = position

        # Multiply remainder by 10 and get the next digit
        remainder *= 10
        digit, remainder = divmod(remainder, denominator)
        result += str(digit)

        position += 1

    if repeating_start != -1:
        non_repeating = result[:result.index('.') + 1 + repeating_start]
        repeating = result[result.index('.') + 1 + repeating_start:]
    else:
        non_repeating = result
        repeating = ""

    return non_repeating, repeating


def show(numerator, denominator, non_repeating, repeating):
    ''' show'''
    len_repeat = len(repeating)
    print(f"Decimal repr for {numerator}/{denominator} {len_repeat}:"
            f" {non_repeating}({repeating})")

def copilot():
    ''' example from copilot
        https://oeis.org/A085837
        also check: https://oeis.org/A051626
    '''
    dens = [3, 6, 7, 9, 11, 12, 13, 14, 15, 17, 18, 19, 21, 22, 23, 24, 26, 27,
        28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46,
        47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65,
        66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 81, 82, 83, 84]

    numerator = 1
    cyclics = {}
    for d in dens:
        denominator = d
        non_repeating, repeating = find_repeating_decimal(numerator, denominator)
        len_repeat = len(repeating)
        show(numerator, denominator, non_repeating, repeating)
        if len_repeat == d - 1:
            cyclics[d] = repeating
    print(f"tried {len(dens)}, and get {len(cyclics)} Cyclic numbers")
    for k, v in cyclics.items():
        print(f"{k}: {v}")
    numer, denom = 1, 7*17
    # 1/7 has len 6 repeating decimal
    # 1/17 has len 16 repeating decimal
    # and lcm(6, 16) = 48
    nr, r = find_repeating_decimal(numer, denom)
    show(numer, denom, nr, r)
    # if denominator is 7*17*19, then length of repeating decimal is:
    # lcm(6, 16, 18) = 144

if __name__ == '__main__':
    copilot()
