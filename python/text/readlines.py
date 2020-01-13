#!/usr/bin/env python3
# coding: utf-8

''' random pick one line from a text file '''

from random import choice

def main():
    ''' main '''

    # read foo.txt into a list
    with open('foo.txt') as f:
        mylist = f.readlines()
        picked_line = choice(mylist).strip()
        if picked_line == '':
            print('! this line is empty')
        else:
            print(picked_line)

if __name__ == '__main__':
    main()
