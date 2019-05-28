#!/usr/bin/env python3
# coding: utf-8

'''
refer to utf-16 wiki:
from U+D800 to U+DFFF
while comes from U+10000 to U+10FFFF
'''

def main():
    surgg = u"\uD83D\uDE1C\uD83D\uDE17\uD83D\uDE0A\uD83D\uDE1C\uD83D\uDE1D\uD83D\uDE1D\uD83D\uDE09"
    a = surgg.encode('utf-16', 'surrogatepass').decode('utf-16')
    print('str: ' + a)
    print('len: {}'.format(len(a)))
    print(a.encode('unicode-escape').decode('utf-8'))

if __name__ == '__main__':
    main()
