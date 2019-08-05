#!/usr/bin/env python3
# coding: utf-8
#

''' function args '''


def test_args(*args):
    ''' test args '''
    print('test_args:', args)
    print('sum:', sum(args))
    print('-----')

def test_kwargs(**kwargs):
    ''' test kwargs '''
    print('kwargs:', kwargs)
    s = kwargs['x']**3 + 2 * kwargs['y']**2 + 3 * kwargs['z']
    print("s:", s)
    print('-----')

def fill_zero(a, max_size=10):
    '''
    input a list **a**
    assign the max_size of new list
    and element will be filled with zero
    '''

    print('len(a):', len(a))
    a = a + [0] * (max_size - len(a))
    return a


def main():
    ''' main '''
    args = (43, 97)
    test_args(*args)
    test_args(3, 5, 7)

    kwargs = {'x': 3, 'y': 4, 'z': 5}
    test_kwargs(**kwargs)
    test_kwargs(x=1, y=2, z=3)

    a = [97]
    a = fill_zero(a, 3)
    print(a)

if __name__ == '__main__':
    main()
