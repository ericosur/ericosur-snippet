#!/usr/bin/python

# python dictionary

def print_dict(**foo):
    for x in foo:
        print( x,"=>",foo[x] )

''' map() test '''
def cube(x):
    return x*x*x


def main():
    rec = { 'name': {'first': 'Brown', 'last': 'Smith'},
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
    print( "map(): ", cubed, type(cubed) )

    items = (31, 37, 41, 43, 47, 53)
    squared = map(lambda x: x**2, items)
    print( "map(): ", squared, type(squared) )


if __name__ == '__main__':
    main()
