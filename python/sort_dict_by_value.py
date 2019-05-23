#!/usr/bin/env python3

'''
from:
http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
'''

from __future__ import print_function
import operator

def main():
    '''main function'''
    x = {1: 41, 3: 37, 4: 79, 2: 17, 0: 23}

    # sort by values of dict
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))
    print("x:{0}".format(x))
    print("sorted by values: {0}".format(sorted_x))

    # sort by keys of dict
    #x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    sorted_x = sorted(x.items(), key=operator.itemgetter(0))
    print("sorted by keys: {0}".format(sorted_x))

if __name__ == '__main__':
    main()
