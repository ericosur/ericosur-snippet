#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
convert epoch value to date/time string
'''

from __future__ import print_function
import time
import sys

def epoch2timestr(epoch=-1):
    ''' Replace time.localtime with time.gmtime for GMT time '''
    if epoch == -1:
        epoch = int(time.time())

    msg = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(epoch))
    return [epoch, msg]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print('argv[1]:({})'.format(sys.argv[1]))
        print(epoch2timestr(int(sys.argv[1])))
    else:
        print(epoch2timestr())
        print(epoch2timestr(1468123201))