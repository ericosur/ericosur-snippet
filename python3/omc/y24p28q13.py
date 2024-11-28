#!/usr/bin/env python3
# coding: utf-8

'''
求滿足下列條件的最小正整數N，N既可以表示為9個連續正整數的和，
又可以表示為10個連續正整數的和，還可以表示為11個連續正整數的和
'''

def series(start, no):
    '''
    start: first number
    no 個連續正整數
    '''
    vals = list(range(start, start+no))
    assert len(vals)==no
    return sum(vals)


def main():
    ''' main '''
    print('nines')
    nines = {None}
    for i in range(40,52):
        r = series(i, 9)
        nines.add(r)
        print(i, r)

    print('tens')
    tens = {None}
    for i in range(40,52):
        r = series(i, 10)
        tens.add(r)
        print(i, r)

    print('elevens')
    elevens = {None}
    for i in range(40,52):
        r = series(i, 11)
        elevens.add(r)
        print(i, r)


    x10 = nines.intersection(tens)
    x11 = x10.intersection(elevens)
    print(x11)



if __name__ == '__main__':
    main()
