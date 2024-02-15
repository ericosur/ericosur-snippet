#!/usr/bin/env python3
# coding: utf-8

'''
p20, q22 若A是一個三位數，且A被12、20、25除之皆餘9，
且A不是11的倍數，則A最大值為多少？
'''

def validate(a):
    return a%12==9 and a%20==9 and a%25==9

def action():
    ''' action '''
    for i in range(100, 999+1):
        if validate(i):
            print(i)

def main():
    ''' main '''
    #test()
    action()

if __name__ == '__main__':
    main()
