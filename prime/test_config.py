#!/usr/bin/env python3
# coding: UTF-8

'''
test load_myutil.py
'''

from store import GetConfig, sep


def main():
    ''' main '''
    print('main')
    conf = GetConfig()
    ret = conf.get_small_config()
    print(ret)
    ret = conf.get_big_config()
    print(ret)
    ret = conf.get_large_config()
    print(ret)
    ret = conf.get_h119_config()
    print(ret)

    sep()
    conf.do_tests()

if __name__ == '__main__':
    main()
