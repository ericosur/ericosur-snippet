#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position

'''
demo how to use string.format()
and multi line string

need python 3.6+
'''

import sys

sys.path.insert(0, "..")
from myutil import require_python_version  # type: ignore[import]


def main():
    '''main function'''
    pi = 3.141592653589
    city_name = 'Taipei'
    geo_place = 10036

    # a multi line long string with extra spaces
    # need python 3.6+ to parse this format-string
    tmp = f'''
    select {pi:.6f} from weather.forecast
    where woeid in (select woeid
    from geo.places({geo_place})
    where text =\'{city_name}\') and u=\'c\'
    '''

    print('Result:')
    # remove '\n' and spaces at head/tail
    msg = tmp.strip().replace('\n', '').replace('    ', ' ')
    print(msg)

if __name__ == '__main__':
    if require_python_version(3, 6):
        main()
    else:
        print('need python 3.6+')
