#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
python dictionary samples

demo how to print a long multi lines
replace lambda in map()

'''
try:
    from rich import print as rprint
    from rich.pretty import pprint
    USE_RICH = True
except ImportError:
    USE_RICH = False
prt = rprint if USE_RICH else print

try:
    from loguru import logger
    USE_LOGURU = True
except ImportError:
    USE_LOGURU = False
logd = logger.debug if USE_LOGURU else print


def print_dict(**foo):
    ''' print content of dict '''
    if USE_RICH:
        pprint(foo)
        return
    for k, v in foo.items():
        prt(k, "=>", v)

# map() test
def cube(x):
    ''' cube of x '''
    return x * x * x

def merge_dict(p, q):
    ''' merge two dict '''
    r = {**p, **q}
    return r

def test1():
    ''' test1 '''
    logd('test1')
    p = {'a': 5, 'b': 7}
    q = {'b': 11, 'c': 13}
    prt(f'{p=}\n{q=}')
    # notice the later will overwrite the prior
    r = merge_dict(p, q)
    prt('p then q: after merge:')
    prt(r)
    # pylint: disable=arguments-out-of-order
    r = merge_dict(q, p)
    prt('q then p: after merge:')
    prt(r)

def test0():
    ''' test0 '''
    logd('test0')
    rec = {'name': {'first': 'Brown', 'last': 'Smith'},
           'job': ['dev', 'mgr'],
           'age': 40.5}
    prt("print( rec ==> ")
    print_dict(**rec)

    prt(f'''access rec[] ==>
rec['name']: {rec['name']}
rec['name']['first']: {rec['name']['first']}
rec['name']['last']: {rec['name']['last']}
''')

    rec['job'].append('foo')
    existed = 'age' in rec
    prt(f"if age in rec? {existed}")

    # demo of map()
    items = [11, 13, 17, 19, 23, 29]
    cubed = map(cube, items)
    prt("map(): ", cubed, type(cubed))

    items = (31, 37, 41, 43, 47, 53)
    # anti pattern
    # https://docs.quantifiedcode.com/python-anti-patterns/readability/using_map_or_filter_where_list_comprehension_is_possible.html
    #squared = map(lambda x: x ** 2, items)
    squared = [x ** 2 for x in items]
    prt("squared(): ", squared, type(squared))

def main():
    ''' main '''
    test0()
    prt('-' * 60)
    test1()

if __name__ == '__main__':
    main()
