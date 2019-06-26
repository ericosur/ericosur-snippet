#!/usr/bin/env python3
# coding: utf-8

'''
using sympy.factorint to factorize integers
'''

def show(value):
    '''
    use sympy.factorint() and display in formatted form
    '''
    from sympy import factorint
    if value <= 2:
        print("must > 1")
        return
    myd = factorint(value)
    print('{} = '.format(value), end='')
    x = list(myd.keys())
    x.sort()
    if len(x) == 1:
        print('PRIME')
        return

    while x:
        key = x.pop(0)
        pv = myd[key]
        if pv == 1:
            print('{}'.format(key), end='')
        else:
            print('{}^{}'.format(key, pv), end='')

        if x:    # not empty
            print(' * ', end='')
        else:
            print()


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print('could also specify numbers from cli')
        for n in range(2147483647, 2147483649):
            show(n)
    else:
        if sys.argv[1] == 'test':
            for n in range(1000, 10000):
                show(n)
            quit()

        for n in sys.argv[1:]:
            try:
                print('n:{}'.format(n))
                show(int(n))
            except ValueError:
                print("{} is not a numeric".format(n))
