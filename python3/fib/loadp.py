#!/usr/bin/python3
# coding: utf-8
#
'''
use pickle to load
'''

import pickle
from glob import glob


def load_pickle(fn):
    ''' load pickle file '''
    mydata = {}
    nitem = 10
    try:
        with open(fn, "rb") as fh:
            mydata = pickle.load(fh)
            print(f"{fn}: {len(mydata)} entries")
            print(f'list first {nitem}...')
            cnt = 0
            for k,v in mydata.items():
                cnt += 1
                if cnt > nitem:
                    break
                print(k, v)
    except IOError as e:
        print('IOError:', e)

def main():
    ''' main '''
    filearr = glob('*.p')
    for ff in filearr:
        load_pickle(ff)

if __name__ == '__main__':
    main()
