#!/usr/bin/python3
# coding: utf-8

'''
only coin 4 and coin 7
'''

def no_change(t):
    ''' find if no change left '''
    curr = t
    diff = 7
    cnt7 = 0
    left = curr
    minq = 99
    while left > 0:
        if left % 4 == 0:
            q = int(left / 4)
            minq = min(q, minq)
            print(f'{t:2d}: {cnt7} x 7 + {q:2d} x 4')
        left = left - diff
        cnt7 += 1
    print(f'minq: {minq}')

def main():
    ''' main '''
    t = [80, 90, 100, 110]
    for i in t:
        no_change(i)


if __name__ == '__main__':
    main()
