#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
demo how to use string.format()
and multi line string
'''

from __future__ import print_function

def main():
    '''main function'''
    condition = '*'
    city_name = 'Taipei'
    tmp = '''
    select {0} from weather.forecast where woeid in (select woeid
     from geo.places(1) where text =\'{1}\') and u=\'c\'
    '''.format(condition, city_name)

    # remove '\n' and spaces at head/tail
    query = tmp.strip().replace('\n', '')
    print(query)

if __name__ == '__main__':
    main()
