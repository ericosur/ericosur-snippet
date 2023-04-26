#!/usr/bin/python3
# coding: utf-8

'''
find a smallest integer that could be divided by 11 and
all digits sum is 15
'''

def digit_sum(v):
    ''' sum of digits, for example, 123
        the sum is 1+2+3 = 6
    '''
    digits = list(str(v))
    values = [int(x) for x in digits]
    return sum(values)

def main():
    ''' main '''
    cnt = 0
    t = 396
    while True:
        if cnt > 10:
            break

        cnt += 1
        t = t + 11
        ds = digit_sum(t)
        print(f'{t}: {ds}')

if __name__ == '__main__':
    main()
