#!/usr/bin/python3.6
# coding: utf-8

'''
demo of myutil.sha256sum(), myutil.md5sum()
'''

import os
import sys
from myutil import sha256sum, md5sum

def test256(f):
    ''' test 256 '''
    digest = sha256sum(f)
    print(f'{digest}  {f}')
    cmd = f'sha256sum {f}'
    os.system(cmd)


def test5(f):
    ''' test 5 '''
    digest = md5sum(f)
    print(f'{digest}  {f}')
    cmd = f'md5sum {f}'
    os.system(cmd)


def main(argv):
    ''' main '''
    if argv == []:
        argv.append('myutil.py')

    for f in argv:
        test256(f)
        test5(f)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
    else:
        main([])
