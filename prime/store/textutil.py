#!/usr/bin/env python3
# coding: utf-8
#

'''
provides text funtions

the format of text file:

# comment
11
13
17
19

'''

def read_textfile(txtfn, debug=False):
    '''
    read number for text file
    one number one line
    will skip empty line
    will skip # line (at the pos 0)
    '''
    TAG = "read_textfile"
    ERROR_LIMIT = 10
    cnt = 0
    err = 0
    ret = []
    if debug:
        print(f'[{TAG}]: from file: {txtfn}')
    with open(txtfn, "rt", encoding='UTF-8') as fobj:
        for ln in fobj.readlines():
            ln = ln.strip()
            cnt += 1
            if err > ERROR_LIMIT:
                print('so many error lines...')
                break
            if ln == '' or ln.find("#")==0:
                continue
            try:
                n = int(ln)
                ret.append(n)
            except ValueError:
                print(f'error at: {cnt}: {ln}')
                err += 1
    if debug:
        print(f'[{TAG}]: process {cnt} lines, {err} errors, return size: {len(ret)}')
    return ret
