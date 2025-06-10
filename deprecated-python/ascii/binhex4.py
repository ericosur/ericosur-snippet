#!/usr/bin/python3
# coding: utf-8

''' binhex '''

import binhex

def main():
    ''' main '''
    A = 'rnd.bin'
    B = 'out.bin'
    binhex.binhex(A, B)
    print('binhex({}, {})'.format(A, B))

if __name__ == '__main__':
    main()
