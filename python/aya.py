#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
	if sys.platform == 'win32':
		print("error: win32 has no utf-8 terminal")
	else:
		print("你好！")
