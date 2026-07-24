#!/usr/bin/env python3
#

''' common funtions '''

import glob


def get_pngs():
    ''' return list of png files '''
    return glob.glob('*.png')
