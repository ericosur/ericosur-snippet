#!/usr/bin/python3
# coding: utf-8

'''
define an operation that A # B = lcm(A,B) - gcd(A,B)
find the max 24 # X, X is between 1, 100
'''

def gcd(m: int, n: int) -> int:
    '''
    calculate gcd number by rescursive
    '''
    if n == 0:
        return m
    return gcd(n, m % n)

def lcm(m: int, n: int) -> int:
	''' get lcm '''
	return (m*n) // gcd(m, n)


def main():
    ''' main '''
    cnt = 0
    for p in range(1,5+1):
        for q in range(1,60):
            if p!=q and p<q and gcd(p, q)==1:
                print(p, q)
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
