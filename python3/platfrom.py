#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' get name of platform '''

from __future__ import print_function
import sys
import re
from platformdirs import PlatformDirs

def show_sysplatform():
	''' show '''
	print(f"OS platform is {sys.platform}")
	print("python version:", sys.version_info)
	#print('version:', sys.version)
	#print("lib path:", sys.path)
	#print('executable:', sys.executable)
	#print('implementation:', sys.implementation)

	# too long to print out
	#print('modules:', sys.modules)

def show_platformdirs():
	''' module platformdirs '''
	p = PlatformDirs('myapp', 'acme')
	print(f'{p.site_cache_dir=}')
	print(f'{p.site_config_dir=}')
	print(f'{p.site_data_dir=}')
	print(f'{p.user_cache_dir=}')
	print(f'{p.user_config_dir=}')
	print(f'{p.user_data_dir=}')
	print(f'{p.user_documents_dir=}')
	print(f'{p.user_log_dir=}')
	print(f'{p.user_music_dir=}')
	print(f'{p.user_pictures_dir=}')
	print(f'{p.user_runtime_dir=}')
	print(f'{p.user_state_dir=}')
	print(f'{p.user_videos_dir=}')

def main():
	''' main '''
	show_sysplatform()
	print()
	show_platformdirs()

if __name__ == '__main__':
	main()
