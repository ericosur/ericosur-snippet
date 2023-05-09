#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' get name of platform '''

from __future__ import print_function
import sys

print(f"OS platform is {sys.platform}")
print("python version:", sys.version_info)
print('version:', sys.version)
print("lib path:", sys.path)
print('executable:', sys.executable)
print('implementation:', sys.implementation)

# too long to print out
#print('modules:', sys.modules)
