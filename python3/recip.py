#!/usr/bin/env python3
# coding: utf-8
#

'''
reciprocal
try to get Repeating decimal

http://mathworld.wolfram.com/RepeatingDecimal.html
'''
#from random import randint

def wala(m, n):
    ''' calculate wala '''
    if n <= 1 or m >= n:
        raise ValueError(m, n)

    (p, q, r, stop, prev_r) = (m*10, 0, 0, 0, -1)
    cnt = 0
    ns = []
    while True:
        cnt += 1
        # if p < n:
        #     q = 0
        (q, r) = divmod(p, n)
        if r in [1, prev_r]:
            if stop >= 1:
                print(q, end='')
                ns.append(q)
                break
            stop += 1
        elif r == 0:
            print(q)
            print('divisible')
            return None
        p = r
        prev_r = r
        if stop == 1:
            print(f'{q}*', end='')
            #print('*', end='')
            #print(q)
            #ns.append(q) # should not append into list
            #stop += 1
            #break   # will not repeat
        if stop == 0:
            print(q, end='')
            ns.append(q)
        p = p * 10
        if cnt > n * 2 + 2:
            #raise ValueError('too many repeating...', ns)
            break

    print()
    return ns


def show_answer(m, n, ns):
    ''' show ns '''
    if ns:
        print(f'{m} / {n} =>')
        s = [str(x) for x in ns]
        print(''.join(s))


def print_vals(n):
    ''' print values '''
    vals = [n*i for i in range(1, 10)]
    print(vals)

def test1():
    ''' test1 '''
    # args = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    #         31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    #         73, 79, 83, 89, 97, 241]
    args = [2, 3, 4, 7*23]
    for n in args:
        result = wala(1, n)
        if result:
            show_answer(1, n, result)
        if result and len(result) == n - 1:
            print('    number of digits is n-1 <=====')

def main():
    ''' main '''
    m = 2
    n = 11*13*17
    print(n)
    res = wala(m, n)
    if res:
        show_answer(m, n, res)

if __name__ == '__main__':
    main()
