#!/usr/bin/python
#
# python version of md5, sha1, sha256
#

# may use ''openssl''
#
# openssl dgst -md5 <filename>
# openssl dgst -sha1 <filename>
# openssl dgst -sha256 <filename>
#
# to see more details, use
# openssl dgst -h

import sys
import hashlib

# argument processing
if len(sys.argv) > 1:
	fname = sys.argv[1]
	print("process file %s" % fname)
else:
	print("no file name is specified")
	sys.exit()

fp = open(fname, "rb")	# need open as binary mode
m = hashlib.md5()
m.update( fp.read() )
print("md5: ", m.hexdigest())

fp.seek(0, 0)
s1 = hashlib.sha1()
s1.update( fp.read() )
print('sha1: ', s1.hexdigest())

fp.seek(0, 0)
s2 = hashlib.sha256()
s2.update( fp.read() )
print('sha256: ', s2.hexdigest())

fp.close()

'''
# this section of code not work after python 3
# the module 'md5' has been moved to 'hashlib'

import sys
import md5
import sha

# argument processing
if len(sys.argv) > 1:
	fname = sys.argv[1]
	print("process file %s" % fname)
else:
	print("no file name is specified")
	sys.exit()

file = open(fname, 'r')
md5_hash = md5.new()
md5_hash.update( file.read() )

file.seek(0, 0);
sha_hash = sha.new()
sha_hash.update(file.read())

print("md5: ", md5_hash.hexdigest())
print("sha1:", sha_hash.hexdigest())

file.close()
'''