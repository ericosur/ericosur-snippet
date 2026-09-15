#!/usr/bin/env python3
# coding: UTF-8

'''
load some functions from __store__
'''

import sys

sys.path.insert(0, "..")
sys.path.insert(0, "prime")
from store import GetConfig, sep
from store.load_myutil import prt  # type: ignore[reportAttributeAccessIssue]


def run_test():
    ''' try different loads '''
    conf = GetConfig()
    the_dict = {"small": conf.get_small_config,
                "big": conf.get_big_config,
                "large": conf.get_large_config,
                "h119": conf.get_h119_config,
                "h422": conf.get_h422_config
                }
    for k,v in the_dict.items():
        prt(f'{k} config')
        prt(f"{v()}")
    sep()
    conf.do_tests()

def main():
    ''' main '''
    run_test()

if __name__ == '__main__':
    main()
