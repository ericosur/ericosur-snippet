#!/usr/bin/env python

import myutil
import re, zipfile


def main():
    jsonf = 'setting.json'
    data = myutil.read_jsonfile(jsonf)
    # use get() instead of 'operator []' to prevent exeception
    zfile = data.get('go.py').get('zipfile')

    if not myutil.isfile(zfile):
        print('specified file not found: %s' % zfile)
        return
    else:
        #print("zfile:{}".format(zfile))
        pass

    foo = zipfile.ZipFile(zfile, 'r')
    print('zipfile: {}\n{}'.format(zfile, '-' * 40))
    flist = foo.namelist()
    for ff in flist:
        print(ff)

    foo.close()

if __name__ == '__main__':
    main()
