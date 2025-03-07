#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    try to list the folder while is one month ago
'''

from __future__ import print_function

import datetime
import glob
import os
import sys
import time
sys.path.insert(0, '.')
sys.path.insert(0, '..')
from myutil import prt

# arg: 0 is list, 1 is detail
def showlist(folders: list, days: int=90, verbose: bool=False) -> None:
    '''
    input: a list with name of folders
    output: it would output the folders which is older than 30 days
    '''
    # timedelta for 30 days
    offset = datetime.timedelta(days=days)

    # get today
    today = datetime.datetime.fromtimestamp(time.time())
    # get datetime for nn days ago
    ago = today - offset
    prt(f'The date before {days} days ago: {ago}')
    # print the epoch from a datetime object
    #prt(ago.timestamp())
    prt('NOTE: here list the older folders')
    prt('=' * 56)

    # collect data for each folder
    datas = []
    for f in folders:
        entry = {}
        entry['folder'] = f
        ctime = os.path.getctime(f)
        entry['ctime'] = ctime
        #entry['ftime'] = datetime.datetime.fromtimestamp(ctime)
        datas.append(entry)

    # grep the folder which is older than 30 days
    for d in datas:
        f = d['folder']
        ctime = d['ctime']
        if ctime <= ago.timestamp():
            ftime = datetime.datetime.fromtimestamp(ctime)
            prt(f"[yellow]{f}[/]: ({ftime})")
    #     ctime = os.path.getctime(f)
    #     foldertime = datetime.datetime.fromtimestamp(ctime)

    #     if foldertime <= ago:
    #         prt(f"[yellow]{f}[/]: ({foldertime})")
    #     else:
    #         if verbose:
    #             prt(f'{f} is newer ({foldertime})')


def main():
    '''main function'''
    # get file list within current folder
    dirs = []

    for d in glob.glob('*'):
        # only sub-directory kept
        if not os.path.isdir(d):
            continue
        # skip the hidden folder
        if d[0] == '.' or d[0:2] == '__':
            continue
        dirs.append(d)

    dirs = sorted(dirs)
    showlist(dirs)

if __name__ == '__main__':
    main()
