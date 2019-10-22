#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
easy dump
'''

from __future__ import print_function
import sys
import os

def dump_file(fname):
    ''' dump specified file '''
    cnt = 0
    msg = ''
    for byt in open(fname, 'rb').read():
        cnt += 1
        msg = msg + '{:02x} '.format(byt)
        if cnt != 0 and not cnt % 16:
            print(msg)
            msg = ''
            cnt = 0


def main(args):
    ''' main function '''

    if args == []:
        print('should not be empty...')
        sys.exit()

    for fn in args:
        if not os.path.isfile(fn):
            print("file not found: {}".format(fn))
            continue

        print("=====> process {}:".format(fn))
        dump_file(fn)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print('usage: easy_dump.py [file1] [file2]...')
        print('demo:')
        main([sys.argv[0]])
