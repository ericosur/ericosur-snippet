#!/usr/bin/env python3
#coding: utf-8

'''
module wand example
given blob and tell which format it is
it is different from the tradition imread (it will decode the input fstream)

https://docs.wand-py.org/en/0.6.12/guide/read.html#read-a-blob
'''

import os
import sys
from wand.image import Image as WandImage


def get_blob_from_file(fn):
    ''' read_oneimg '''
    print('[DEBUG] get_blob_from_file:', fn)
    blob = None
    with open(fn, 'rb') as fobj:
        blob = fobj.read()
    return blob

def identify_blob(blob):
    ''' identify blob after construct a WandImage
        the size of blob should be same as input file
    '''
    with WandImage(blob=blob) as img:
        print(f'S:{len(blob)}, (W:{img.width}, H:{img.height}) format: {img.format}')
    # here img.__exit__

class Solution():
    ''' class solution '''
    files = ['bmp3870.bmp', 'map3850.tif', 'shoelace-knot.png', 'img2668.jpg']

    def __init__(self):
        home = os.getenv('HOME')
        src_dir = os.path.join(home, 'Pictures/data')
        self.srcfiles = [ os.path.join(src_dir, f) for f in Solution.files ]
        self._check_images()

    def _check_images(self):
        ''' check images exists '''
        for f in self.srcfiles:
            if not os.path.exists(f):
                print('[FAIL] fail at once, file not found:', f)
                sys.exit(-1)

    def action(self):
        ''' action '''
        for f in self.srcfiles:
            blob = get_blob_from_file(f)
            identify_blob(blob)

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    Solution.run()

if __name__ == '__main__':
    main()
