#!/usr/bin/python

'''
change one byte from specified file
change money for ww2 savegame

TODO: add glob to modify multiple savegame at one run

'''

import sys

PATH_APP='/var/mobile/Applications'
PATH_DOC='Documents'
path_dict = { 
	'0': '',
	# euro 2
	'1': '7D9F41C7-E8ED-4E1B-9018-486A5887DE0D', 
	# euro 3
	'2': '3893A048-623C-47D7-9D96-934EC6FC4B9F', 
	# world war
	'3': '3D5AA6A4-4091-4390-9B03-86213162C4C5', 
}

'''
In european war 3, modify commander.sav at 0x0c for modal.
'''
GAME_FILE = 'game0.sav'
DEBUG = 1

def read_and_report(pos = '0'):
	offset = 0x0064
	value = '\x0f\x27\x00\x00'

	if pos == '0':
		fname = '.' + '/' + GAME_FILE
	else:
		fname = PATH_APP + '/' + path_dict[pos] + '/' + PATH_DOC + '/' + GAME_FILE

	if pos == '2':
		offset = 0x00c4
		value = '\x0f\x27\x00\x00\x0e\x27'

	print fname
	
	if DEBUG:
		return

	fp = open(fname, "r+b")
	fp.seek(offset, 0)
	fp.write(value)
	fp.close

if __name__ == '__main__':
	if len(sys.argv) > 1:
		print sys.argv[0], sys.argv[1]
		read_and_report(sys.argv[1])
	else:
		read_and_report()

