#!/usr/bin/python3
# coding: utf-8

'''
the tail of multipler of 13? 17? 19? is 123
find the smallest one
'''

def test_n(n, t):
    ''' test n '''
    if n % 1000 == t:
        return True
    return False

def main():
    ''' main '''
    TAIL = 123
    for b in [13, 17, 19]:
        for i in range(99999):
            v = i * b
            if test_n(v, TAIL):
                print('tail of {}/{} is {}'.format(b, v, TAIL))
                break


if __name__ == '__main__':
    print(__doc__)
    main()
