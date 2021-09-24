#!/usr/bin/python3
# -*- coding: big5 -*-

'''
notice now this file is stored as ansi (cp950) text

# -*- coding: utf-8 -*-
the text file nned to be stored in utf-8
'''


def print_hex(in_string):
    ''' print string in hex '''
    for c in list(in_string):
        #print("%X" % ord(c), end=' ')
        print(f"{ord(c):X}", end=' ')
    print()


def main():
    ''' main '''
    STR = "中文字"   # notice the prefix 'u'
    print(STR)
    print_hex(STR)    # would print the unicode code point
    print(STR.encode('utf-8'))
    print_hex(STR)

if __name__ == '__main__':
    main()
