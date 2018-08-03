#!/usr/bin/python
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
    for line in open(fname, 'rb').read():
        cnt += 1
        #print('%02x' % ord(line), end=' ')
        msg = msg + '{:02x} '.format(ord(line))
        if cnt != 0 and not cnt % 16:
            print(msg)
            msg = ''
            cnt = 0


def main():
    ''' main function '''
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        fname = sys.argv[0]

    if not os.path.isfile(fname):
        print("file not found: {}".format(fname))
        quit()

    print("process %s" % fname)
    dump_file(fname)


if __name__ == '__main__':
    main()
