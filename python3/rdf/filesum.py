#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=wrong-import-position
#

'''
demo of md5sum, sha1sum, sha256sum from myutil
also call cli md5sum, sha1sum, sha256sum to compare
'''

import argparse
import os
import sys

sys.path.insert(0, "..")
from myutil import isfile, md5sum, sha1sum, sha256sum


def test_factory(fn, hashfn, cmd):
    ''' test factory '''
    digest = hashfn(fn)
    print(f'{digest}  {fn}')

    # may not exist if windows or else...
    if isfile(cmd):
        cmd = f'{cmd} {fn}'
        os.system(cmd)


def do_test(f):
    ''' perform test '''
    the_tests = [
        [md5sum, "md5sum", "/usr/bin/md5sum"],
        [sha1sum, "sha1sum", "/usr/bin/sha1sum"],
        [sha256sum, "sha256sum", "/usr/bin/sha256sum"],
    ]

    for t in the_tests:
        [func, msg, cli] = t
        print(f'----- {msg} -----')
        test_factory(f, func, cli)


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
