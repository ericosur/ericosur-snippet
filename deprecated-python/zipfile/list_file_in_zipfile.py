#!/usr/bin/env python3
# coding: utf-8

''' list file in zip '''

#import re
import zipfile
import myutil

def main():
    ''' main '''
    jsonf = 'setting.json'
    data = myutil.read_jsonfile(jsonf)
    # use get() instead of 'operator []' to prevent exeception
    zfile = data.get('go.py').get('zipfile')

    if not myutil.isfile(zfile):
        print('specified file not found: %s' % zfile)
        return

    zf = zipfile.ZipFile(zfile, 'r')
    print('zipfile: {}\n{}'.format(zfile, '-' * 40))
    flist = zf.namelist()
    for ff in flist:
        print(ff)

    zf.close()

if __name__ == '__main__':
    main()
