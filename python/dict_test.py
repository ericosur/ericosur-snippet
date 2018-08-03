#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
python dictionary samples

demo how to print a long multi lines
replace lambda in map()

'''

from __future__ import print_function


def print_dict(**foo):
    ''' print content of dict '''
    for x in foo:
        print(x, "=>", foo[x])

# map() test
def cube(x):
    ''' cube of x '''
    return x * x * x


def main():
    '''main function'''
    rec = {'name': {'first': 'Brown', 'last': 'Smith'},
           'job': ['dev', 'mgr'],
           'age': 40.5}
    print("print( rec ==> ")
    print_dict(**rec)

    print('''access rec[] ==>
rec['name']: {0}
rec['name']['first']: {1}
rec['name']['last']: {2}
'''.format(rec['name'], rec['name']['first'], rec['name']['last']))

    rec['job'].append('foo')

    print("if age in rec? {0}".format('age' in rec))

    # demo of map()
    items = [11, 13, 17, 19, 23, 29]
    cubed = map(cube, items)
    print("map(): ", cubed, type(cubed))

    items = (31, 37, 41, 43, 47, 53)
    # anti pattern
    # https://docs.quantifiedcode.com/python-anti-patterns/readability/using_map_or_filter_where_list_comprehension_is_possible.html
    #squared = map(lambda x: x ** 2, items)
    squared = [x ** 2 for x in items]
    print("squared(): ", squared, type(squared))


if __name__ == '__main__':
    main()
