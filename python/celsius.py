#!/usr/bin/python
# -*- coding: utf-8 -*-

''' convert temperature from CLI '''

from __future__ import print_function
import sys
import locale


def convert_temperature():
    '''convert temerature'''
    # Loop over the arguments
    for i in sys.argv[1:]:
        try:
            fahrenheit = float(locale.atof(i))  # note: string.atoi ==> locale.atoi
        except ValueError:
            print('invalid value: {}'.format(i))
        else:
            celsius = (fahrenheit - 32.0) * 5.0 / 9.0
            #print '%i\260F = %i\260C' % (int(fahrenheit), int(celsius+.5))
            #   print '%i degree F = %i degree C' % (int(fahrenheit), int(celsius+.5))
            #print('%i degree F = %i degree C' % (fahrenheit, celsius))
            print('%.2f degree F = %.2f degree C' % (fahrenheit, celsius))


def main():
    '''main function'''
    # If no arguments were given, print a helpful message
    if len(sys.argv) == 1:
        print('Usage: celsius temp1 temp2 ...')
        sys.exit(0)

    print('convert fahrenheit to celsius')
    convert_temperature()


if __name__ == '__main__':
    main()
