#!/usr/bin/env python3
# coding: UTF-8

'''
load some functions from __store__
'''

import sys

sys.path.insert(0, "..")
sys.path.insert(0, "prime")
from store import GetConfig
from store.load_myutil import prt  # type: ignore[reportAttributeAccessIssue]


def run_test():
    ''' try different loads '''
    conf = GetConfig()
    conf.do_tests()
    prt(conf.get_h422_config())
    prt(conf.get_large_config())

def main():
    ''' main '''
    run_test()

if __name__ == '__main__':
    main()
