#!/usr/bin/env python3
# coding: utf-8

'''
demo of module PyExifTool
'''

from glob import glob
import os

def main():
    ''' main '''
    files = glob('*.jpg')
    cnt = 0
    for f in files:
        cnt += 1
        d = os.path.getmtime(f)
        print(d)
        if cnt > 5:
            break

if __name__ == '__main__':
    main()
