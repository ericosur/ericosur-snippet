#!/usr/bin/env python3

# mypy: ignore-errors

'''
keyring basic config ?
'''


import sys

import keyring.util.platform_

sys.path.insert(0, '/usr/local/lib/python3.5/dist-packages')

print(keyring.util.platform_.config_root())
print(keyring.util.platform_.data_root())
