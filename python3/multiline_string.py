#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

'''
demo how to use string.format()
and multi line string

need python 3.6+
'''

from __future__ import print_function
from myutil import get_python_version


def main():
    '''main function'''
    pi = 3.141592653589
    city_name = 'Taipei'

    # a multi line long string with extra spaces
    # need python 3.6+ to parse this format-string
    tmp = f'''
    select {pi:.6f} from weather.forecast
    where woeid in (select woeid
    from geo.places(1)
    where text =\'{city_name}\') and u=\'c\'
    '''

    # remove '\n' and spaces at head/tail
    msg = tmp.strip().replace('\n', '').replace('    ', ' ')
    print(msg)

if __name__ == '__main__':
    if float(get_python_version()) >= 3.6:
        main()
    else:
        print('need python 3.6+')
