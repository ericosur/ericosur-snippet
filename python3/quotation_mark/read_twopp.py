#!/usr/bin/python3
# coding: utf-8

''' show codepoint of twopp.txt '''

def main():
    ''' main '''
    with open("twopp.txt", "rt") as f:
        for l in f.readlines():
            c = l.strip()
            print('[{}]: U+{:04X}'.format(c, ord(c)))

if __name__ == '__main__':
    main()
