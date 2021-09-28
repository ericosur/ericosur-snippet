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
    try:
        with open(fn, "rb") as fh:
            mydata = pickle.load(fh)
            print(f"{fn}: {len(mydata)} entries")
    except IOError as e:
        print('IOError:', e)

def main():
    ''' main '''
    filearr = glob('*.p')
    for ff in filearr:
        load_pickle(ff)

if __name__ == '__main__':
    main()
