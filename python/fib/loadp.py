#!/usr/bin/python3
'''
use pickle to load
'''
import pickle
from glob import glob

def load_pickle(fn):
    mydata = {}
    try:
        with open(fn, "rb") as fh:
            mydata = pickle.load(fh)
            print("{}: {} entries".format(fn, len(mydata)))
    except IOError:
        print('IOError')

def main():
    filearr = glob('*.p')
    for ff in filearr:
        load_pickle(ff)

if __name__ == '__main__':
    main()
