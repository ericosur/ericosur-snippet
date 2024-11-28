#!/usr/bin/env python3
# coding: utf-8

'''
to solve one to nice problem
'''

def get_number(i):
    ''' generate a number like 1, 22, 333, 4,444, 55,555 to
        999,999,999
    '''
    digits = ""
    rep = str(i)
    for _ in range(i):
        digits += rep
    return digits

def main():
    ''' main '''
    summ = 0
    vals = []
    for i in range(1, 10):
        val = get_number(i)
        vals.append(val)
        summ += int(val)

    print(f"The sum of these values:\n{vals}\n{summ}\nAnd mod 9 = {summ % 9}")

if __name__ == '__main__':
    main()
