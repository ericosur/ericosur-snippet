# coding: utf-8

'''
provide logd()
'''

import sys


def logd(*args, **wargs):
    ''' logd
    use it like the print(), additional parameter is 'debug'
    logd("hello world", debug=False) will not print at all
    '''
    d = False
    if "debug" in wargs:
        d = wargs.pop("debug")
    if d:
        print(*args, **wargs, file=sys.stderr)
