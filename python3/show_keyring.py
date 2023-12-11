#!/usr/bin/env python3
# coding: utf-8

'''
keyring basic config ?
'''

from __future__ import print_function

import sys

import keyring.util.platform_

sys.path.insert(0, '/usr/local/lib/python3.5/dist-packages')

print(keyring.util.platform_.config_root())
print(keyring.util.platform_.data_root())
