#!/usr/bin/python3
# coding: utf-8

'''
2k but not 4k between (low, high)
'''

def main():
    ''' main '''
    low = 150
    high = 250
    total = 0
    cnt = 0
    v = low -1
    while v < high:
        v += 1
        if v % 2 == 0:
            if v % 4 == 0:
                continue

            print(v)
            total += v
            cnt += 1
    print()
    print(total)
    print(cnt)

if __name__ == '__main__':
    main()
