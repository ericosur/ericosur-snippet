#!/usr/bin/python3
# coding: utf-8

'''
demo of myutil.sha256sum(), myutil.md5sum()
'''

import argparse
import os

from myutil import md5sum, sha1sum, sha256sum


def test_factory(fn, hashfn, cmd):
    ''' test factory '''
    digest = hashfn(fn)
    print(f'{digest}  {fn}')
    cmd = f'{cmd} {fn}'
    os.system(cmd)


def do_test(f):
    ''' perform test '''
    func = "md5sum"
    print(f"----- {func} -----")
    test_factory(f, md5sum, func)

    func = "sha1sum"
    print(f"----- {func} -----")
    test_factory(f, sha1sum, func)

    func = "sha256sum"
    print(f"----- {func} -----")
    test_factory(f, sha256sum, func)


def process_files(files):
    ''' main '''
    for f in files:
        do_test(f)


def main():
    ''' main '''
    parser = argparse.ArgumentParser(description='example script for md5sum, sha1sum, sha256sum')
    parser.add_argument("files", metavar='file', type=str, nargs='+',
        help="perform digest function on files")
    parser.add_argument("-v", "--verbose", action='store_true', help='verbose')
    args = parser.parse_args()

    if args.verbose:
        print('verbose on')
    #print(args.files)
    process_files(args.files)

if __name__ == '__main__':
    main()
