#!/usr/bin/python3
# coding: utf-8

'''
binomial
'''

def sumx(n):
    ''' returns sum of 1 to n '''
    if n == 1:
        return 1
    s = (1 + n) * n / 2
    return s

def main():
    ''' main '''
    t = 0
    for x in range(1,100):
        sx = sumx(x)
        r = sx / (x+1.0)
        t += r
        print(f'{sx}, {r}')
    print(t)

if __name__ == '__main__':
    main()
