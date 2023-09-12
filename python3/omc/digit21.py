#!/usr/bin/python3
# coding: utf-8

'''
3-digit numbers, sum of digits equals 21
last digit - middle digit = 1
'''

def is_valid(v):
    ''' search answer '''
    digits = list(str(v))
    vals = [int(x) for x in digits]
    if sum(vals) == 21:
        if vals[1]-vals[2]==1:
            print(v)
            return True
    return False

def main():
    ''' main '''
    for i in range(100, 999+1):
        is_valid(i)

if __name__ == '__main__':
    main()
