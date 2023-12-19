#!/usr/bin/env python3
#coding: utf-8
# pylint: disable=import-error
# pylint: disable=import-outside-toplevel

'''
pbf is bookmark file of Potplayer

such thumbnail is not supported under ubuntu

It is a file encoding UTF16. One of these lines look like:
note: too line in one line they are in one line, no CRLF

```
11=1302791*Book 3*28000000480000004800000001002000040000008108
00000000000000000000000000000000000000000000FFD8FFE0
```

<no>=<timestamp>*<bookmark name>*<hex string of thumbnail>

OSError: Unsupported BMP compression (4)

The image is in the awkward Microsoft BMP V3 format with,
I believe, RLE compression and I don't believe Pillow can handle that.

'''

import binascii
import io
import os
import platform
import re
import sys


def identify_blob(blob):
    ''' identify blob after construct a WandImage
        the size of blob should be same as input file
    '''
    from wand.image import Image as WandImage
    with WandImage(blob=blob) as img:
        print(f'S:{len(blob)}, (W:{img.width}, H:{img.height}) format: {img.format}')

def is_windows():
    ''' check if windows '''
    system_name = platform.system().lower()
    return "windows" in system_name

def output_blob(ofn, blob):
    ''' just output to file '''
    with open(ofn, 'wb') as fobj:
        fobj.write(blob)
    print('output to:', ofn)

def output_opencv(ifn, ofn):
    ''' read and write an image with opencv '''
    import cv2
    if not os.path.exists(ifn):
        print('file not found:', ifn)
        sys.exit(-1)
    img = cv2.imread(ifn)
    if not img:
        print('[FAIL] img is None')
        return
    cv2.imwrite(ofn, img)
    print('output to:', ofn)

def output_imageio(ofn, blob):
    ''' from byte streams '''
    import imageio.v3 as iio
    byte_stream = io.BytesIO(blob)
    frames = iio.imread(byte_stream, index=None)
    iio.imwrite(ofn, frames)

# pylint: disable=not-callable
def output_pillow(ofn, blob):
    ''' output with pillow '''
    from PIL import Image as PILImage
    img = PILImage(blob)
    img.show(ofn)

class Solution():
    ''' class solution '''
    def __init__(self):
        self.fn = None
        #self.the_dict = OrderedDict()
        self.the_dict = {}
        self.the_sorted = {}

    def parse_line(self, ln):
        ''' parse one line '''
        m = re.match(r'^(\d+)=(\d+)\*([^\*]+)\*([0-9a-fA-F]+)$', ln)
        #item = {}
        if m:
            no, timestamp, bookmark, thumbnail = int(m[1]), int(m[2]), m[3], m[4]
            #print(f'[DEBUG] {no}={timestamp}*{bookmark}*{thumbnail[:16]}...')
            #'tn': thumbnail
            self.the_dict[no] = {'ts': timestamp, 'bm': bookmark, 'tn': thumbnail}

    def parse_pbf(self, fn):
        ''' read_pbf '''
        print('parse_pbf:', fn)
        with open(fn, 'rt', encoding='UTF-16') as fobj:
            for ln in fobj.readlines():
                ln = ln.strip()
                self.parse_line(ln)

    @staticmethod
    def dump_dict(the_dict):
        ''' dump '''
        for k, v in the_dict.items():
            print(k, v)

    @staticmethod
    def dump_list(the_list):
        ''' dump '''
        for k in the_list:
            print(k[:2])

    def alter_bookmark_name(self):
        ''' modify the name of bookmark '''
        cnt = 1
        for i in self.the_sorted:
            #print(i[1]['bm'])
            i[1]['bm'] = f'書籤_{cnt}'
            cnt += 1

    def output_pbf(self, ofn):
        ''' output pbf '''
        # specify newline to force it ouput CRLF
        with open(ofn, 'wt', encoding='UTF-16', newline='\r\n') as fobj:
            print('[Bookmark]', file=fobj)
            cnt = 0
            for i in self.the_sorted:
                ts = i[1].get('ts')
                bm = i[1].get('bm')
                tn = i[1].get('tn')
                print(f'{i[0]}={ts}*{bm}*{tn}', file=fobj)
                cnt += 1
            print(f'{cnt}=\n', file=fobj)
        print('output_pbf:', ofn)


    def output_thumbnail(self):
        ''' output thumbnail '''
        for i in self.the_sorted:
            no = i[0]
            tn = i[1].get('tn')
            blob = binascii.unhexlify(tn)
            ifn = f'tmp{no}.bmp'
            output_blob(ifn, blob)
            ofn = f'thumb{no}.bmp'
            output_opencv(ifn, ofn)

    def action(self):
        ''' action '''
        self.parse_pbf('test.pbf')
        #self.dump_dict()

        # type of the_sorted is list (not dict any more)
        self.the_sorted = sorted(self.the_dict.items(), key=lambda item: item[1]['ts'])
        #self.dump_list(self.the_sorted)

        self.alter_bookmark_name()

        # could output blob to file, but cannot decode it well under ubuntu
        # XnViewMP could view such files but I cannot find good module to
        # process it under ubuntu
        if is_windows():
            self.output_thumbnail()

        # UTF-16 LE w/ BOM, CRLF text file
        self.output_pbf('output.pbf')

    @classmethod
    def run(cls):
        ''' run '''
        obj = cls()
        obj.action()

def main():
    ''' main '''
    if not is_windows():
        print('[INFO] not run under windows, will not process thumbnails')
    Solution.run()

if __name__ == '__main__':
    main()
