#!/usr/bin/python3
# coding: utf-8

'''
1+3+5+7...
'''


def main():
    ''' main '''
    limit = 400
    t = 0
    k = 1
    repeat = 1000
    for i in range(repeat):
        #print(k)
        t += k
        k += 2
        print(i, t)
        if t >= limit:
            break



if __name__ == '__main__':
    main()
