#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    try to list the folder while is one month ago
'''

from __future__ import print_function
import sys
import glob
import os
import time
import datetime

# arg: 0 is list, 1 is detail
def showlist(folders, arg=1):
    '''
    input: a list with name of folders
    output: it would output the folders which is older than 30 days
    '''
    # timedelta for 30 days
    offset = datetime.timedelta(days=30)
    #print offset

    # get today
    today = datetime.datetime.fromtimestamp(time.time())
    # get datetime for 30 days ago
    ago = today - offset
    print('30 days ago = ', ago)

    ctime = 0
    foldertime = 0
    for xx in folders:
        ctime = os.path.getctime(xx)
        foldertime = datetime.datetime.fromtimestamp(ctime)
        if foldertime <= ago:
            if arg == 1:
                print(f"!!! {xx} is one month ago ({foldertime})")
            else:
                print(xx)
        else:
            if arg == 1:
                print(f'{xx} is newer ({foldertime})')
        #print xx, ":", time.strftime('%c', time.localtime(ctime))

def main():
    '''main function'''
    # get file list within current folder
    alllist = glob.glob('*')
    dirlist = []

    for x in alllist:
        # only sub-directory kept
        if os.path.isdir(x):
            #print x
            dirlist.append(x)
    detail_arg = 1
    if (len(sys.argv) > 1) and (sys.argv[1] == '-l'):
        detail_arg = 0
    #print len(dirlist)
    showlist(dirlist, detail_arg)


if __name__ == '__main__':
    main()
