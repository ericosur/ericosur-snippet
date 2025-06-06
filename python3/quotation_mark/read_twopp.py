#!/usr/bin/env python3
# coding: utf-8

''' show codepoint of twopp.txt '''

def main():
    ''' main '''
    with open("twopp.txt", "rt", encoding='utf8') as f:
        for ln in f.readlines():
            c = ln.strip()
            print(f'[{c}]: U+{ord(c):04X}')

if __name__ == '__main__':
    main()
