#!/usr/bin/python3
# coding: utf-8

'''
continuous sum

eg:
15 = 1 + 2 + 3 + 4 + 5
15 = 4 + 5 + 6
15 = 7 + 8

ask 45?
'''

import argparse


def solve(n):
    ''' solve '''
    print("=======> solve this: {}".format(n))
    upper = n // 2
    s = 0
    ans = []
    for i in range(1, upper+1):
        s = 0
        r = i
        while s < n:
            s += r
            ans.append(r)
            if s == n:
                print('exactly: ', ans)
                break
            if s > n:
                break
            r += 1
        ans.clear()

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='brief description for this script')
    parser.add_argument("integers", metavar='ints', type=int, nargs='*',
        help="trial with these integers")

    args = parser.parse_args()
    if args.integers == []:
        print('apply demo question: 45')
        args.integers.append(45)

    for ii in args.integers:
        solve(ii)

if __name__ == '__main__':
    main()
