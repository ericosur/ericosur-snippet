#!/usr/bin/python3
# coding: utf-8


def gcd(m: int, n: int) -> int:
    '''
    calculate gcd number by rescursive
    '''
    if n == 0:
        return m
    return gcd(n, m % n)

def main():
    ''' main '''
    m = []
    for v in range(1,48+1):
        if gcd(v, 48) == 1:
            print(v)
            m.append(v)
    print(sum(m))
    print(len(m))

if __name__ == '__main__':
    main()
