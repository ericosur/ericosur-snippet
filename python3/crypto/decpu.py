#!/usr/bin/python3
#coding:UTF-8

'''
decrypt and get the data
'''

from passutil import PassUtil

def main():
    ''' main '''
    fn = 'my.json'
    decpu = PassUtil(fn)
    decpu.load()
    d = decpu.decrypt().decode()
    print(d)

if __name__ == '__main__':
    main()
