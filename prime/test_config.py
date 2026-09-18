#!/usr/bin/env python3
# coding: UTF-8

'''
load some functions from __store__
'''

import sys

sys.path.insert(0, "..")
sys.path.insert(0, "prime")
from store import GetConfig


def run_test():
    ''' try different loads '''
    conf = GetConfig()
    conf.do_tests()

def main():
    ''' main '''
    run_test()

if __name__ == '__main__':
    main()
