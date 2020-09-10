#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

'''
list all dir
'''

from os import listdir, system, chdir, getcwd
from os.path import isdir, join

def check_dir(d):
    ''' check dir with pylint '''
    chdir(d)
    print('chdir: ', d)
    system('pylint *.py')

def main():
    ''' main '''
    # 指定要列出所有檔案的目錄
    top = getcwd()
    print('cwd:', top)

    # 取得所有檔案與子目錄名稱
    files = listdir(top)


    for f in files:
        if f == '__pycache__':
            continue
        fullpath = join(top, f)
        if isdir(fullpath):
            check_dir(fullpath)


if __name__ == '__main__':
    main()
