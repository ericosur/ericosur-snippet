#!/usr/bin/python
import os
import sys

"""
    try to locate specified name in PATH
"""

def search_file(filename, search_path, pathsep=os.pathsep):
	"""
	Given a search path, find file with requested name
	"""

	result = None
	print ("searching", filename,"...")
	pathext = os.getenv('pathext')
	for path in search_path.split(pathsep):
		#print 'search in', path
		for ext in pathext.split(pathsep):
			ff = filename + ext
			candidate = os.path.join(path, ff)
			#print candidate;

			if os.path.isfile(candidate):
				result = os.path.abspath(candidate)
				print('found in', result)
				break   # just break one inner loop for pathext, will search in next path

	return result


if __name__ == '__main__':
	if len(sys.argv) <= 1:
		print('please specify file to search in path');
		quit()
	for idx in range(1, len(sys.argv)):
		x = sys.argv[idx]
		#print 'search:', x
		res = search_file(x, os.getenv('path'))
	if res == None:
		print("not found in PATH")
