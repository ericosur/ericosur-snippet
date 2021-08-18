#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
list all dir
'''

from glob import glob
from os import listdir, system, chdir, getcwd
from os.path import isdir, join

def check_dir(d):
    ''' check dir with pylint '''
    chdir(d)
    arr = glob('*.py')
    # if no py files, will not issue pylint command
    if arr:
        print('pylint check dir:', d)
        system('pylint *.py')

def main():
    ''' main '''
    # record the current working directory
    top = getcwd()
    print('cwd:', top)

    # get sub-directories & files under CWD (one level only)
    files = listdir(top)
    ignores = ['__pycache__']
    for f in files:
        if f in ignores:
            continue
        fullpath = join(top, f)
        if isdir(fullpath):
            check_dir(fullpath)


if __name__ == '__main__':
    main()
