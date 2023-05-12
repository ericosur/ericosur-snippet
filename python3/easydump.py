#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
easy dump a specified file
'''

import argparse
import os

class MyConfig():
    ''' a class that stores a shared variable '''
    _v = False
    def get_v(self):
        ''' getter '''
        return type(self)._v
    def set_v(self, v):
        ''' setter '''
        type(self)._v = v
    demo = property(get_v, set_v)


def dump_file(fname):
    ''' dump specified file '''
    config = MyConfig()
    cnt = 0
    total_cnt = 0
    msg = ''
    isforcebreak = False
    with open(fname, 'rb') as fin:
        for byt in fin.read():
            total_cnt += 1
            cnt += 1
            msg = msg + f'{byt:02x} '
            if cnt != 0 and not cnt % 16:
                print(msg)
                msg = ''
                cnt = 0
            if config.demo and total_cnt > 64:
                isforcebreak = True
                msg = ''
                break
        if msg != '':
            print(msg)
    if isforcebreak:
        print('[INFO] break due to DEMO mode')


def test(args):
    ''' main function '''
    config = MyConfig()
    if args == []:
        print('apply DEMO mode...')
        config.demo = True
        args.append('ranit.py')

    for fn in args:
        if not os.path.isfile(fn):
            print(f"file not found: {fn}")
            continue

        print(f"{fn}:")
        dump_file(fn)

def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='trivia script to dump a file')
    parser.add_argument("files", type=str, nargs='*', help="specified files to dump")
    parser.add_argument("-d", "--demo", action='store_true', default=False, help='apply demo mode')

    #parser.parse_args(['-i input.txt -o out.txt str1 str2'])

    args = parser.parse_args()

    if args.demo:
        #print('demo:', args.demo)
        test([])
        return

    if args.files == []:
        parser.print_help()
        return

    test(args.files)

if __name__ == '__main__':
    main()
