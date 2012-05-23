#!/usr/bin/python

'''
change one byte from specified file
change money for ww2 savegame

TODO: add glob to modify multiple savegame at one run

'''

def read_and_report():
	offset = 0x0065
	fname = '/var/mobile/Applications/3D5AA6A4-4091-4390-9B03-86213162C4C5/Documents/game0.sav'

	fp = open(fname, "r+b")
	fp.seek(offset, 0)
	fp.write('\x7f')
	fp.close

if __name__ == '__main__':
	read_and_report()
