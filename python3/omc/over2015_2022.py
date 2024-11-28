#!/usr/bin/env python3
# coding: utf-8

'''
p = 1 + 20 + 39 + 58 + ... + 2015
q = 2 + 4 + 6 + ... + 2022
'''

def main():
    ''' main '''
    p_limit=2015
    p_delta = 19
    t = 1
    p = []
    while True:
        p.append(t)
        t += p_delta
        if t>p_limit:
            break
    print(p[-1], sum(p))

    q_limit=2022
    q_delta = 2
    t = 2
    q = []
    while True:
        q.append(t)
        t += q_delta
        if t>q_limit:
            break
    print(q[-1], sum(q))


if __name__ == '__main__':
    main()
