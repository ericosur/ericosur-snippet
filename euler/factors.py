#!/usr/bin/env python3
# code: utf-8

'''
https://projecteuler.net/problem=3
https://stackoverflow.com/questions/42080641/finding-all-numbers-that-evenly-divide-a-number
https://stackoverflow.com/questions/24975705/python-why-does-this-project-euler-3-solution-work
https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/
'''

def find_max_factor(nn):
    ''' find max factor '''
    i = 2
    factors = []
    while i * i < nn:
        while nn % i == 0:
            nn = nn // i
            if i not in factors:
                factors.append(i)
        i = i + 1
    if i not in factors:
        factors.append(i)
    if nn not in factors:
        factors.append(nn)
    return nn, factors

def test(nn):
    ''' test '''
    maxf, factors = find_max_factor(nn)
    print('{} max factor: {}\nfactors: {}\n'.format(nn, maxf, factors))

def main():
    ''' main '''
    test(12)
    test(13195)
    test(600851475143)

if __name__ == '__main__':
    main()
