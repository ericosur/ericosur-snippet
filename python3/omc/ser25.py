#!/usr/bin/python3
# coding: utf-8

'''
m = 2, 7, 12, 17, 22, ...
n = 5, 7, 9, 11, 13, 15, 17, ...
'''


def main():
    ''' main '''
    limit = 100
    m = set()
    x = 2
    for _ in range(limit):
        m.add(x)
        x += 5
    #print(m)
    x = 5
    n = set()
    for _ in range(limit):
        n.add(x)
        x += 2
    p = m.intersection(n)
    q = list(p)
    q.sort()
    print(q)


if __name__ == '__main__':
    main()
