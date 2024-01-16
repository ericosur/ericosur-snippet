#!/usr/bin/python

'''python version of md5, sha1, sha256'''


# may use ''openssl''
#
# openssl dgst -md5 <filename>
# openssl dgst -sha1 <filename>
# openssl dgst -sha256 <filename>
#
# simple command:
# openssl sha256 <filename>
#
# to see more details, use
# openssl dgst -h

from __future__ import print_function
import sys
import hashlib

def main():
    '''main function'''
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        print(f"process file {fname}")
    else:
        print("no file name is specified")
        sys.exit()

    # need open as binary mode
    with open(fname, "rb") as fp:
        m = hashlib.md5()
        m.update(fp.read())
        print("md5: ", m.hexdigest())

        fp.seek(0, 0)
        s1 = hashlib.sha1()
        s1.update(fp.read())
        print('sha1: ', s1.hexdigest())

        fp.seek(0, 0)
        s2 = hashlib.sha256()
        s2.update(fp.read())
        print('sha256: ', s2.hexdigest())


if __name__ == '__main__':
    main()
