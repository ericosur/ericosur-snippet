#!/usr/bin/env python3
# coding: utf-8
#

''' sample of hasattr '''


def hooray(obj, stm):
    ''' hooray '''
    if hasattr(obj, stm):
        print(f'has {stm}')
    else:
        print(f'NO such attr: {stm}')

def main():
    ''' main '''
    #arr = [dict(), set(), list(), tuple()]
    arr = [{}, set(), [], tuple()]
    for aa in arr:
        print('type:', type(aa))
        hooray(aa, 'add')
        hooray(aa, 'append')
        hooray(aa, 'extend')
        hooray(aa, 'remove')
        hooray(aa, '__contains__')


if __name__ == '__main__':
    main()
