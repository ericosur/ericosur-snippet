#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
python dictionary samples

demo how to print a long multi lines
replace lambda in map()

'''

def print_dict(**foo):
    ''' print content of dict '''
    for k, v in foo.items():
        print(k, "=>", v)

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

    print(f'''access rec[] ==>
rec['name']: {rec['name']}
rec['name']['first']: {rec['name']['first']}
rec['name']['last']: {rec['name']['last']}
''')

    rec['job'].append('foo')
    existed = 'age' in rec
    print(f"if age in rec? {existed}")

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
