#!/usr/bin/python3
# coding: utf-8

'''
9xx // AB = 25 ... 2x
'''

def test_number():
    for n in range(900, 1000):
        for ab in range(21, 99):
            if n // ab == 25:
                r = n % ab
                if 29 >= r >= 20:
                    print(n, ab, r)


def main():
    ''' main '''
    print('main')
    test_number()

if __name__ == '__main__':
    main()
