#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
    this file needs to be stored as UTF-8 text file
'''

from __future__ import print_function
import sys

def get_python_version():
    ''' will return a float like 2.7, 3.5 of python version '''
    ver = list(sys.version_info)
    n = float(ver[0]) + float(ver[1]) / 10
    return n

def print_hex(in_string):
    ''' print string in hex '''
    for c in list(in_string):
        print("{:x}".format(ord(c)), end=' ')
    print()

def hello_py2(msg):
    ''' hello for python2 '''
    # as big5
    print('===== hello_py2 =====')
    big5 = msg.decode('utf8').encode('big5')    # still str
    print('big5:', big5)
    print_hex(big5)

def hello_py3(msg):
    ''' hello for python3 '''
    print('===== hello_py3 =====')
    big5 = msg.encode('big5')
    print('big5:', big5)  # type would be byte
    for c in big5:
        print('{:x}'.format(c), end=' ')
    print()

def main():
    '''main function'''
    # utf-8
    msg = "哈囉"
    print('input:', msg)
    print('hex: ', end='')
    # py2: will get utf-8 hex
    # py3: will get unicode codepoint
    print_hex(msg)

    if get_python_version() >= 3.0:
        hello_py3(msg)
    else:
        hello_py2(msg)


if __name__ == '__main__':
    main()
