#!/usr/bin/env python3
# coding: utf-8
#
# pylint: disable=import-error
# pylint: disable=wrong-import-position
#

'''
brief description for this script
'''

import os
import sys

HOME = os.getenv('HOME')
UTILPATH = os.path.join(HOME, 'src/ericosur-snippet/python3')
if os.path.exists(UTILPATH):
    sys.path.insert(0, UTILPATH)

from myutil import read_setting

def read_image_config():
    ''' read image common config '''
    CONFIG = 'setting.json'
    if not os.path.exists(CONFIG):
        print('[ERROR] cannot load config:', CONFIG)
        sys.exit(1)
    data = read_setting(CONFIG)
    return data
