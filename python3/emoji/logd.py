# coding: utf-8

'''
provide logd()
'''

import sys
from rich.console import Console
error_console = Console(stderr=True, style="bold red")

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

def loge(*args):
    ''' loge
    '''
    error_console.log(*args)
