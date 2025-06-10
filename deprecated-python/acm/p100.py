#!/usr/bin/python

'''
    the 3n+1 problem
    http://acm.uva.es/p/v1/100.html

Sample Input

1 10
100 200
201 210
900 1000

Sample Output

1 10 20
100 200 125
201 210 89
900 1000 174

'''
ARR = []
DEBUG = 0

# pylint: disable=global-statement

def p100(n):
    ''' get p100 '''
    global ARR

    if DEBUG:
        print('n', n,)
    ARR.append(n)
    if n == 1:
        r = len(ARR)
        if DEBUG:
            print("len = ", r)
        return r

    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n = n / 2

    return p100(n)

def process(t):
    ''' process pair '''
    global ARR
    local_max = 0
    if DEBUG:
        print("fr, to = ", t[0], t[1])
    else:
        print(t[0], t[1],)

    for i in range(t[0], t[1]+1):
        ARR = []
        if DEBUG:
            print("i", i,)
        r = p100(i)
        #print "r", r,
        if r > local_max:
            #print "max!!"
            local_max = r
    if DEBUG:
        print("max", local_max)
    else:
        print(local_max)


def find_max_in_pair(tp):
    '''
        to prevent n < m
    '''
    (m, n) = (tp)
    #print m, n,
    if n < m:
        q = (n, m)
        #print q
        process(q)
    else:
        #print tp
        process(tp)

def main():
    ''' main '''
    pair = [(1, 10), (100, 200),
            (201, 210), (900, 1000)]

    for pp in pair:
        find_max_in_pair(pp)

if __name__ == '__main__':
    main()
