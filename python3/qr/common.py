#!/usr/bin/env python3
# coding: utf-8
#

''' common funtions '''

import glob


def get_pngs():
    ''' return list of png files '''
    return glob.glob('*.png')
