#!/usr/bin/python3
# coding: utf-8

'''
    first example from ''Text processing in python''
'''


def is_comment(line):
    '''
    return true if the first char is #
    '''
    return line[:1] == '#'

def main():
    ''' main '''
    filename = "foo.txt"
    selected = filter(is_comment, open(filename).readlines())
    print(selected)

if __name__ == '__main__':
    main()
