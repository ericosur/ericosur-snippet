#!/usr/bin/env python3
# coding: utf-8

'''
int dow2(int y, int m, int d)
{
    d += m<3 ? y-- : y-2;
    return ((23*m/9+d+4+y/4-y/100+y/400)%7);
}
'''

def dow(y, m, d):
    ''' get day of week '''
    if m < 3:
        d += y
        y -= 1
    else:
        d += y - 2
    return (23*m//9+d+4+y//4-y//100+y//400)%7

def getyy(y):
    ''' get doomday of specified year '''
    cc = y // 100
    if cc < 17 or cc > 24:
        print('[FAIL] y is out-of-bound')
        return -1

    #     17 18 19 20
    #     21 22 23 24
    pp = [0, 2, 4, 5]
    yy = y % 100
    #print('yy:', yy)
    if yy%2: # odd
        yy += 11
    yy = yy // 2
    #print('yy:', yy)
    if yy%2:
        yy += 11
    # else:
    #     yy = yy // 2

    yy += pp[cc%4-1]
    return yy % 7


def main():
    '''
    print(dow(1975,6,17))
    print(dow(2012,2,10))
    print(dow(1976,11,8))
    '''

    #           2      3    2    4    4     3     1
    '''
    for v in [1975, 1985, 1941, 2012, 2018, 2019, 2020]:
        print('yy for {} = {}'.format(v, getyy(v)))
    '''
    for v in range(2010,2021):
        print('yy for {} = {}'.format(v, getyy(v)))

if __name__ == '__main__':
    main()
