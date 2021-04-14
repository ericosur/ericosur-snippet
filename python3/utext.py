#!/usr/bin/python3
# coding: utf-8

'''
simply to show how to import a module within another sub-directory
'''

import argparse
import emoji.mytofrom

def utf8_seq(cc: str):
    ''' utf8 sequence in hex format '''
    for ch in cc:
        s = ch.encode('utf-8').hex()
        print('{}({})'.format(ch, s), end=' ')
    print()

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='use emoji.mytofrom to show unicode sequence')
    parser.add_argument("s1", nargs='?', type=str, default='大道之行')
    parser.add_argument("-c", "--chars", action='store_true', help="show utf-8 hex by each character")
    args = parser.parse_args()

    s = args.s1
    emoji.mytofrom.to_from_u16(s)
    emoji.mytofrom.to_from_u8(s)
    emoji.mytofrom.to_utf8(s)

    if args.chars:
        utf8_seq(s)


if __name__ == '__main__':
    main()
