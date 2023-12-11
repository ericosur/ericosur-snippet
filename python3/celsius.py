#!/usr/bin/python
# -*- coding: utf-8 -*-

''' convert temperature from CLI
    degree symbol is U+00B0
'''

from __future__ import print_function

import locale
import sys


def convert_temperature(argv):
    '''convert temerature'''
    # Loop over the arguments
    for i in argv:
        try:
            fahrenheit = float(locale.atof(i))  # note: string.atoi ==> locale.atoi
        except ValueError:
            print('invalid value: {i}')
        else:
            celsius = (fahrenheit - 32.0) * 5.0 / 9.0
            #print '%i\260F = %i\260C' % (int(fahrenheit), int(celsius+.5))
            #   print '%i degree F = %i degree C' % (int(fahrenheit), int(celsius+.5))
            #print('%i degree F = %i degree C' % (fahrenheit, celsius))
            print(f"{fahrenheit:.2f} °F = {celsius:.2f} °C")

def main():
    '''main function'''
    # If no arguments were given, print a helpful message
    if len(sys.argv) > 1:
        convert_temperature(sys.argv[1:])
    else:
        print('convert fahrenheit to celsius')
        print('Usage: celsius <temp1> <temp2> ...')
        sys.exit(0)

if __name__ == '__main__':
    main()
